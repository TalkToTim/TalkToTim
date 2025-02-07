
def main(api_key=''):
    st.set_page_config(page_icon="💬2️⃣🧑🏻‍💻", page_title="Talk To Tim")

    with st.container():
        st.markdown("<h1 style='color: #9b4dca;'>Say Hi to Tim!</h1>", unsafe_allow_html=True)

    # Sidebar for settings
    with st.sidebar:
        st.header("Settings")
        difficulty_level = st.radio("Select difficulty level:", ["Junior", "Mid", "Senior", "Staff"])
        explanation_level = st.radio("Select explanation level:", ["Brief", "Detailed"])
        friendliness = st.radio("Select friendliness level:", ["Friendly", "Neutral", "Formal"])

    # User query input
    question = st.text_input("Enter a query regarding an interview", "")

    if question:
        answer = ask_llm(
            question,
            difficulty_level=difficulty_level.lower(),
            explanation_level=explanation_level.lower(),
            friendliness=friendliness.lower(),
            api_key=api_key
        )
        st.write(f"The response of the LLM is: {answer}")


if __name__ == "__main__":
    import sys
    import os
    from dotenv import load_dotenv
    import os


    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    dotenv_path = os.path.join(os.path.dirname(__file__), "..\\..\\resources\\.env")

    load_dotenv(dotenv_path)
    api_key = os.getenv("OPENAI_API_KEY")

    use_dummy_llm = False
    if use_dummy_llm:
        from llms_backend.ask_for_interview_play import ask_chatgpt_for_interview_dummy as ask_llm
    else:
        from llms_backend.ask_for_interview_play import ask_chatgpt_for_interview as ask_llm
    import streamlit as st
    main(api_key=api_key)
