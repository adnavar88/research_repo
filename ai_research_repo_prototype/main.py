import streamlit as st
from pathlib import Path
import re

# --- Streamlit UI setup ---
st.set_page_config(page_title="Lab Research Q&A (Keyword Search)", layout="wide")
st.title("🔍 Lab Research Transcript Q&A")
st.caption("Ask a question — we'll return relevant text directly from text.txt")

# --- Load local text.txt ---
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

# --- Display preview ---
with st.expander("📄 View Transcript Preview"):
    st.text(transcript[:1000])

# --- Input box ---
query = st.text_input("❓ Ask a question or enter a keyword (no AI, keyword-based snippet matching)")

# --- Snippet retrieval (simple and effective) ---
if query:
    st.markdown(f"**💬 You asked:** {query}")

    # Clean and split transcript into lines or chunks
    sentences = [s.strip() for s in transcript.split("\n") if s.strip()]
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    matches = [s for s in sentences if pattern.search(s)]

    if matches:
        st.markdown("### 🔍 Relevant Matches")
        for match in matches[:10]:
            st.markdown(f"🟢 {match}")
    else:
        st.warning("⚠️ No matching snippets found. Try simpler or alternative keywords.")
