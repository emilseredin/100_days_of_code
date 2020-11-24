import os


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def add(a: float, b: float) -> float:
    """
        Return the sum of two numbers
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
        Return the difference between the two numbers
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
        Return the product of two numbers
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
        Return the ratio of two numbers 
    """
    return a / b


def do_calculation(num1: float, num2: float, op: str) -> float:
    """
        Return the result of performing the operation on two numbers
    """
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    if op not in operations:
        raise ValueError("Unsupported operation.")
    return operations[op](a=num1, b=num2)


def main():
    keep_running = True
    while keep_running:
        num1 = float(input("What's the first number? ").strip())
        continue_calculating = True
        while continue_calculating:
            print("+\n-\n*\n/")
            operation = input(
                "Pick an operation from the line above: ").strip()
            num2 = float(input("What's the next number? ").strip())
            result = do_calculation(num1, num2, operation)
            print("{} {} {} = {}".format(num1, operation, num2, result))
            answer = input(
                "Type 'c' to continue calculating with {}, 'n' to start a new calculation, or 'q' to exit calculator: ".format(result))
            if answer == 'c':
                num1 = result
            elif answer == 'n':
                continue_calculating = False
                clear() 
            else:
                continue_calculating = False
                keep_running = False


if __name__ == "__main__":
    main()
