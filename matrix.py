import pickle


def build_matrix(data: str) -> dict:
    '''
    build a markov matrix, 2 word vs 1 following word
    
    :param data: data as single string
    :type data: str
    :return: the probability matrix, dict of dict, with key as starting 2 words and secondary key as word with associated number of occurrences
    :rtype: dict
    '''
    matrix = {}
    chain = []
    for word in data.split(' '):
        chain.append(word)
        if len(chain) < 3:
            continue

        key = tuple(chain[:2])
        if key not in matrix.keys():
            matrix[key] = {}

        if word in matrix[key].keys():
            matrix[key][word] += 1
        else:
            matrix[key][word] = 1

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
    from constants import SHREK_PATH, MATRIX_PATH

    processed_shrek = process_shrek(SHREK_PATH)
    matrix = build_matrix(processed_shrek)

    save_matrix(matrix, MATRIX_PATH)
