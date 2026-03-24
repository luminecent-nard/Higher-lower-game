import math
import random

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

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

def string_checker(question, valid_ans=('yes', 'no')):
    error = f"please enter a valid option from the following list: {valid_ans}"
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            #check if the user response is a word in the list
            if item == user_response:
                return item

            #check if user response is the same as
            #the first letter of an item in the list
            elif user_response == item[0]:
                return item
        #print error if user does not enter something that is valid
        print(error)
        print()

def make_statement(statement, decoration):
    """adds emoji/decoration to headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")

    return ""

def instructions():
    """prints instructions"""
    

    print("""
*** Instructions ***

to begin choose number of rounds and either customise 
the game parameters or go with the default game (where the 
secret number will be between 1 and 100).

choose how many rounds you would like to play (<enter> for infinite mode). 

your goal is to guess the secret number without running out of guesses.

good luck.

    """)
#main routine

#int game variables
end_game = ""
mode = "regular"
rounds_played = 0
already_guessed = []
warning = f"\nCareful, you only have one guess left!\n"
feedback = ""
guess = ""
warning_display = "false"

print()
make_statement("Higher Lower game","↑↓↑")
print()

#instructions
want_instructions = string_checker("Do you want the instructions: ")

#display instructions if the user wants to see
if want_instructions == "yes":
    instructions()

#ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds do you want to play (press <enter> for infinite): ",
                       low=1,exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

#get game parameters
low_num = int_check("Low number? ")
high_num = int_check("High number? ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

#display amount of guesses
print()
print(f"You get {guesses_allowed} guesses")

#game loop starts here
while rounds_played < num_rounds:

    #round headings (based on mode)
    if mode == "infinite":
        print()
        rounds_heading = make_statement(f"Round {rounds_played + 1} (infinite mode)","-")
    else:
        print()
        rounds_heading = make_statement(f"Round {rounds_played + 1} of {num_rounds}","-")

    #generate secret number
    secret = random.randint(low_num, high_num)

    # reset guesses used at the start of each round
    guesses_used = 0
    already_guessed = []

    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess the number
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check for exit code
        if guess == "xxx":
            print("See ya later!")
            # set up end game to use for outer loop
            end_game = "yes"
            break

        # check that the guess is not a duplicate
        if guess in already_guessed:
            print(f"you've already guessed {guess}. you've still used "
                  f"{guesses_used} / {guesses_allowed}")
            continue

        else:
            already_guessed.append(guess)

        # add 1 to the number of guesses used
        guesses_used += 1

        # compare users guess with secret number
        if guess == secret:
            if guesses_used == 1:
                feedback = "Pure skill"
            # variable responses for different scenarios
            elif guesses_used == guesses_allowed:
                feedback = f"phew, you nearly ran out of all {guesses_allowed} guesses"

            else:
                feedback = f"You got it in {guesses_used} guesses"

            print()
            print(feedback)
            break

        # warns the player if they have only one guess left
        if guesses_used == guesses_allowed - 1:
            warning_display = "true"

        # tells the user to guess higher
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Higher! \n"
                        f"you've used {guesses_used} / {guesses_allowed}")

        # tells the user that they need to guess lower
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Lower! \n"
                        f"you've used {guesses_used} / {guesses_allowed}")

        # out of guesses
        else:
            feedback = ("Out of guesses \n"
                        "better luck next time!")

        # display feedback
        print()
        print(feedback)
        if warning_display == "true":
            print(warning)
            warning_display = "false"
        print()
    #if users are in infinite mode increase number of rounds

    #round progression
    rounds_played += 1

    #make infinite infinite
    if mode == "infinite":
        num_rounds += 1

    if end_game == "yes":
        break

#game loop ends here
print("end of game")
#game history / stats