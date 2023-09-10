def fibonacci_sequence(n):
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_sequence = [0, 1]  # Initialize with the first two terms
        while len(fib_sequence) <= n:
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)
        return fib_sequence[:-1] if n > 1 else [0]  # Exclude the last term if n > 1, else return [0]
