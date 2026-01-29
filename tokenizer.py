class Tokenizer:
    '''
    base tokenizer class, inherit and fill in to specifications
    '''
    def __init__(self):
        self.SOL = (123456789,)
        self.EOL = (987654321,)

    def process_data(self, data: str) -> list:
        pass

    def tokenize(self, data: list) -> list:
        pass

    def stringify(self, tokens: list) -> str:
        pass

    def to_token(self, data: str) -> tuple:
        pass

    def from_token(self, token: tuple) -> str:
        pass


class WordTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()

    def process_data(self, data, lower=True, add_sol_eol=True):
        return _process_text(data, lower=lower, delimiter=' ', add_sol_eol=add_sol_eol)

    def tokenize(self, data):
        tokens = [self.to_token(word) for word in data]
        return tokens
    
    def stringify(self, tokens: list) -> str:
        return  ' '.join([self.from_token(token) for token in tokens if token not in [self.SOL, self.EOL]])

    def to_token(self, word: str) -> tuple:
        if word == '[START_OF_LINE]':
            return self.SOL
        
        if word == '[END_OF_LINE]':
            return self.EOL
        
        return tuple([ord(c) for c in word])
    
    def from_token(self, token: tuple) -> str:
        if token == self.SOL:
            return '[START_OF_LINE]'
        
        if token == self.EOL:
            return '[END_OF_LINE]'

        return ''.join([chr(c) for c in token])
    

class CharacterTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()

    def process_data(self, data, lower=True, add_sol_eol=True):
        return _process_text(data, lower=lower, delimiter=None, add_sol_eol=add_sol_eol)

    def tokenize(self, data):
        tokens = [self.to_token(c) for c in data]
        return tokens
    
    def stringify(self, tokens: list) -> str:
        return  ''.join([self.from_token(token) for token in tokens if token not in [self.SOL, self.EOL]])

    def to_token(self, char: str) -> tuple:
        if char == '[START_OF_LINE]':
            return self.SOL
        
        if char == '[END_OF_LINE]':
            return self.EOL
        
        return (ord(char),)
    
    def from_token(self, token: tuple) -> str:
        if token == self.SOL:
            return '[START_OF_LINE]'
        
        if token == self.EOL:
            return '[END_OF_LINE]'

        return chr(token[0])


def _process_text(data: str, lower=True, delimiter=' ', add_sol_eol=True) -> str:
    '''
    process the text data, so it's ready to be tokenized

    adds special SOL and EOL texts if specified
    
    :param data: text data
    :type data: str
    :param lower: convert to lowercase?
    :type lower: bool
    :param delimiter: if None, split by every character
    :type delimiter: str
    :param add_sol_eol: add special SOL and EOL strings?
    :type add_sol_eol: bool
    :return: processed text data
    :rtype: str
    '''
    processed = data

    if lower:
        processed = processed.lower()

    if delimiter:
        processed = [chunk for chunk in processed.split(delimiter)]
    else:
        processed = [c for c in processed]

    if not add_sol_eol:
        return processed

    processed = ['[START_OF_LINE]'] + processed
    i = 0
    for element in processed:
        i += 1

        if (element[-1] in ['.', '?', '!']):
            processed = processed[:i] + ['[END_OF_LINE]', '[START_OF_LINE]'] + processed[i:]
            i += 2

    if processed[-1] == '[START_OF_LINE]':
        del processed[-1]
    
    return processed

if __name__ == "__main__":
    data = "This is a test data. This data should provide enough material for the tokenizer to work with. I'm just gonna fill some random words. WOOO."

    for tokenizer_class in [WordTokenizer, CharacterTokenizer]:
        tokenizer = tokenizer_class()

        processed = tokenizer.process_data(data) # ready raw text data so it's a list tokenizer can process
        # print(processed)
        tokens = tokenizer.tokenize(processed) # tokenize the processed list
        # print(tokens)
        text = tokenizer.stringify(tokens) # convert the tokens back into string
        print(text)