import os
import streamlit as st
import google.generativeai as genai

st.title("我的 AI 助手")

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("未設定 API Key，請檢查 Settings 裡的 Secrets！")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    user_input = st.text_area("請輸入問題：")

    if st.button("送出"):
        if user_input:
            with st.spinner("AI 思考中..."):
                response = model.generate_content(user_input)
                st.write(response.text)
        else:
            st.warning("請輸入內容！")
