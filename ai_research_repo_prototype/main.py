import streamlit as st
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

# --- Embed the transcript directly ---
transcript = """
[PASTE YOUR FULL INTERVIEW TEXT HERE]

Example:
The extractions team at Natera works across three shifts, with 166 people in total. They use Google Sheets for tracking performance, and communicate using Google Chat and Tasks...
"""

st.success("✅ Transcript embedded and loaded successfully.")

# --- Display original text ---
with st.expander("📄 View Original Interview Transcript"):
    st.text(transcript[:5000])  # Show first 5000 characters

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
