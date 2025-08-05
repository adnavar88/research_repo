import streamlit as st

# Set up the page
st.set_page_config(page_title="User Research GPT", layout="wide")
st.title("🔍 AI-Powered Research Assistant")
st.caption("Ask me anything from past user research: pain points, quotes, patterns, or themes.")

# Show prompt examples
with st.expander("🤖 Try asking things like..."):
    st.markdown("""
    - What do users say about the onboarding flow?
    - Show quotes about pricing confusion
    - Summarize usability test insights from July
    - Did we talk to Gen Z users about notifications?
    """)

# Input box
query = st.text_input("🔎 Enter your research question:")

# Simulated placeholder response
if query:
    st.write(f"📥 Fetching insights for: **{query}**")
    st.success("✅ This is a prototype — GPT response would appear here once connected to your backend.")
