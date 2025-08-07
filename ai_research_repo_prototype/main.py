import streamlit as st
from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

# --- Streamlit UI setup ---
st.set_page_config(page_title="Extractions Research Chat", layout="wide")
st.title("🧬 Ask Me Anything: Lab Workflow Research (Extractions)")
st.caption("Based on interviews from the UX research archive")

# --- Load transcript from file ---
file_path = Path("text.txt")  # ✅ your new filename

if file_path.exists():
    transcript = file_path.read_text(encoding="utf-8")
    st.success("✅ Transcript loaded successfully.")
else:
    st.error("Transcript file not found. Please make sure 'text.txt' is in the same folder as main.py.")
    st.stop()

# --- Display original text ---
with st.expander("📄 View Original Interview Transcript"):
    st.text(transcript[:5000])  # Show first 5000 chars

# --- Process text for embedding ---
docs = [Document(page_content=transcript)]
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# --- Vectorstore + Embeddings ---
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(split_docs, embeddings)

# --- LLM and QA chain ---
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = load_qa_chain(llm, chain_type="stuff")

# --- User question input ---
query = st.text_input("❓ Ask a question about the extractions team's user research")

if query:
    with st.spinner("🤖 Thinking..."):
        retriever = vectorstore.as_retriever(_
