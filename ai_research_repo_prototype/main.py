import streamlit as st

# --- Streamlit UI setup ---
st.set_page_config(page_title="Lab Transcript Viewer", layout="wide")
st.title("📄 Lab Research Transcript Viewer")
st.caption("Upload your transcript file and ask a question. AI coming next.")

# --- Upload .txt file ---
uploaded_file = st.file_uploader("📤 Upload your transcript.txt file", type=["txt"])

if uploaded_file:
    # --- Read transcript content ---
    try:
        transcript = uploaded_file.read().decode("utf-8")
        st.success("✅ transcript.txt loaded successfully.")
    except Exception as e:
        st.error("❌ Could not read uploaded file.")
        st.code(str(e))
        st.stop()

    # --- Show preview of file ---
    with st.expander("📄 View Transcript Preview"):
        st.text(transcript[:5000])  # Show first 5000 characters

    # --- User input box ---
    query = st.text_input("❓ Ask a question based on the transcript")

    if query:
        st.markdown(f"**💬 You asked:** {query}")
        st.info("🧠 Placeholder only - AI coming next.")

else:
    st.info("👈 Please upload a `.txt` transcript file to begin.")
