import re
def to_underscore(string):
    res_list = []
    snake = []
    if type(string) != str : return str(string)
    res_list = re.findall('[A-Z][^A-Z]*', string)
    for word in res_list: snake.append(word.lower())
    return "_".join(snake)
