import streamlit as st
import os
import traceback
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

# --- Streamlit UI setup ---
st.set_page_config(page_title="Extractions Research Chat", layout="wide")
st.title("🧬 Ask Me Anything: Lab Workflow Research (Extractions)")
st.caption("Powered by Hugging Face (No OpenAI Required)")

# --- Embedded transcript ---
transcript = """
The extractions team at Natera works across three shifts, with 166 people in total. 
They use Google Sheets for tracking performance and scheduling, and communicate via Google Chat and Tasks. 
Key pain points include Advantage 1.0 being slow, limited platform support, and instrument or shipping delays. 
There’s a push for automation, especially around scheduling and instrument tracking. 
Some staff also write Snowflake queries to support their work. 
The Extractions Manager is helping scale the Altera assay and interfaces with platform teams.
"""

st.success("✅ Transcript loaded.")

# --- Display the transcript ---
with st.expander("📄 View Original Interview Transcript"):
    st.text(transcript[:5000])

# --- Input box (always visible) ---
query = st.text_input("❓ Ask a question about the extractions team's user research")

# --- Vectorstore creation ---
try:
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = [Document(page_content=transcript)]
    split_docs = splitter.split_documents(docs)

    embeddings = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}  # Safe for Streamlit Cloud (no GPU)
    )

    vectorstore = FAISS.from_documents(split_docs, embeddings)

except Exception as e:
    st.error(f"❌ Error during vectorstore creation: {e}")
    st.code(traceback.format_exc())
    st.stop()

# --- Handle query and display result ---
if query:
    st.markdown(f"**💬 You asked:** {query}")
    response = None

    try:
        token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not token:
            raise ValueError("❌ Hugging Face token is missing. Add it to Streamlit secrets.")

        # ✅ Use supported Hugging Face model
        llm = HuggingFaceHub(
            repo_id="declare-lab/flan-alpaca-base",
            task="text2text-generation",
            model_kwargs={"temperature": 0.5, "max_length": 512}
        )

        # ✅ Use RetrievalQA to combine retriever and LLM
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            chain_type="stuff",
            return_source_documents=False
        )

        response = qa_chain.run(query)

    except Exception as e:
        st.error("❌ An error occurred while generating the response.")
        st.code(traceback.format_exc())
        response = None

    if response:
        st.markdown(f"**🤖 AI says:** {response}")
    else:
        st.warning("⚠️ No response generated.")
