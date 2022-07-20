def year_input():

    print("Would you like to sort by Year? (y/n)")
    yes_no = input()

    if yes_no.lower() == "y":
        yn = True
        return yn

    elif yes_no.lower() == "n":
        yn = False
        return yn

    else:
        print("Please make a valid input (Please enter \"y\" for YES or \"n\" for NO)")
        year_input()


def month_input():
    print("Would you like to sort by Month? (y/n)")
    yes_no = input()

    if yes_no.lower() == "y":
        yn = True
        return yn

    elif yes_no.lower() == "n":
        yn = False
        return yn

    else:
        print("Please make a valid input (Please enter \"y\" for YES or \"n\" for NO)")
        month_input()


def day_input():
    print("Would you like to sort by Day? (y/n)")
    yes_no = input()

    if yes_no.lower() == "y":
        yn = True
        return yn

    elif yes_no.lower() == "n":
        yn = False
        return yn

    else:
        print("Please make a valid input (Please enter \"y\" for YES or \"n\" for NO)")
        day_input()


def month_year_input():
    print("Would you like to have folders show both the month and year? (ex: March 2004) (y/n)")
    yes_no = input()

    if yes_no.lower() == "y":
        yn = True
        return yn

    elif yes_no.lower() == "n":
        yn = False
        return yn

    else:
        print("Please make a valid input (Please enter \"y\" for YES or \"n\" for NO)")
        month_year_input()


def folder_remover_input():
    print("Would you like to remove all sub-folders? This will take the files inside the sub-folders and mix them with"
          " the files in the main folder (y/n)")
    yes_no = input()

    if yes_no.lower() == "y":
        yn = True
        return yn

    elif yes_no.lower() == "n":
        yn = False
        return yn

    else:
        print("Please make a valid input (Please enter \"y\" for YES or \"n\" for NO)")
        folder_remover_input()
