import random
secret_number = random.randint(1, 100)
attempts = 0
print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("I have selected a number from 1 to 100.")
print("Can you guess it?")
print()

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")
    elif guess > secret_number:
        print("Too high! Try a smaller number.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

print("Thanks for playing!")