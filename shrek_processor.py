import re


def process_shrek(path: str) -> str:
    '''
    processes shrek script text for language processing
    
    :param path: path to script file
    :type path: str
    :return: processed text
    :rtype: str
    '''
    lines = ['[SOL]']
    start_of_line = True
    with open(path, mode='r', encoding='utf8') as f:
        for line in list(f)[2: 3011]: # ignore SHREK SCRIPT and the ending songs
            # line = re.sub(r'\{.*?\}', '', line)
            line = line.lower()
            line = re.sub(r'\.{2,}', ' .', line)
            line = re.sub(r'\?{2,}', ' ?', line)
            line = re.sub(r'\!{2,}', ' !', line)
            line = line.replace('\n', '')
            line = line.replace(' -', '')
            line = line.replace('-', '')
            line = line.replace('.', ' . [EOL] [SOL]')
            line = line.replace(',', ' ,')
            line = line.replace('?', ' ? [EOL] [SOL]')
            line = line.replace('!', ' ! [EOL] [SOL]')
            line = line.strip()
            
            if line =='':
                continue

            lines.append(line)
                         
    return ' '.join(lines)


if __name__ == '__main__':
    from constants import SHREK_PATH
    processed_shrek = process_shrek(SHREK_PATH)
    # print(processed_shrek)
    print(processed_shrek)
