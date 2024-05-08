def order(sentence):
    if sentence == "": return ""
    ordered_sentence = []
    array = sentence.split(" ")
    order = []
    indexes = []
    for word in array:
        index = array.index(word)
        for character in word:
            if character in "123456789":
                order.append(int(character))
                indexes.append(index)
    for i in range(1, max(order) + 1):
        position = order.index(i)
        ordered_sentence.append(array[position])
    return " ".join(ordered_sentence)
