import streamlit as st

st.set_page_config(page_title="Lab Transcript Viewer", layout="wide")
st.title("📄 Lab Research Transcript Viewer")
st.caption("Upload your transcript file and ask a question.")

# --- Upload transcript file ---
uploaded_file = st.file_uploader("📤 Upload your transcript.txt file", type=["txt"])

if uploaded_file:
    transcript = uploaded_file.read().decode("utf-8")
    st.success("✅ transcript.txt loaded from upload.")

    # --- Show preview ---
    with st.expander("📄 View Transcript Preview"):
        st.text(transcript[:5000])

    # --- Input box ---
    query = st.text_input("❓ Ask a question (AI not enabled yet)")

    if query:
        st.markdown(f"**💬 You asked:** {query}")
        st.info("🧠 This is just a placeholder. No AI response yet.")
else:
    st.info("👈 Please upload a transcript file to begin.")
 — AI coming next.")
