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
st.set_page_config(page_title="Lab Research Q&A", layout="wide")
st.title("🧬 Ask Me Anything: Lab Workflow Research")
st.caption("Powered by Hugging Face + LangChain")

# --- File uploader ---
uploaded_file = st.file_uploader("📤 Upload your transcript.txt file", type=["txt"])

if uploaded_file:
    try:
        transcript = uploaded_file.read().decode("utf-8")
        st.success("✅ transcript.txt loaded.")
    except Exception as e:
        st.error("❌ Failed to read uploaded file.")
        st.code(str(e))
        st.stop()

    # Show preview
    with st.expander("📄 View Transcript Preview"):
        st.text(transcript[:5000])

    # Input box
    query = st.text_input("❓ Ask a question about lab workflows, systems, or pain points")

    # Chunking and embeddings
    try:
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = [Document(page_content=transcript)]
        split_docs = splitter.split_documents(docs)

        embeddings = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )

        vectorstore = FAISS.from_documents(split_docs, embeddings)

    except Exception as e:
        st.error("❌ Failed to process transcript.")
        st.code(traceback.format_exc())
        st.stop()

    # AI response
    if query:
        st.markdown(f"**💬 You asked:** {query}")
        response = None

        try:
            token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
            if not token:
                raise ValueError("Missing Hugging Face API token. Add it to Streamlit secrets.")

            llm = HuggingFaceHub(
                repo_id="google/flan-t5-small",
                task="text2text-generation",
                model_kwargs={"temperature": 0.5, "max_length": 512}
            )

            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                retriever=vectorstore.as_retriever(),
                chain_type="stuff",
                return_source_documents=False
            )

            response = qa_chain.run(query)

        except Exception as e:
            st.error("❌ Failed to generate AI response.")
            st.code(traceback.format_exc())

        if response:
            st.markdown(f"**🤖 AI says:** {response}")
        else:
            st.warning("⚠️ No response generated.")
else:
    st.info("👈 Please upload a transcript file to get started.")
