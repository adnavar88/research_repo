import streamlit as st
from pathlib import Path

# --- Minimal Streamlit app to confirm file + input box work ---
st.set_page_config(page_title="Lab Workflow Transcript Viewer", layout="wide")
st.title("📄 Lab Research Transcript Viewer")
st.caption("This app just reads your transcript file and shows a chat box")

# --- Load transcript.txt ---
file_path = Path("transcript.txt")
if file_path.exists():
    transcript = file_path.read_text(encoding="utf-8")
    st.success("✅ transcript.txt loaded successfully.")
else:
    st.error("❌ transcript.txt not found.")
    st.stop()

# --- Preview transcript ---
with st.expander("📄 View Transcript Preview"):
    st.text(transcript[:5000])  # Show first 5000 characters only

# --- Input box ---
query = st.text_input("❓ Ask a question (AI not enabled yet)")

if query:
    st.markdown(f"**💬 You asked:** {query}")
    st.info("🧠 This is just a placeholder. No AI response yet.")
