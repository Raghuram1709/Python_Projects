import random

def play_game():

    print("🎲 Welcome to Number Guessing Game 🎲")
    
    print("\nChoose Difficulty level")
    print("1. Easy - 10 chances")
    print("2. Medium - 7 chances")
    print("3. Hard - 5 chances")
    print("4. Impossible - 3 chances")
    
    max_range = int(input("Select maximun range:"))

    difficulty = int(input("Enter 1 or 2 or 3 or.. what ever you want: "))

    difficulty_map = {1: 10, 2: 7, 3: 5, 4: 3}
    

    invalid_difficulty_lines = [
        "😂 Invalid difficulty? Bold move… enjoy 7 pity chances.",
        "😏 Ohhh, breaking the rules? Cute. Anyway, here’s 7 chances.",
        "🤣 That’s not even a difficulty. I’ll be nice though—7 chances for you.",
        "Bruh, you think you’re clever? Nah. 7 chances, take it or leave it.",
        "🤡 Invalid choice detected. Congratulations, you just unlocked… 7 chances."
    ]

    if difficulty in difficulty_map:
        chances = difficulty_map[difficulty]
        
        if max_range < chances:
            print(" 😏 Nice try... range is too small compared to chances. Doubling it for you!")
            max_range = chances * 2
        elif max_range == chances:
            print("😏 Nice try... range is equal to chances. +5 range for you")
            max_range = chances + 5
    else:
        print(random.choice(invalid_difficulty_lines))
        chances = 7

    sys_num = random.randrange(max_range)

    correct_lines = [
        "🎯 Right on the money! Dead shot!",
        "🔥 Sniped it! You actually got it!",
        "👏 Respect, you nailed it!",
        "Damn… didn’t think you’d get it, but here we are 😏",
        "You got it… finally. Miracles *do* happen."
    ]

    too_low_lines = [
        "😂 Too low… even my GPA is higher than that.",
        "Bruh, that’s so low it’s underground 🌋",
        "Not even close, you’re digging a tunnel 😭",
        "That guess was shorter than a TikTok attention span.",
        "Lowball of the century… try again."
    ]

    too_high_lines = [
        "🤣 Too high! You trying to reach Mars?",
        "Relax bro, we’re not guessing Elon’s net worth 🚀",
        "That number overshot harder than my life goals.",
        "Way too high—NASA just called about your guess 🌌",
        "Bro chill… it’s a number, not Mount Everest."
    ]

    wasted_lines = [
        "❌ That’s not even a number. Bold strategy, Cotton.",
        "Lmao… you typed that? That’s one chance gone 😂",
        "Bro… you had ONE job. Enter a number.",
        "Epic fail. Guess wasted.",
        "Your keyboard must be trolling you 💀"
    ]

    gameover_lines = [
        "Game Over 😭 The number was {sys_num}. Better luck next time!",
        "😏 Out of chances. The number was {sys_num}. You tried… kinda.",
        "💀 Bruh, it was {sys_num}. Don’t cry now.",
        "You lost. The number was {sys_num}. Should’ve asked Siri.",
        "Ouch. {sys_num} was the answer. Brutal ending, my friend."
    ]

    
    while chances > 0:
        print(f"\nYou Have {chances} chances to guess...")
        try:
            num = int(input("Guess the number:"))
            if num == sys_num:
                print(random.choice(correct_lines))
                break
            elif num < sys_num:
                print(random.choice(too_low_lines))
            else:
                print(random.choice(too_high_lines))

        except ValueError:
            print(random.choice(wasted_lines))  
        chances = chances - 1
    if chances == 0:
        print(random.choice(gameover_lines).format(sys_num = sys_num))
    
while True:
    play_game()
    choice = input("Do you to play again? say(yes/no): ").lower()
    if choice == "no" or choice == "n":
        print("Okay! Thanks for playing ✌️")
        break

