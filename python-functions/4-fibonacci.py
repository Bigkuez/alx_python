def fibonacci_sequence(n):
    if n <= 0:
        return []  # Return an empty list for non-positive n
    elif n == 1:
        return [0]  # Special case for n = 1, return [0]
    else:
        fib_sequence = [0, 1]  # Initialize with the first two terms
        while len(fib_sequence) < n:
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)
        return fib_sequence
