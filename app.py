import streamlit as st
from langchain_script import generate_script

st.set_page_config(page_title="Custom Script Generator", layout="centered")

st.title("🎬 Custom Script Generator using Gemini")
st.markdown("Generate creative scripts for influencers, brands, and more!")

user_input = st.text_area("Enter your prompt (e.g. GRWM, monsoon ad, picnic reel, etc.)")

if st.button("Generate Script"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating script..."):
            script = generate_script(user_input)
        st.success("✅ Script generated!")
        st.text_area("Generated Script", script, height=300)
