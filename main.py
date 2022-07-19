import functions
import User_input

# List of all possible outcomes
dic_of_inputs = {
    (True, False, False, False, False): functions.year_only,
    (True, True, False, False, False): functions.month_only,
    (True, True, True, False, False): functions.day_only,
    (True, False, False, True, False): functions.year_pv,
    (True, True, False, True, False): functions.month_pv(),
    (True, True, True, True, False): functions.day_pv(),
    (False, False, False, False, True): functions.my_only(),
    (False, False, False, True, True): functions.my_pv(),
}

print(User_input.qa_input)
# Places user input into the dictionary and picks out appropriate function
dic_of_inputs[User_input.qa_input]()
