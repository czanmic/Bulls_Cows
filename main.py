"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Aneta Michulková
email: michulkova.aneta@gmail.com
"""
import random, time

def generate_unique_numbers():
    """
    Generate the 4 unique numbers from random library. 
    First number can not be 0.
    Type set up to string for better comparision.
    """
    first_digit_no_zero = random.choice(range(1,10)) 
    remaining_digits = random.sample([d for d in range(10) if d != first_digit_no_zero], 3) 
    digits_list = [first_digit_no_zero]+remaining_digits
    return "".join(str(num) for num in digits_list)
    
secret_number = generate_unique_numbers()
#print(secret_number) # testing purpose only

def is_valid(guess):
    """
    function controls the input logic: 
    Guess must be exactly 4 unique digitals and can not start with 0.
    If conditions are not met, it returns warrning and do not let you to continue.
    If conditions are met, it returns None so you can continue in the game.
    """

    if not guess.isdigit():
        return "Input must be numeric"
    if len(guess) != 4:
        return "Input must be 4 digits"
    if guess[0] == "0":
        return "Number cannot start with zero"
    if len(set(guess)) != 4:
        return "Digits must be unique"
    return None  

bulls = 0
cows = 0
start_time = time.time()
guess_count = 0

while bulls != 4:
    guess = input(f"""
              Hi there!
              I've generated a random 4 digit number for you.
              Let's play a Bulls and Cows game.
              Enter a number:
              """)
    
    # calling the function is_valid.
    # if error then it shows the error message from function and exit the game
    error = is_valid(guess) 
    if error: 
        print(error) 
        guess_count += 1
        print("Please try again!")
        continue # do not exit the game; starting from the begining

    bulls = 0
    cows = 0
    guess_count += 1

    # comparision of the numbers from guess and secret_number
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")

end_time = time.time()
total_time = end_time - start_time

print("🎉 You won! 🎉",
      f"The secret number was {secret_number}.",
      f"You've got it in {guess_count} guesses.",
      f"Time: {total_time:.2f} seconds",
      sep="\n")
