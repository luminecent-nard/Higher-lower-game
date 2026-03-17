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

#main routine

#round checker
# rounds = "test"
# while rounds != "":
#     rounds = int_check("Rounds <enter> for infinite:", low=1, exit_code="")
#     print(f"you asked for {rounds}")

#low number
# low_num = int_check("low number? ")
# print(f"you chose a low number of {low_num}")

#high number
# high_num = int_check("high number? ", low=1)
# print(f"you chose a high number of {high_num}")

#check user guesses
guess = ""
while guess != "xxx":
    guess = int_check("guess: ", low=0, high=10, exit_code="xxx")
    print(f"you guessed {guess}")
    print()