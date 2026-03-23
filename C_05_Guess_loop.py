#checks for int with optional upper and lower
#limits and an optional exit code for infinite mode
#/ quitting the game
def int_check(question, low=None, high=None, exit_code=None):

    #if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    #if the number needs to be more than an integer
    #(rounds, high number)
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f"more than / equal to {low}")

    #if the number needs to be below low and high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        #check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response  = int(response)

            #check the interger is not too low
            if low is not None and response < low:
                print(error)

            #check response is more than low
            elif high is not None and response > high:
                print(error)

            #if response is valid return it
            else:
                return response

        except ValueError:
            print(error)

#guessing loop

#replace number with random number between high and low values
secret = 7

#parameters that already exist in base game
low_num = 0
high_num = 10
guesses_allowed = 5

#set guesses to 0 at the start of each round
guesses_used = 0
already_guessed = []
warning = f"\nCareful, you only have one guess left!\n"

feedback = ""
guess = ""
warning_display = "false"
while guess != secret and guesses_used < guesses_allowed:

    #ask the user to guess the number
    guess = int_check("Guess: ", low_num, high_num, "xxx")

    #check for exit code
    if guess == "xxx":
        print("See ya later!")
        #set up end game to use for outer loop
        end_game = "yes"
        break

    #check that the guess is not a duplicate
    if guess in already_guessed:
        print(f"you've already guessed {guess}. you've still used "
              f"{guesses_used} / {guesses_allowed}")
        continue

    else:
        already_guessed.append(guess)

    #add 1 to the number of guesses used
    guesses_used += 1

    #compare users guess with secret number
    if guess == secret:
        if guesses_used == 1:
            feedback = "Pure skill"
        #variable responses for different scenarios
        elif guesses_used == guesses_allowed:
            feedback = f"lucky, you used all {guesses_allowed} guesses"

        else:
            feedback = f"You got it in {guesses_used} guesses"

        print()
        print(feedback)
        break

    #warns the player if they have only one guess left
    if guesses_used == guesses_allowed - 1:
        warning_display = "true"

    #tells the user to guess higher
    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Higher! "
                    f"you've used {guesses_used} / {guesses_allowed}")

    #tells the user that they need to guess lower
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Lower! "
                    f"you've used {guesses_used} / {guesses_allowed}")

    #out of guesses
    else:
        feedback = ("Out of guesses \n"
                    "better luck next time!")

    #display feedback
    print()
    print(feedback)
    if warning_display == "true":
        print(warning)
        warning_display = "false"
