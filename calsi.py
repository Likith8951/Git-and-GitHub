def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main():
    print("Calculator (enter q to quit)")

    while True:
        expression = input("Enter a calculation (e.g. 2 + 3): ").strip()
        if expression.lower() == "q":
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Please enter a calculation in the form: number operator number")
            continue

        try:
            first = float(parts[0])
            second = float(parts[2])
            result = calculate(first, parts[1], second)
        except ValueError as error:
            print(f"Invalid calculation: {error}")
            continue
        except ZeroDivisionError as error:
            print(error)
            continue

        print(f"Result: {result:g}\n")


if __name__ == "__main__":
    main()
    