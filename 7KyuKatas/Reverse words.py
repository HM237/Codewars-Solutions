def reverse_words(text):
    text = text.split(" ")
    reverse = []
    for word in text: reverse.append(word[::-1])
    return " ".join(reverse)
