
#functions
def make_statement(statement, decoration):
    """adds emoji/decoration to headings"""

    ends = decoration
    print(f"{ends} {statement} {ends}")

    return ""

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
print()
make_statement("Higher Lower game","↑↓↑")
print()


want_instructions = string_checker("do you want the instructions: ")

#display instructions if the user wants to see
if want_instructions == "yes":
    instructions()

print()
print("program continues")





