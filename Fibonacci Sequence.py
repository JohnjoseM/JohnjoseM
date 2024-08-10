def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
n = 10
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_sequence(n)}")
