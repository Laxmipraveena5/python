# Get input from the user
num = int(input("Enter a number: "))

# Initialize first two Fibonacci numbers
a, b = 0, 1

# Print the Fibonacci series up to 'num'
print("Fibonacci Series:", end=" ")

while a <= num:
    print(a, end=" ")
    a, b = b, a + b  # Update values

print()  # New line after printing series
