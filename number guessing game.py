# Reverse Number Guessing Game (User Feedback Based)

# Step 1: Start request
start = input("Do you want to start the game? (yes/no): ").lower()
if start != "yes":
    print("Game exited.")
    exit()

# Step 2: Rules using tuple
rules = (
    "Think of a number between 1 and 100",
    "Computer will guess the number",
    "Reply with: low, high, or correct"
)

print("\nGame Rules:")
for rule in rules:
    print("-", rule)

input("\nThink of a number and press Enter to continue...")

# Step 3: Data structures
guess_list = []     # list to store guesses
attempts = 0

low = 1
high = 100

# Step 4: Guessing loop
while True:
    if low > high:
        print("\n❌ Inconsistent answers detected. Game stopped.")
        break

    computer_guess = (low + high) // 2  # mathematical expression
    attempts += 1

    guess_list.append(computer_guess)

    print(f"\nComputer guesses: {computer_guess}")
    feedback = input("Is it low, high, or correct? ").lower()

    if feedback == "low":
        low = computer_guess + 1
    elif feedback == "high":
        high = computer_guess - 1
    elif feedback == "correct":
        print("\n🏆 COMPUTER WON! Guess is correct.")
        break
    else:
        print("Invalid input. Please type low, high, or correct.")

# Step 5: Store result using dictionary
game_result = {
    "Total Attempts": attempts,
    "Guesses (List)": guess_list,
}

# Step 6: Final result
print("\n--- Game Summary ---")
for key, value in game_result.items():
    print(key, ":", value)