def add(a, b):
    """Add two numbers and return their sum.
    
    Args:
        a: First numeric value.
        b: Second numeric value.
    
    Returns:
        The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    num1 = 5
    num2 = 3
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
    
    num3 = 10.5
    num4 = 2.5
    result2 = add(num3, num4)
    print(f"The sum of {num3} and {num4} is: {result2}")
