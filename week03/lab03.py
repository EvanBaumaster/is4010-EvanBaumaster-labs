def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    This function demonstrates string formatting and function design
    by creating a Mad Libs-style story from user-provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story (e.g., "silly", "brave", "colorful").
    noun : str
        A noun to use in the story (e.g., "cat", "computer", "adventure").
    verb : str
        A past-tense verb to use in the story (e.g., "jumped", "crashed", "danced").

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.

    Examples
    --------
    >>> generate_mad_lib("silly", "cat", "jumped")
    "The silly cat jumped over the lazy dog and laughed."
    
    >>> generate_mad_lib("brave", "knight", "battled") 
    "Once upon a time, a brave knight battled dragons and saved the kingdom."
    """
    # TODO: Replace this with your creative story implementation
    # Must use f-string formatting and include all three parameters
    
    
    story = f"Once upon a time, a {adjective} {noun} {verb} through the enchanted forest, discovering magical secrets along the way."
    return story

# Test your function
# print(my_mad_lib("sparkly", "unicorn", "danced"))
print(generate_mad_lib("sparkly", "unicorn", "danced"))


import random

def guessing_game():
    """
    Plays a number guessing game with the user.
    
    This interactive game demonstrates while loops, conditionals, and user input
    handling. The user attempts to guess a randomly generated number between
    1 and 100, receiving feedback after each guess.

    Game Flow:
    1. Generate a random secret number between 1 and 100 (inclusive)
    2. Prompt the user with clear instructions
    3. Use a while loop to continue until the user guesses correctly
    4. For each guess:
       - Convert user input to integer
       - Compare guess to secret number
       - Provide feedback: "Too high!", "Too low!", or success
       - Count attempts
    5. When correct, congratulate user and show number of attempts
    6. Exit the game

    Input Validation:
    - Assume user will enter valid integers (error handling not required)
    
    Example Game Session:
    --------
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    Enter your guess: 50
    Too high! Try again.
    Enter your guess: 25
    Too low! Try again.
    Enter your guess: 37
    Congratulations! You guessed it in 3 attempts!
    """

    """
    Enhanced version of the guessing game with additional features.
    """
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Add a maximum number of attempts
    
    print("Enhanced Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        # TODO: Add the game logic here
        # 1. Get user input
        # 2. Increment attempts
        # 3. Check if guess is correct, too high, or too low
        # 4. If correct, congratulate and break
        # 5. If wrong, give feedback and continue
        # 6. If max attempts reached, reveal the number
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess > secret:
            print("Too high!")
        else:
            print("Too low!")

    if attempts >= max_attempts and guess != secret:
        print(f"Game over! The number was {secret}.")

# Test your enhanced game
# enhanced_guessing_game()
guessing_game()


if __name__ == '__main__':
    guessing_game()