import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Lab Transcript Viewer", layout="wide")
st.title("📄 Lab Research Transcript Viewer")
st.caption("Confirms file is loading and input box is working.")

# --- Load transcript.txt the classic way ---
try:
    file_path = Path(__file__).parent / "transcript.txt"
    if not file_path.exists():
        raise FileNotFoundError("File not found at: " + str(file_path.resolve()))

    transcript = file_path.read_text(encoding="utf-8")
    st.success("✅ transcript.txt loaded successfully.")
except Exception as e:
    st.error("❌ Could not load transcript.txt.")
    st.code(str(e))
    st.stop()

# --- Show preview ---
with st.expander("📄 View Transcript Preview"):
    st.text(transcript[:5000])

# --- Input box ---
query = st.text_input("❓ Ask a question (AI not enabled yet)")

if query:
    st.markdown(f"**💬 You asked:** {query}")
    st.info("🧠 Placeholder only — AI coming next.")
