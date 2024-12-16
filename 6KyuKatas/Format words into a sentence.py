def format_words(words):
    if words == None or words == [] or words == ['']: return ''
    count = words.count('')
    sentence = []
    for word in words:
        if word == '':
            if count == 1: pass
        else: sentence.append(word)
    if len(sentence)== 1: return sentence[0]
    return (', '.join(sentence[:-1])) + f' and {sentence[-1]}'
