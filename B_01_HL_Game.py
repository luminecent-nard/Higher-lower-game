# Check that users have entered a valid
# option based on a list
def integer_checker(question):
    """checks that the integer is more than 13"""


    while True:
        error = "Please enter an integer more than 1."
        #check for infinite mode
        to_check = input(question)

        if to_check == "":
            return "infinite"
        #round detector thingy
        try:

            response = int(to_check)

            #checks that the number is more than 1
            if response < 1:
                print(error)

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
mode = "regular"
rounds_played = 0

print()
make_statement("Higher Lower game","↑↓↑")
print()

#instructions
want_instructions = string_checker("do you want the instructions: ")

#display instructions if the user wants to see
if want_instructions == "yes":
    instructions()

print()
print("program continues")
#ask user for number of rounds / infinite mode
num_rounds = integer_checker("how many rounds do you want to play (press <enter> for infinite): ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#game loop starts here
while rounds_played < num_rounds:

    #round headings (based on mode)
    if mode == "infinite":
        rounds_heading = make_statement(f"Round {rounds_played + 1} (infinite mode)","-")
    else:
        rounds_heading = make_statement(f"Round {rounds_played + 1} of {num_rounds}","-")

    #get user choice
    user_choice = input("choose: ").lower()

    #exit code
    if user_choice == "xxx":
        break

    rounds_played += 1

    #if users are in infinite mode increase number of rounds
    if mode == "infinite":
        num_rounds += 1

#game loop ends here

#game history / stats