import streamlit as st
import os
import traceback
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceHubEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

# --- Streamlit UI setup ---
st.set_page_config(page_title="Lab Research Q&A", layout="wide")
st.title("🧬 Lab Research Q&A (with AI)")
st.caption("Using Hugging Face embeddings and flan-t5-small to answer from text.txt")

# --- Load text.txt (must be in same folder as main.py) ---
try:
    base_path = Path(__file__).parent
    file_path = base_path / "text.txt"
    st.write(f"📍 Checking file path: `{file_path.resolve()}`")

    if not file_path.exists():
        raise FileNotFoundError(f"File not found at: {file_path.resolve()}")

    transcript = file_path.read_text(encoding="utf-8")
    st.success("✅ text.txt loaded successfully.")
except Exception as e:
    st.error("❌ Could not load text.txt.")
    st.code(str(e))
    st.stop()

# --- Show preview ---
with st.expander("📄 View Transcript Preview"):
    st.text(transcript[:1000])  # Preview first 1000 chars

# --- Input box ---
query = st.text_input("❓ Ask a question based on the transcript")

# --- Build vectorstore ---
try:
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = [Document(page_content=transcript)]
    split_docs = splitter.split_documents(docs)

    embeddings = HuggingFaceHubEmbeddings(
        repo_id="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(split_docs, embeddings)

except Exception as e:
    st.error("❌ Error during embedding or vectorstore creation.")
    st.code(traceback.format_exc())
    st.stop()

# --- Handle query and run QA chain ---
if query:
    st.markdown(f"**💬 You asked:** {query}")
    try:
        token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not token:
            raise ValueError("Missing HUGGINGFACEHUB_API_TOKEN in Streamlit secrets.")

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
        st.markdown(f"**🤖 AI says:** {response}")

    except Exception as e:
        st.error("❌ AI failed to generate a response.")
        st.code(traceback.format_exc())
