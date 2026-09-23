"""Day 2 - Direct Prompting vs Chain-of-Thought comparison."""

import sys
from pathlib import Path

# Allow imports from the main day1_lab folder
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import client, MODEL


QUESTIONS = [
    (
        "Three courses cost Rs. 12,000, Rs. 18,000, and Rs. 15,000. "
        "A 15% scholarship applies to the total and the balance is paid "
        "in 4 equal installments. What is each installment?",
        "Rs. 9,562.50"
    ),
    (
        "There are 18 computers. Each computer has 2 students in the "
        "morning and 3 students in the afternoon. How many student "
        "sittings are there?",
        "90"
    ),
    (
        "Ravi is taller than Kumar, Kumar is taller than Arun, and "
        "Priya is shorter than Arun. Who is tallest and who is shortest?",
        "Ravi is tallest and Priya is shortest"
    )
]


DIRECT_PROMPT = """
You are a helpful assistant.
Give only the final answer.
Do not explain.
"""


COT_PROMPT = """
You are a helpful assistant.
Solve the problem step by step.
Number each step and show the calculation or reasoning in that step.
After the steps, write the last line exactly as:

Final Answer: <answer>
"""


def ask_llm(prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


print("=== Direct Prompting vs Chain-of-Thought ===")

for i, (question, expected) in enumerate(QUESTIONS, start=1):

    print(f"\n{'=' * 60}")
    print(f"QUESTION {i}")
    print(question)
    print(f"Expected answer: {expected}")

    print("\n--- DIRECT PROMPT ---")

    try:
        direct_answer = ask_llm(DIRECT_PROMPT, question)
        print(direct_answer)
    except Exception as e:
        direct_answer = f"ERROR: {e}"
        print(direct_answer)

    print("\n--- CHAIN-OF-THOUGHT PROMPT ---")

    try:
        cot_answer = ask_llm(COT_PROMPT, question)
        print(cot_answer)
    except Exception as e:
        cot_answer = f"ERROR: {e}"
        print(cot_answer)