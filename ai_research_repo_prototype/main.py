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
file_path = Path("research_docs/Lab Workflow UX Research Interviews.txt")

# 🔍 Debugging output
st.write("📁 Files in research_docs folder:", list(Path("research_docs").glob("*")))

if file_path.exists():
    transcript = file_path.read_text(encoding="utf-8")
else:
    st.error("Transcript file not found. Please upload 'Lab Workflow UX Research Interviews.txt' to the research_docs folder.")
    st.stop()

# --- Display original text ---
with st.expander("📄 View Original Interview Transcript"):
    st.text(transcript[:5000])  # Only show first 5000 chars for readability

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
        retriever = vectorstore.as_retriever()
        relevant_docs = retriever.get_relevant_documents(query)
        response = qa_chain.run(input_documents=relevant_docs, question=query)

    st.markdown(f"**💬 You asked:** {query}")
    st.markdown(f"**🤖 AI says:** {response}")

