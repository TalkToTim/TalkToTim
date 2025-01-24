import streamlit as st

# App title
st.set_page_config(page_icon="💬2️⃣🧑🏻‍💻", page_title="Talk To Tim")

user_prompt = st.chat_input("Say something")
if user_prompt:
    with st.chat_message("user"):
        st.write(f"User: {user_prompt}")