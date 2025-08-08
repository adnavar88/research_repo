import streamlit as st
import re
from pathlib import Path

# --- UI Setup ---
st.set_page_config(page_title="Lab Transcript Search", layout="wide")
st.title("📄 Lab Workflow Transcript Q&A")
st.caption("Reads from text.txt — no upload needed.")

# --- Load text.txt ---
try:
    file_path = Path("text.txt")
    if not file_path.exists():
        raise FileNotFoundError("File not found at: " + str(file_path.resolve()))

    transcript = file_path.read_text(encoding="utf-8")
    st.success("✅ text.txt loaded successfully.")
except Exception as e:
    st.error("❌ Could not load text.txt.")
    st.code(str(e))
    st.stop()

# --- Show preview of the transcript ---
with st.expander("📄 View Transcript Preview"):
    st.text(transcript[:5000])  # Limit preview

# --- Search box ---
query = st.text_input("❓ Ask a question or enter a keyword (no AI, keyword search only)")

if query:
    st.markdown(f"**💬 You asked:** {query}")

    # --- Keyword search
    sentences = transcript.split("\n")
    matches = [s for s in sentences if re.search(query, s, re.IGNORECASE)]

    if matches:
        st.markdown("**🔍 Matching lines:**")
        for match in matches[:10]:
            st.markdown(f"- {match}")
    else:
        st.warning("⚠️ No matching lines found.")
