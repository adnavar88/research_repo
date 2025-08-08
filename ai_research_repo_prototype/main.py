import streamlit as st

st.set_page_config(page_title="Keyword-Based Lab Q&A", layout="wide")
st.title("🧬 Lab Research Transcript Search")
st.caption("Simple and reliable keyword-based Q&A — no models required.")

# --- Upload transcript file ---
uploaded_file = st.file_uploader("📤 Upload your transcript.txt file", type=["txt"])

if uploaded_file:
    transcript = uploaded_file.read().decode("utf-8")
    st.success("✅ transcript.txt loaded successfully.")

    with st.expander("📄 View Transcript Preview"):
        st.text(transcript[:5000])  # Preview only

    # --- Question input ---
    query = st.text_input("❓ Ask a question (we’ll search for matching phrases)")

    if query:
        st.markdown(f"**💬 You asked:** {query}")

        # --- Basic keyword match
        import re

        sentences = transcript.split("\n")
        matches = [s for s in sentences if re.search(query, s, re.IGNORECASE)]

        if matches:
            st.markdown("**🔍 Found matching content:**")
            for match in matches[:5]:  # Limit to top 5 matches
                st.markdown(f"- {match}")
        else:
            st.warning("⚠️ No exact matches found. Try rephrasing or using simpler keywords.")
else:
    st.info("👈 Please upload a `.txt` transcript to begin.")
