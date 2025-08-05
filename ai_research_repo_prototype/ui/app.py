
import streamlit as st

st.set_page_config(page_title="User Research GPT", layout="wide")
st.title("🔍 AI-Powered Research Assistant")

query = st.text_input("What do you want to know from past research?")

if query:
    st.write("Fetching insights for:", query)
    st.success("🚧 Prototype only – connect to LangChain backend to fetch results.")
