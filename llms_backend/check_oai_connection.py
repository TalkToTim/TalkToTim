from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


def check_connection():
    response = ""
    try:
        # Initialize the ChatOpenAI model using LangChain
        chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

        human_message = HumanMessage(content="What is the capital of France?")
        response = chat_model([human_message])

        print("Test successful! Response from model:", response)

    except Exception as e:
        print(f"Connection failed. Error: {e}")

    return response

if __name__ == "__main__":

    from dotenv import load_dotenv
    import os
    dotenv_path = os.path.join(os.path.dirname(__file__), "..\\resources\\.env")

    load_dotenv(dotenv_path)
    api_key = os.getenv("OPENAI_API_KEY")
    response = check_connection()
