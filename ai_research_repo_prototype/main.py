import streamlit as st
from pathlib import Path

# --- UI setup ---
st.set_page_config(page_title="Lab Transcript Debug", layout="wide")
st.title("📄 Lab Research Transcript Debug")
st.caption("This app confirms whether text.txt is being found and read correctly.")

# --- Attempt to read text.txt ---
try:
    file_path = Path(__file__).parent / "text.txt"  # Ensure relative to main.py
    st.write(f"📍 Checking path: `{file_path.resolve()}`")

    if not file_path.exists():
        raise FileNotFoundError("File not found at: " + str(file_path.resolve()))

    transcript = file_path.read_text(encoding="utf-8")
    st.success("✅ text.txt loaded successfully!")

    with st.expander("📄 Transcript Preview"):
        st.text(transcript[:1000])  # Show first 1000 characters

except Exception as e:
    st.error("❌ Failed to load text.txt.")
    st.code(str(e))
    st.stop()

# --- Query input ---
query = st.text_input("❓ Ask a question or enter a keyword (no AI yet)")

if query:
    st.markdown(f"**💬 You asked:** {query}")
    st.info("🧠 AI will be added after file load is confirmed.")
