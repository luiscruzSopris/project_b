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


if __name__ == "__main__":
    main()
