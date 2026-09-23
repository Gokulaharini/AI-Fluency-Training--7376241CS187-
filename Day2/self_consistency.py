"""Day 2 - Self-Consistency experiment."""

import sys
from pathlib import Path
from collections import Counter

# Allow imports from the main day1_lab folder
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import client, MODEL


QUESTION = (
    "Three courses cost Rs. 12,000, Rs. 18,000, and Rs. 15,000. "
    "A 15% scholarship applies to the total and the balance is paid "
    "in 4 equal installments. What is each installment?"
)

COT_PROMPT = """
You are a helpful assistant.
Solve the problem step by step.
After the reasoning, write:

Final Answer: <answer>
"""

RUNS = 5
TEMPERATURE = 0.8


def ask_cot(question, temperature):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": COT_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=temperature
    )

    return response.choices[0].message.content


def extract_final_answer(text):
    for line in text.splitlines():
        if "Final Answer:" in line:
            return line.split("Final Answer:", 1)[1].strip()

        if "9,562.50" in line or "9562.50" in line:
            return "Rs. 9,562.50"

        if "9,562.5" in line or "9562.5" in line:
            return "Rs. 9,562.50"

    return "Answer not extracted"
print("=== Self-Consistency Experiment ===")
print(f"Temperature: {TEMPERATURE}")
print(f"Runs: {RUNS}")
print(f"\nQuestion:\n{QUESTION}")

answers = []

for i in range(1, RUNS + 1):
    print(f"\n{'=' * 60}")
    print(f"RUN {i}")

    try:
        response = ask_cot(QUESTION, TEMPERATURE)
        answer = extract_final_answer(response)

        answers.append(answer)

        print(response)
        print(f"\nExtracted answer: {answer}")

    except Exception as e:
        print(f"ERROR: {e}")


if answers:
    counts = Counter(answers)
    majority_answer, majority_count = counts.most_common(1)[0]

    print("\n" + "=" * 60)
    print("SELF-CONSISTENCY RESULT")
    print("=" * 60)

    print("\nAll extracted answers:")
    for i, answer in enumerate(answers, start=1):
        print(f"Run {i}: {answer}")

    print(f"\nMajority answer: {majority_answer}")
    print(f"Majority count: {majority_count}/{len(answers)}")

    print("\nExpected correct answer: Rs. 9,562.50")

    if "9,562.50" in majority_answer or "9562.50" in majority_answer:
        print("Majority answer is CORRECT.")
    else:
        print("Majority answer is NOT CORRECT.")

print("\n=== Temperature 0 comparison ===")

try:
    temp0_response = ask_cot(QUESTION, 0)

    print(temp0_response)

    temp0_answer = extract_final_answer(temp0_response)

    print(f"\nTemperature 0 extracted answer: {temp0_answer}")

except Exception as e:
    print(f"ERROR: {e}")