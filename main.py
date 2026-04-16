"""
main.py - A simple example program for Git practice.

This module demonstrates basic Python functionality and serves as a
starting point for experimenting with Git workflows.
"""


def greet(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def main() -> None:
    """Entry point of the program."""
    print(greet())
    print(greet("Git"))
    print(f"2 + 3 = {add(2, 3)}")


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

if __name__ == "__main__":
    main()
