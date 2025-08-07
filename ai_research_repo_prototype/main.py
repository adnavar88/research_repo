import streamlit as st
import pkgutil

# --- Streamlit UI setup ---
st.set_page_config(page_title="Lab Transcript Viewer", layout="wide")
st.title("📄 Lab Research Transcript Viewer")
st.caption("This app confirms the transcript file is loading correctly and shows a question box.")

# --- Load transcript.txt using pkgutil ---
try:
    transcript_bytes = pkgutil.get_data(__name__, "transcript.txt")
    if transcript_bytes is None:
        raise FileNotFoundError("Streamlit build did not include transcript.txt.")
    transcript = transcript_bytes.decode("utf-8")
    st.success("✅ transcript.txt loaded successfully.")
except Exception as e:
    st.error("❌ Failed to load transcript.txt.")
    st.code(str(e))
    st.stop()

# --- Show preview of transcript ---
with st.expander("📄 View Transcript Preview"):
    st.text(transcript[:5000])  # Show first 5000 characters

# --- User question input ---
query = st.text_input("❓ Ask a question (AI not enabled yet)")

if query:
    st.markdown(f"**💬 You asked:** {query}")
    st.info("🧠 This is just a placeholder. No AI response yet.")
