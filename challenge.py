from config import COURSE_FEES

budget = 30000

print("=== Day 1 Challenge ===")
print(f"Budget: Rs. {budget}")

courses = list(COURSE_FEES.keys())

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        course1 = courses[i]
        course2 = courses[j]

        total = COURSE_FEES[course1] + COURSE_FEES[course2]

        if total <= budget:
            print(
                f"{course1} + {course2} = Rs. {total}"
            )