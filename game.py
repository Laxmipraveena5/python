import random  # Import random module

# Generate a random number between 1 and 50
random_number = random.randint(1, 50)

attempts = 5  # Set max attempts

print(" Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess the correct number between 1 and 50.")

while attempts > 0:
    try:
        guess = int(input("\nEnter your guess: "))  # User input
        
        if guess < 1 or guess > 50:
            print(" Please guess a number between 1 and 50!")
            continue  # Skip this attempt
        
        attempts -= 1  # Reduce attempts
        
        if guess == random_number:
            print(" YOU WON! The correct number was", random_number)
            break  # Exit the loop
        elif guess < random_number:
            print(" Too low! Try again.")
        else:
            print(" Too high! Try again.")
        
        if attempts > 0:
            print(f" Attempts left: {attempts}")
        else:
            print(f" YOU LOST! The correct number was {random_number}")
    
    except ValueError:
        print(" Invalid input! Please enter a number.")

