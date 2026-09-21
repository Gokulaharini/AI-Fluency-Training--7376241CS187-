import ast
import operator

from config import COURSE_FEES


def get_course_fee(course_code):
    course_code = course_code.upper()

    if course_code not in COURSE_FEES:
        return f"Course {course_code} not found."

    return COURSE_FEES[course_code]


def calculator(expression):
    """
    Safely calculate basic arithmetic expressions.
    """

    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numbers are allowed.")

        if isinstance(node, ast.BinOp):
            operator_function = allowed_operators.get(type(node.op))

            if operator_function is None:
                raise ValueError("Operator not allowed.")

            left = evaluate(node.left)
            right = evaluate(node.right)

            return operator_function(left, right)

        raise ValueError("Invalid expression.")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree)


# Test the tools
if __name__ == "__main__":
    print("=== Testing Tools ===")

    print("AI202 fee:", get_course_fee("ai202"))

    print(
        "Scholarship calculation:",
        calculator("(12000 + 18000) * 0.9")
    )

    print(
        "Fee difference:",
        calculator("15000 - 12000")
    )