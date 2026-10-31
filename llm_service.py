from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:31415/v1",
    api_key="freellmapi-450e5c5ad6ea88d94490d0fe22a2e35c7be8375dd95569be"
)

def ask_ai(question:str)->str:
    response = client.chat.completions.create(
        model = "auto",
        messages = [
            {
                "role":"system",
                "content": (
                    "You are helpful voice assistent."
                    "Give short, conversational asnwers."
                    "Answer the user's actual question."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content or "Sorry, I couldn't generate a response"

if __name__ == "__main__":
    print(ask_ai("what is artificial intelligence?"))