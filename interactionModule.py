"""
The compare_value() function return a String depending on the relation (superior, egal, inferior) between the
value of its parameters.
"""


def compare_value(value, comparator):
    if value < comparator:
        return "It's bigger...\n"
    elif value > comparator:
        return "It's smaller...\n"
    elif value == comparator:
        return "It's the same values...\n"


"""
The final_msg() function return a String depending on the score.
"""


def final_msg(score):
    if score == 0:
        return 'The game is over for you, try again !'
    else:
        return f'Well done ! You won ! Your score is {score}'
