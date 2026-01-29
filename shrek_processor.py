import re


def process_shrek(path: str) -> str:
    '''
    processes shrek script text for language processing
    
    :param path: path to script file
    :type path: str
    :return: processed text
    :rtype: str
    '''
    lines = []
    with open(path, mode='r', encoding='utf8') as f:
        for line in list(f)[2: 3011]: # ignore SHREK SCRIPT and the ending songs
            # line = re.sub(r'\{.*?\}', '', line) # comment this bit out if you want to include the {} bracketed bits
            line = re.sub(r'\.{2,}', ' .', line)
            line = re.sub(r'\?{2,}', ' ?', line)
            line = re.sub(r'\!{2,}', ' !', line)
            line = line.replace('\n', '')
            line = line.replace(' -', '')
            line = line.replace('-', '')
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
