import streamlit as st
from orchestrator import main

st.title("AI Research Assistant (Gemini-powered)")
topic = st.text_input("Enter research topic:")

if st.button("Generate Report"):
    main(topic)
    st.success(f"Report for '{topic}' generated!")
