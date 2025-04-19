# Sample Python code for demonstration

def hello_world() -> None:
    """
    Prints a hello world message to the console.
    """
    print("Hello, World!")

def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    Parameters:
    a (int): The first number to add
    b (int): The second number to add

    Returns:
    int: The result of adding a and b
    """
    return a + b

if __name__ == '__main__':
    hello_world()
    result = add(5, 7)
    print(f"5 + 7 = {result}")