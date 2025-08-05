import streamlit as st

st.set_page_config(page_title="Lab Workflow UX Research", layout="wide")

st.title("🧬 Lab Workflow UX Research Interview")
st.subheader("Marco Montenegro – Extractions Department Manager")
st.caption("Interview conducted by digomez@natera.com on Thu, 17 Jul 2025")

st.markdown("### 🧑‍🔬 Background & Role")
st.markdown("""
- 11 years at Natera, Extractions Department Manager  
- Team: 166 people (targeting 183 by year-end), 24/7 operations across 3 shifts  
- Education: UC San Diego microbiology, earned CGMBS license through Natera program  
- Department role: DNA extraction for all downstream teams (Panorama, Signatera, Verizon, tissue, etc.)
""")

st.markdown("### 🛠 Current Workflow & Tools")
st.markdown("""
- **Primary tools:** Google Sheets, Google Chat, Google Tasks  
- **Schedule management:**  
  - Shared Google Sheets with color-coded station assignments  
  - Accessible across shifts for real-time planning  
- **Performance tracking:**  
  - Custom Google Sheets for sample metrics and batch monitoring  
- **Communication:**  
  - Supervisor group chats  
  - Daily huddles  
  - In-person shift handoffs
""")

st.markdown("### 🤝 Decision Making & Project Involvement")
st.markdown("""
- **Project:** Altera assay internalization (moving from send-out to in-house testing)  
- Role in software design feedback and production scalability  
- Collaborates with platform teams and lab informatics  
- Provides input on operator workflow optimization
""")

st.markdown("### 📊 Performance Metrics & OKRs")
st.markdown("""
- **SLAs by product:**  
  - Prospera: 6-hour turnaround from receipt  
  - Panorama: 24-hour turnaround from receipt  
- **Additional metrics:**  
  - Error minimization  
  - 95% training completion  
  - Attendance/compliance  
- **Recognition:**  
  - Verbal acknowledgment and performance transparency
""")

st.markdown("### ⚠️ Pain Points & Challenges")
st.markdown("""
- **Advantage 1.0 software limitations:**  
  - Slow loading times  
  - Limited engineering resources  
  - Focus diverted to new systems  
- **Team communication scale:** 160+ people over 3 shifts  
- **Operational bottlenecks:**  
  - Instrument downtime  
  - FedEx delays (Memphis hub)  
  - Transport lag from Pleasanton  
- **Email overload from automated systems**
""")

st.markdown("### 🚀 Improvement Opportunities")
st.markdown("""
- **Automation ideas:**  
  - Daily schedule scripting (Python)  
  - Instrument status dashboard  
  - Eliminate manual Google Sheets workflows  
- **Team-driven innovation:**  
  - Internal automation proposals by staff  
  - Snowflake scripts for rapid data pulls  
- **Staffing growth:**  
  - Additional managers/supervisors  
  - Challenges accessing Manager Development Program (MDP) on time
""")

st.markdown("---")
st.markdown("📄 **Full transcript:** [View on Granola](https://notes.granola.ai/d/c500ce14-882f-4c3c-b6dd-ca867944b030)")
