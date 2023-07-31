def my_factorial_for(n):
    """
    Calculates the factorial of n with a for loop.
    Args:
        n (int): upper bound for factorial

    Returns:
        n! (int): the factorial of n

    Raises:
        Negative value error if n < 0.
    """

    if n < 0:
        return -1
    elif n == 0:
        return 1

    n_factorial = 1
    for iterator in range(1, n + 1):
        # [1,2,3,...,n]
        n_factorial *= iterator

    return n_factorial


def my_factorial_while(n):
    """
    Calculates the factorial of n with a while loop.
    Args:
        n (int): upper bound for factorial

    Returns:
        n! (int): the factorial of n

    Raises:
        Negative value error if n < 0.
    """
    if n < 0:
        return -1

    n_factorial = 1  # The answer we are returning
    iterator = 0
    while iterator < n:  # [0,1,2,..., n-1]
        iterator += 1
        # [1,2,3,...,n]
        n_factorial *= iterator

    return n_factorial


def MyFactorial(n):
    """
    Returns a formatted string of factorial n.
    Args:
        n (int): integer to be used for determining the factorial

    Returns:
        result (string): formatted string representing the factorial and how it was calculated.
    """
    if n % 2 == 0:
        result = f"FORLOOP  : Factorial of {n} is {my_factorial_for(n)}"
    else:
        result = f"WHILELOOP: Factorial of {n} is {my_factorial_while(n)}"
    return result


# Very simple tests
for iterator in range(-10, 51):
    print(MyFactorial(iterator))
