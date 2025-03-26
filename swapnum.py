# Get input from the user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swap using a third variable
temp = a
a = b
b = temp

# Display swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
