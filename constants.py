from tokenizer import WordTokenizer, CharacterTokenizer


SHREK_PATH = './data/shrek.txt'
MATRIX_PATH = './matrix/shrek_word_n2.pkl'
TOKEN_PATH = './token.txt'

TOKENIZER = WordTokenizer # which tokenizer? WordTokenizer tokenizes each words, CharacterTokenizer tokenizes each letters
MATRIX_N = 2 # number of tokens used as key in matrix
TEMPERATURE = 10 # basically randomness out output, higher the more chaotic

COOLDOWN_SECONDS = 5 # bot cool down period in seconds. so people can't spam the bot