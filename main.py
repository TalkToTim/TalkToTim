import streamlit as st

# App title
st.set_page_config(page_icon="💬2️⃣🧑🏻‍💻", page_title="Talk To Tim")

user_prompt = st.chat_input("Say something")
if user_prompt:
    st.write(f"User has sent the following prompt: {user_prompt}")