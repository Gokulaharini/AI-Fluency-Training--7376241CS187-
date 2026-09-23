"""Day 2 - ReAct trace using the required tools."""

import sys
from pathlib import Path

# Allow imports from the main day1_lab folder
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import get_course_fee, calculator


print("QUESTION:")
print(
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)

print("\n--- ReAct Trace ---")

print("\nThought 1:")
print("I need the fees for CS101, AI202, and DS303.")

print("\nAction 1:")
print("get_course_fee('CS101')")

cs101 = get_course_fee("CS101")

print("\nObservation 1:")
print(f"CS101 fee = Rs. {cs101}")

print("\nAction 2:")
print("get_course_fee('AI202')")

ai202 = get_course_fee("AI202")

print("\nObservation 2:")
print(f"AI202 fee = Rs. {ai202}")

print("\nAction 3:")
print("get_course_fee('DS303')")

ds303 = get_course_fee("DS303")

print("\nObservation 3:")
print(f"DS303 fee = Rs. {ds303}")

print("\nThought 2:")
print("I now calculate the final fee for both options.")

print("\nAction 4:")
print(f"calculator('({cs101} + {ai202}) * 0.90')")

option1 = calculator(f"({cs101} + {ai202}) * 0.90")

print("\nObservation 4:")
print(f"Option 1 final fee = Rs. {option1}")

print("\nAction 5:")
print(f"calculator('({cs101} + {ai202} + {ds303}) * 0.75')")

option2 = calculator(f"({cs101} + {ai202} + {ds303}) * 0.75")

print("\nObservation 5:")
print(f"Option 2 final fee = Rs. {option2}")

print("\nAction 6:")
print(f"calculator('{option2} - {option1}')")

difference = calculator(f"{option2} - {option1}")

print("\nObservation 6:")
print(f"Difference = Rs. {difference}")

print("\nThought 3:")
print("The first option is cheaper.")

print("\nFINAL ANSWER:")
print(
    f"CS101 + AI202 with a 10% scholarship is cheaper "
    f"by Rs. {difference}."
)