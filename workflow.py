from config import COURSE_FEES, QUESTIONS


def workflow_answer(question):
    question_lower = question.lower()

    # Question 1
    if "fee for ai202" in question_lower:
        return f"The fee for AI202 is Rs. {COURSE_FEES['AI202']}."

    # Question 2
    elif "cs101" in question_lower and "ai202" in question_lower and "10%" in question_lower:
        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        discounted_total = total * 0.90
        return f"The total after a 10% scholarship is Rs. {discounted_total:.0f}."

    # Question 3
    elif "ds303" in question_lower and "cs101" in question_lower:
        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]

        if difference > 0:
            return f"Yes. DS303 is Rs. {difference} more expensive than CS101."
        elif difference < 0:
            return f"No. DS303 is Rs. {-difference} cheaper than CS101."
        else:
            return "No. Both courses have the same fee."

    # Question 4
    else:
        return "I don't have a rule for this question."


print("=== Day 1 Rule-Based Workflow ===")

for i, question in enumerate(QUESTIONS, start=1):
    print(f"\nQuestion {i}: {question}")
    answer = workflow_answer(question)
    print("Answer:", answer)