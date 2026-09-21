from config import client, MODEL, QUESTIONS


def ask_llm(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content


print("=== Day 1 Plain LLM Chatbot ===")

for i, question in enumerate(QUESTIONS, start=1):
    print(f"\nQuestion {i}: {question}")
    answer = ask_llm(question)
    print("Answer:", answer)