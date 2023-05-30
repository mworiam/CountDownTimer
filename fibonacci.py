'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.'''

def generate_fibonacci_numbers(count):
    fibonacci_numbers = []

    # Handle the first two numbers separately
    if count >= 1:
        fibonacci_numbers.append(0)
    if count >= 2:
        fibonacci_numbers.append(1)

    # Generate the remaining Fibonacci numbers
    for i in range(2, count):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

    return fibonacci_numbers

# Ask the user for the count of Fibonacci numbers
count = int(input("How many Fibonacci numbers do you want to generate? "))

# Generate and print the Fibonacci numbers
fibonacci_sequence = generate_fibonacci_numbers(count)
print("Fibonacci sequence:")
for number in fibonacci_sequence:
    print(number)
