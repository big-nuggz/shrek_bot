import random
import time

from constants import MATRIX_PATH, TOKENIZER, TEMPERATURE
from matrix import load_matrix
from generator import generate_sentence


if __name__ == "__main__":
    tokenizer = TOKENIZER()
    matrix = load_matrix(MATRIX_PATH)

    all_SOL = [key for key in matrix.keys() if key[0] == tokenizer.SOL] # all starting words

    for _ in range(10):
        starting_words = all_SOL[random.randint(0, len(all_SOL) - 1)]
        output = generate_sentence(matrix, tokenizer, starting_words, temperature=TEMPERATURE)

        print(output)
