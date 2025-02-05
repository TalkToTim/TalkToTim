# Function to configure and interact with ChatGPT for an interview simulation


def ask_chatgpt_for_interview(question, difficulty_level="medium", explanation_level="detailed",
                              friendliness="friendly"):
    try:
        # System message to configure the assistant's behavior for an interview
        system_prompt = (
            f"You are an AI configured to simulate an interview and to be an helpful assistant for job interview. "
            f"The difficulty level of your questions should be in a difficulty that assumes the candidate is at a {difficulty_level} level. "
            f"Provide {explanation_level} explanations for your answers. "
            f"Maintain a {friendliness} tone throughout the interaction."
        )

        # Make a request to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the model to use
            messages=[
                {"role": "system", "content": system_prompt},  # Configure the system behavior
                {"role": "user", "content": question},  # User's question
            ],
            temperature=0.5,  # Controls the creativity of the response
        )

        # Extract the assistant's reply from the API response
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        # Handle any errors that occur
        return f"An error occurred: {e}"


def ask_chatgpt_for_interview_dummy(question, difficulty_level="medium", explanation_level="detailed",
                              friendliness="friendly"):
    response = "This is a dummy response from the assistant."
    return response



if __name__ == "__main__":
    from openai import OpenAI

    client = OpenAI(
        api_key=""
    )

    question = "Can you ask me a question related to data scientist interview at gaming startup?"
    difficulty = "hard"  # Set difficulty level (e.g., easy, medium, hard)
    explanation = "detailed"  # Set explanation level (e.g., brief, detailed, none)
    friendliness = "very friendly"  # Set friendliness level (e.g., friendly, neutral, formal)

    # Get a response from the configured assistant
    answer = ask_chatgpt_for_interview(question, difficulty_level=difficulty, explanation_level=explanation, friendliness=friendliness)
    print("Assistant's Response:", answer)
