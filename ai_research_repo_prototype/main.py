import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.docstore.document import Document
from langchain.chains.question_answering import load_qa_chain
import os

# --- Streamlit UI setup ---
st.set_page_config(page_title="Extractions Research Chat", layout="wide")
st.title("🧬 Ask Me Anything: Lab Workflow Research (Extractions)")
st.caption("Powered by Hugging Face (No OpenAI Required)")

# --- Embed the transcript directly ---
transcript = """
The extractions team at Natera works across three shifts, with 166 people in total. 
They use Google Sheets for tracking performance and scheduling, and communicate via Google Chat and Tasks. 
Key pain points include Advantage 1.0 being slow, limited platform support, and instrument or shipping delays. 
There’s a push for automation, especially around scheduling and instrument tracking. 
Some staff also write Snowflake queries to support their work. 
The Extractions Manager is helping scale the Altera assay and interfaces with platform teams.
"""

st.success("✅ Transcript loaded.")

# --- Display original text ---
with st.expander("📄 View Original Interview Transcript"):
    st.text(transcript[:5000])

# --- Embed text chunks ---
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = [Document(page_content=transcript)]
split_docs = splitter.split_documents(docs)

# --- Embed with sentence-transformers ---
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(split_docs, embeddings)

# --- Question input ---
query = st.text_input("❓ Ask a question about the extractions team's user research")

# --- Model and response handling ---
if query:
    with st.spinner("🤖 Thinking..."):
        try:
            # Confirm Hugging Face token exists
            if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
                raise ValueError("HUGGINGFACEHUB_API_TOKEN is missing from environment or Streamlit secrets.")

            retriever = vectorstore.as_retriever()
            relevant_docs = retriever.get_relevant_documents(query)

            llm = HuggingFaceHub(
                repo_id="google/flan-t5-large",
                model_kwargs={"temperature": 0.5, "max_length": 512}
            )

            qa_chain = load_qa_chain(llm, chain_type="stuff")
            response = qa_chain.run(input_documents=relevant_docs, question=query)

        except Exception as e:
            response = f"❌ Failed to load model or generate response:\n\n{str(e)}"

    st.markdown(f"**💬 You asked:** {query}")
    st.markdown(f"**🤖 AI says:** {response}")
