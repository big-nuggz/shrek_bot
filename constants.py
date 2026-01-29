from tokenizer import WordTokenizer, CharacterTokenizer


SHREK_PATH = './data/shrek.txt'
MATRIX_PATH = './matrix/shrek_word_n2.pkl'
TOKEN_PATH = './token.txt'

TOKENIZER = WordTokenizer
MATRIX_N = 2
TEMPERATURE = 10

COOLDOWN_SECONDS = 5