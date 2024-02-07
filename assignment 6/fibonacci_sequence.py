
def generate_fibonacci(n):
    # Generate a sequence of n Fibonacci numbers
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    return sequence

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence:", fibonacci_sequence)

if __name__ == "__main__":
    main()
