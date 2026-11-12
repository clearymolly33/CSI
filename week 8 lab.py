import random
#Part 1
def secret_number():
    return random.randint(1, 20)
print("The secret number is:", secret_number())
#Part 2
def guessing_game():
    secret = secret_number()
    attempts = 0
    while attempts < 5:
        guess = int(input("Guess a number between 1 and 20: "))
        attempts += 1
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            return
    print("Out of attempts! The secret number was:", secret)
#Part 3
def quick_quiz():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print("What is", num1, "+", num2, "?")
    answer = int(input("Answer: "))
    if answer == num1 + num2:
        print("Correct! You earned 1 point.")
    else:
        print("Incorrect.")
#Part 4
def main():
    choice = ""
    while choice != "3":
        print("\n===== PYTHON CHALLENGE GAME =====")
        print("1. Play the guessing game")
        print("2. Take a quick math quiz")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            guessing_game()
        elif choice == "2":
            quick_quiz()
        elif choice == "3":
            print("Goodbye!")
        else:
            print("Invalid option. Try again.")
main()