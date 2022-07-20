import functions
import User_input
import os

# List of all possible outcomes
dic_of_inputs = {
    (True, False, False, False): functions.year_only,
    (True, True, False, False): functions.month_only,
    (True, True, True, False): functions.day_only,
    (False, False, False, True): functions.my_only
}

if User_input.fr_input:
    functions.folder_remover()

# Places user input into the dictionary and picks out appropriate function
dic_of_inputs[User_input.qa_input]()

print("your files are now sorted")
