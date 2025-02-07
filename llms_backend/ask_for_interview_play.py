# Function to configure and interact with ChatGPT for an interview simulation


def ask_chatgpt_for_interview(
        user_question,
        difficulty_level="medium",
        explanation_level="detailed",
        friendliness="friendly",
        api_key=""
):
    try:
        from langchain_community.chat_models import ChatOpenAI
        from langchain.schema import HumanMessage, SystemMessage
        from resources import config
        model_type = config.model_params['model_type']
        default_temperature = config.model_params['default_temperature']

        llm = ChatOpenAI(model=model_type, temperature=default_temperature, openai_api_key=api_key)

        system_msg_text = (
            f"You are an AI configured to simulate an interview and to be an helpful assistant for job interview.\n"
            f"The difficulty level of your questions should be in a difficulty that assumes the candidate is at a {difficulty_level} level.\n"
            f"Provide {explanation_level} explanations for your answers.\n"
            f"Maintain a {friendliness} tone throughout the interaction.\n"
            f"Make sure to answer only interview related questions. "
            f"Any other question should be responded with ```I am an AI interview assistant and cannot answer this question.```'.\n"
        )
        messages = [
            SystemMessage(content=system_msg_text),
            HumanMessage(content=user_question)
        ]

        response = llm.invoke(messages)
        print(response.content)
        return response.content

    except Exception as e:
        return f"An error occurred: {e}"


def ask_chatgpt_for_interview_dummy(user_question, difficulty_level="medium", explanation_level="detailed",
                              friendliness="friendly", api_key=''):
    response = "This is a dummy response from the assistant."
    return response



if __name__ == "__main__":
    from langchain_community.chat_models import ChatOpenAI
    from langchain.schema import HumanMessage, SystemMessage

    from dotenv import load_dotenv
    import os
    dotenv_path = os.path.join(os.path.dirname(__file__), "..\\resources\\.env")
    load_dotenv(dotenv_path)
    api_key = os.getenv("OPENAI_API_KEY")


    question = "Can you ask me a question related to data scientist interview at gaming startup?"
    difficulty = "hard"  # Set difficulty level (e.g., easy, medium, hard)
    explanation = "detailed"  # Set explanation level (e.g., brief, detailed, none)
    friendliness = "very friendly"  # Set friendliness level (e.g., friendly, neutral, formal)

    # Get a response from the configured assistant
    answer = ask_chatgpt_for_interview(
        user_question=question,
        difficulty_level=difficulty,
        explanation_level=explanation,
        friendliness=friendliness,
        api_key=api_key
    )
    print("Assistant's Response:", answer)
