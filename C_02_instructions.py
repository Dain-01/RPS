# functions go here

def  yes_no(question):

    # check user response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response =input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Roll the dice and try to win!
     """)



# Main routine


want_instructions = yes_no("Do you want instructions vro? ")

# Display the instructions if the user wants to see them . . .

if want_instructions == "yes":
    instructions()

print()
print("program continues")