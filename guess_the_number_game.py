from random import randint
print('''                                                    d8b                                                   d8b                      
                                                d8P ?88                                                   ?88                      
                                             d888888P88b                                                   88b                     
 d888b8b  ?88   d8P d8888b .d888b,.d888b,      ?88'  888888b  d8888b      88bd88b ?88   d8P  88bd8b,d88b   888888b    d8888b  88bd88b
d8P' ?88  d88   88 d8b_,dP ?8b,   ?8b,         88P   88P `?8bd8b_,dP      88P' ?8bd88   88   88P'`?8P'?8b  88P `?8b  d8b_,dP  88P'  `
88b  ,88b ?8(  d88 88b       `?8b   `?8b       88b  d88   88P88b         d88   88P?8(  d88  d88  d88  88P d88,  d88  88b     d88     
`?88P'`88b`?88P'?8b`?888P'`?888P'`?888P'       `?8bd88'   88b`?888P'    d88'   88b`?88P'?8bd88' d88'  88b d88'`?88P `?888P'd88'     
       )88                                                                                                                         
      ,88P                                                                                                                         
  `?8888P                                                                                                                          
''')
print("\nWelcome to the number guessing game!\n")
game_over = False

life = 5
NUMBER = randint(1, 100)

difficulty = input("Choose the difficulty. Type: 'easy' or 'hard'\n").lower()
if difficulty == "hard":
    life = 5
elif difficulty == "easy":
    life = 10
else:
    print("You didn't choose one of difficulty levels. You'll play hard level.\n")


def guess_function():
    global NUMBER
    global life
    global game_over

    while not game_over:
        attempts_amount = f"You have {life} attempts to guess the number"
        print(attempts_amount)
        guess = int(input("Guess a number: "))

        if guess != NUMBER:
            life -= 1
            if life == 0:
                print(f"\nYou ran out guesses. You loose! The number was: {NUMBER}")
                game_over = True
                return

        if guess == NUMBER:
            print(f"You got it, the answer was {NUMBER}")
            game_over = True
        elif guess > NUMBER:
            print(f"Too high\nGuess again")
            guess_function()
        elif guess < NUMBER:
            print(f"Too low\nGuess again")
            guess_function()


guess_function()
