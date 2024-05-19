   """
    Calculates the factorial of a non-negative integer.
    
    Args:
    n (int): Non-negative integer
    
    Returns:
    int: Factorial of n
    """
def factorial(n):
    # Base case: If n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: Multiply n by factorial of n-1
        return n * factorial(n - 1)

# Example usage
result = factorial(5)
print(result)  # Output: 120
