"""
Session 4 - Task 3
A custom calculator tool (add, subtract, multiply, divide) defined as a
function and registered using LangChain's Tool class.
"""

from langchain.tools import Tool


def calculator(expression: str) -> str:
    """
    Parses a simple expression like 'add 4 5', 'subtract 10 3',
    'multiply 6 7', or 'divide 20 4' and returns the result.
    """
    try:
        parts = expression.strip().lower().split()
        op, a, b = parts[0], float(parts[1]), float(parts[2])

        if op == "add":
            result = a + b
        elif op == "subtract":
            result = a - b
        elif op == "multiply":
            result = a * b
        elif op == "divide":
            if b == 0:
                return "Error: cannot divide by zero."
            result = a / b
        else:
            return f"Unknown operation '{op}'. Use add, subtract, multiply, or divide."

        return str(result)
    except (IndexError, ValueError):
        return "Error: expected format is '<operation> <num1> <num2>', e.g. 'multiply 6 7'."


calculator_tool = Tool(
    name="Calculator",
    func=calculator,
    description=(
        "Use this for arithmetic. Input format: '<operation> <num1> <num2>', "
        "e.g. 'add 4 5', 'multiply 6 7', 'divide 20 4'."
    ),
)

if __name__ == "__main__":
    print(calculator("multiply 6 7"))
    print(calculator("divide 20 4"))
    print(calculator("divide 5 0"))
