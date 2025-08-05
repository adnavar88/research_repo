import streamlit as st

# Set page config
st.set_page_config(page_title="Extractions Research Chat", layout="wide")

st.title("🧬 Ask Me Anything: Lab Workflow Research (Extractions)")
st.caption("Based on interview with the Extractions Manager at Natera")

# Display transcript link
with st.expander("📄 View Original Transcript"):
    st.markdown("[Read the full interview on Granola](https://notes.granola.ai/d/c500ce14-882f-4c3c-b6dd-ca867944b030)")

# Simulated knowledge base from the interview
context = {
    "tools": "The Extractions Manager's team uses Google Sheets (for scheduling and performance tracking), Google Chat, and Google Tasks.",
    "team_structure": "The extractions team has 166 people working 24/7 across 3 shifts, with daily huddles and supervisor group chats.",
    "metrics": "SLAs: Prospera – 6 hours, Panorama – 24 hours. Also tracks training completion, attendance, error rates.",
    "pain_points": "Advantage 1.0 is slow and under-supported. Communication is tough across 160+ people. Shipping and instrument delays cause bottlenecks.",
    "improvements": "There's interest in automating daily schedules with Python, tracking instruments, and reducing Google Sheet usage. Some staff use Snowflake scripts.",
    "project": "The Extractions Manager is involved in bringing Altera assay in-house, giving feedback to platform teams, and ensuring scalability."
}

# Input box
query = st.text_input("❓ Ask a question about the extractions team's user research")

# Simple rule-based QA logic (simulating GPT response based on transcript)
if query:
    query_lower = query.lower()
    response = "🤖 Hmm, I couldn’t find anything in the interview that matches your question."

    if "tools" in query_lower or "software" in query_lower:
        response = context["tools"]
    elif "team" in query_lower or "structure" in query_lower or "shift" in query_lower:
        response = context["team_structure"]
    elif "metric" in query_lower or "sla" in query_lower or "okrs" in query_lower:
        response = context["metrics"]
    elif "challenge" in query_lower or "pain" in query_lower or "issue" in query_lower:
        response = context["pain_points"]
    elif "improve" in query_lower or "automation" in query_lower or "solution" in query_lower:
        response = context["improvements"]
    elif "altera" in query_lower or "project" in query_lower:
        response = context["project"]

    st.markdown(f"**💬 You asked:** {query}")
    st.markdown(f"**🤖 AI says:** {response}")
