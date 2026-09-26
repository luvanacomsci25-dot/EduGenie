import streamlit as st
import google.generativeai as genai
st.set_page_config(page_title="EduGenie", page_icon="🎓")
st.title("🎓 EduGenie - AI Learning Assistant")
api_key = st.sidebar.text_input("Gemini API Key", type="password")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    q = st.text_input("Un Kelvi Enna?")
    if st.button("Ask 🚀"):
        if q:
            res = model.generate_content(f"Answer simply in Tanglish: {q}")
            st.success(res.text)
else:
    st.info("Sidebar la API Key podu da!")
