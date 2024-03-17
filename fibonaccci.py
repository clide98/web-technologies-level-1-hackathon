# Fibonacci Sequence Program
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n]

def main():
    n = int(input("Enter the number of terms for Fibonacci sequence: "))
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci Sequence up to term", n, ":", fibonacci_sequence)

if __name__ == "__main__":
    main()