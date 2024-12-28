def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    Raises a ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if type(n) != int:
        raise TypeError("Factorial is only defined for integers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


