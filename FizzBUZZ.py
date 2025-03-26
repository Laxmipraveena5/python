# FizzBuzz Program from 1 to 100

for num in range(1, 101):  # Loop from 1 to 100
    if num % 15 == 0:  # Divisible by 15 (both 3 and 5)
        print("FizzBuzz")
    elif num % 3 == 0:  # Divisible by 3
        print("Fizz")
    elif num % 5 == 0:  # Divisible by 5
        print("Buzz")
    else:
        print(num)  # Print the number if not divisible by 3 or 5
