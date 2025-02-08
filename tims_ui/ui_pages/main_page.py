"""
This is the main page of the UI. It contains the main function that is called when the UI is run.
Includes connection to the backend (with the LLM).
"""

def initialize_botton_values(st, ui_config):
    # Init radio buttons values
    ui_init_radio_values = ui_config['ui_init_radio']
    if "difficulty_level" not in st.session_state:
        st.session_state.difficulty_level = ui_init_radio_values['difficulty_level']
    if "explanation_level" not in st.session_state:
        st.session_state.explanation_level = ui_init_radio_values['explanation_level']
    if "friendliness" not in st.session_state:
        st.session_state.friendliness = ui_init_radio_values['friendliness']

    # Use session_state to persist values
    ui_radio_options = ui_config['ui_radio_options']
    st.session_state.difficulty_level = st.radio(
        "Select difficulty level:", ui_radio_options['difficulty_level'],
        index=ui_radio_options['difficulty_level'].index(st.session_state.difficulty_level)
    )

    st.session_state.explanation_level = st.radio(
        "Select explanation level:", ui_radio_options['explanation_level'],
        index=ui_radio_options['explanation_level'].index(st.session_state.explanation_level)
    )

    st.session_state.friendliness = st.radio(
        "Select friendliness level:", ui_radio_options['friendliness'],
        index=ui_radio_options['friendliness'].index(st.session_state.friendliness)
    )


def main(api_key=''):
    from resources import config
    ui_config = config.ui_params
    st.set_page_config(page_icon="💬2️⃣🧑🏻‍💻", page_title="Talk To Tim")

    with st.container():
        st.markdown("<h1 style='color: #9b4dca;'>Say Hi to Tim!</h1>", unsafe_allow_html=True)

    # Sidebar for settings
    with st.sidebar:
        st.header("Settings")
        initialize_botton_values(st=st, ui_config=ui_config)

    # Trigger calls on "Enter"
    with st.form("query_form"):
        question = st.text_input("Enter a query regarding an interview", "")
        submitted = st.form_submit_button("Submit")

    # Trigger LLM call only when the user presses "Enter" or "Submit"
    if submitted and question:
        answer = ask_llm(
            question,
            difficulty_level=st.session_state.difficulty_level.lower(),
            explanation_level=st.session_state.explanation_level.lower(),
            friendliness=st.session_state.friendliness.lower(),
            api_key=api_key
        )
        st.write(f"{answer}")


if __name__ == "__main__":
    import sys
    import os
    from dotenv import load_dotenv
    import os
    import streamlit as st


    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    dotenv_path = os.path.join(os.path.dirname(__file__), "..\\..\\resources\\.env")

    load_dotenv(dotenv_path)
    api_key = os.getenv("OPENAI_API_KEY")

    use_dummy_llm = False
    if use_dummy_llm:
        from llms_backend.ask_for_interview_play import ask_chatgpt_for_interview_dummy as ask_llm
    else:
        from llms_backend.ask_for_interview_play import ask_chatgpt_for_interview as ask_llm
    main(api_key=api_key)
