import random

def select_with_temperature(choices, temperature=1.0):
    words = list(choices.keys())
    weights = [p ** (1 / temperature) for p in choices.values()]
    
    return random.choices(words, weights=weights, k=1)[0]


def generate_sentence(matrix: dict, start: tuple, max_words=200, temperature=0.1) -> str:
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
    output = list(start)
    for _ in range(max_words):
        key = tuple(output[-2:])
        choices = matrix[key]
        choice = select_with_temperature(choices, temperature)

        if choice == '[EOL]':
            break

        output.append(choice)

    output = ' '.join(output)
    output = output.replace('[SOL] ', '')
    output = output.replace(' .', '.')
    output = output.replace(' ,', ',')
    output = output.replace(' ?', '?')
    output = output.replace(' !', '!')
    output = output.replace('{', '*')
    output = output.replace('}', '*')
    output = output.capitalize()

    return output


if __name__ == '__main__':
    from constants import MATRIX_PATH
    from matrix import load_matrix

    matrix = load_matrix(MATRIX_PATH)

    all_SOL = [key for key in matrix.keys() if key[0] == '[SOL]']

    # generate some random sentences
    for _ in range (10):
        starting_words = all_SOL[random.randint(0, len(all_SOL) - 1)]
        output = generate_sentence(matrix, starting_words, temperature=10)
        print(output)