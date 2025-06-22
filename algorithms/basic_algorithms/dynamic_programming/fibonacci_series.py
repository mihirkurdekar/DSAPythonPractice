'''
Fibonacci Series: Calculate the nth Fibonacci number using dynamic programming.
'''

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    :param n: The position in the Fibonacci sequence (0-indexed).
    :return: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Create an array to store Fibonacci numbers up to n
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1
    
    # Fill the array using the previous two Fibonacci numbers
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    :param n: The position in the Fibonacci sequence (0-indexed).
    :return: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
if __name__ == "__main__":
    n = 10  # Change this value to compute a different Fibonacci number
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    # Output: The 10th Fibonacci number is: 55

    print(f"The {n}th Fibonacci number (recursive) is: {fibonacci_recursive(n)}")
    # Output: The 10th Fibonacci number (recursive) is: 55