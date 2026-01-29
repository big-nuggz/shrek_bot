import pickle


def build_matrix(tokens: list, n=2) -> dict:
    '''
    build a markov matrix, n tokens vs 1 following token
    
    :param tokens: list of tokens
    :type tokens: list
    :return: the probability matrix, dict of dict, with key as starting n tokens and secondary key as token with associated number of occurrences
    :rtype: dict
    '''
    matrix = {}
    chain = []
    for token in tokens:
        chain.append(token)
        if len(chain) < (n + 1):
            continue

        key = tuple(chain[:n])
        if key not in matrix.keys():
            matrix[key] = {}

        if token in matrix[key].keys():
            matrix[key][token] += 1
        else:
            matrix[key][token] = 1

        del chain[0]

    return matrix


def save_matrix(matrix: dict, path: str) -> None:
    with open(path, 'wb') as bf:
        pickle.dump(matrix, bf)


def load_matrix(path: str) -> dict:
    with open(path, 'rb') as bf:
        return pickle.load(bf)


if __name__ == '__main__':
    from shrek_processor import process_shrek
    from constants import SHREK_PATH, MATRIX_PATH, TOKENIZER, MATRIX_N

    tokenizer = TOKENIZER()

    shrek_text = process_shrek(SHREK_PATH)
    
    data = tokenizer.process_data(shrek_text, lower=True, add_sol_eol=True)
    tokens = tokenizer.tokenize(data)
    matrix = build_matrix(tokens, n=MATRIX_N)

    save_matrix(matrix, MATRIX_PATH)
