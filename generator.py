import random
from tokenizer import Tokenizer

def select_with_temperature(choices, temperature=1.0):
    tokens = list(choices.keys())
    weights = [p ** (1 / temperature) for p in choices.values()]
    
    return random.choices(tokens, weights=weights, k=1)[0]


def generate_sentence(matrix: dict, tokenizer: Tokenizer, start: tuple, max_tokens=200, temperature=0.1) -> str:
    '''
    generate a sentence with given matrix until EOL, or max_words word count is reached
    
    :param matrix: probability matrix dictionary
    :type matrix dict
    :param start: 2 starting words as tuple
    :type start: tuple
    :param max_words: maximum number of words that can be generated if EOL is not reached
    :type max_words: int
    :param temperature: random picker temp, higher the more random
    :type temperature: float
    :return: Description
    :rtype: str
    '''
    n = len(start)
    output = list(start)
    for _ in range(max_tokens):
        key = tuple(output[-n:])
        choices = matrix[key]
        choice = select_with_temperature(choices, temperature)

        if choice == tokenizer.EOL:
            break

        output.append(choice)

    output = tokenizer.stringify(output)
    output = output.strip()
    output = output.replace(' .', '.')
    output = output.replace(' ,', ',')
    output = output.replace(' ?', '?')
    output = output.replace(' !', '!')
    output = output.replace('{', '*')
    output = output.replace('}', '*')
    output = output.capitalize()

    return output
