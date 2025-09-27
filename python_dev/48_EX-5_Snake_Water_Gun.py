import random
while True:
    choices = ["Snake", "Water", "Gun"]
    bot = random.choice(choices)

    Player = input("Enter your choice (Snake, Water, Gun): ").capitalize()

    if Player == bot:
        print("It's a Draw!")

    elif Player == "Snake":
        if bot == "Water":
            print("You win! Snake drinks Water.")
        elif bot == "Gun":
            print("You lose! Gun kills Snake")

    elif Player == "Water":
        if bot == "Gun":
            print("You win! Water douses Gun.")
        elif bot == "Snake":
            print("You lose! Snake drinks Water")

    elif Player == "Gun":
        if bot == "Snake":
            print("You win! Gun kills Snake")
        elif bot == "Water":
            print("You lose! Water douses Gun")

    else:
        print("Invalid input!")
        continue

    print(f"Computer chose: {bot}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break