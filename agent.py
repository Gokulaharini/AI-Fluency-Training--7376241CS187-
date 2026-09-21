from config import client, MODEL
from tools import get_course_fee, calculator


SYSTEM_PROMPT = """
You are a helpful university fee assistant.

Rules:
1. Never guess course fees.
2. Always use get_course_fee when you need a course fee.
3. Use calculator for arithmetic.
4. You can answer general questions without tools when no fee data is needed.
5. Do not use tools unnecessarily.
"""


def ask_agent(question):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(6):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "get_course_fee",
                        "description": "Get the fee for a course.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "course_code": {
                                    "type": "string",
                                    "description": "Course code such as CS101, AI202, or DS303."
                                }
                            },
                            "required": ["course_code"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "calculator",
                        "description": "Calculate a basic arithmetic expression.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "expression": {
                                    "type": "string",
                                    "description": "Arithmetic expression to calculate."
                                }
                            },
                            "required": ["expression"]
                        }
                    }
                }
            ],
            tool_choice="auto"
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content

        messages.append(message)

        for tool_call in message.tool_calls:
            function_name = tool_call.function.name

            import json

            arguments = json.loads(tool_call.function.arguments)

            if function_name == "get_course_fee":
                result = get_course_fee(arguments["course_code"])

            elif function_name == "calculator":
                result = calculator(arguments["expression"])

            else:
                result = "Unknown tool."

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

    return "Agent stopped after reaching the maximum number of steps."


if __name__ == "__main__":
    print("=== Day 1 AI Agent ===")

    questions = [
        "What is the fee for AI202?",
        "What is the total fee for CS101 and AI202 after a 10% scholarship?",
        "Is DS303 more expensive than CS101, and by how much?",
        "Write a two-line welcome message for new AI students."
    ]

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question}")
        answer = ask_agent(question)
        print("Answer:", answer)