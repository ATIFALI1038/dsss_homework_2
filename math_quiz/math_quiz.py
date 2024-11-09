import random

def generate_random_number(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).
    
    Parameters:
    min_value (int): The minimum value for the random number.
    max_value (int): The maximum value for the random number.

    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Chooses a random operator from the list of supported operators: +, -, *.
    
    Returns:
    str: A randomly selected operator as a string.
    """
    return random.choice(['+', '-', '*'])


def calculate_answer(num1, num2, operator):
    """
    Calculates the answer to a mathematical expression based on two numbers and an operator.
    
    Parameters:
    num1 (int): The first number in the expression.
    num2 (int): The second number in the expression.
    operator (str): The operator, one of '+', '-', or '*'.
    
    Returns:
    tuple: A tuple containing the problem string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    
    # Compute the correct answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        raise ValueError("Unsupported operator")  # Raise an error if an unsupported operator is encountered

    return problem, answer


def math_quiz():
    """
    Main function to run the Math Quiz game. Generates random math problems for the user to solve.
    """
    score = 0
    total_questions = 3  # Set total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)  # Set as integer for consistency
        operator = generate_random_operator()

        problem, correct_answer = calculate_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        # Error handling for user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

