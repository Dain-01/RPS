# Check that users have entered a valid
# option based on a list

def string_checker (question, valid_ans=('yes', 'no')):
    """Uses string checker to check"""

    error = f"Please enter a valid option from the following list:{valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

To begin, choose the number of rounds (or play infinite mode)

Then play against the computer. You need to put R (rock) P (paper) or S (scissors). 

The rules are as follows:
- Paper beats Rock
- Rock beats scissors 
- Scissors beats Paper
""")


# Check that users have entered an int more than 0 (allows <enter>)

def int_check(question):
    while True:
        error = "please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:

            response = int(to_check)

            # Check if the number is more then or equal to 1
            if response < 1:
                print(error)

            else:
               return response

        except ValueError:
            print(error)



# Main Routine Starts here

# Initialize game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("🙈🙉🙊 Rock / Paper / Scissors Game 🙈🙉🙊")
print()

#asks user if they want instructions
want_instructions = string_checker("Do you want instructions vro? ")

# Display the instructions if the user wants to see them . . .

if want_instructions == "yes":
    instructions()

# Asks user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        round_heading = f"\n(❁´◡`❁) Round {rounds_played + 1} (Infinite Mode) (❁´◡`❁)"
    else:
        round_heading = f"\n (●'◡'●) Round {rounds_played + 1} of {num_rounds} (●'◡'●)"

    print(round_heading)
    print()

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # if user choice is exit code, break loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / Statistics area
