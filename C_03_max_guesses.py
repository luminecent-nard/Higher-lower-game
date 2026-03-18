import math

#calculate number of guesses allowed
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

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

#main routine
#imput low guesses
while True:
    low_number = int_check("low num ")
    high_number = int_check("high num ", low=low_number)

    actual = calc_guesses(low_number, high_number)
    print(f"max guesses {actual}")
