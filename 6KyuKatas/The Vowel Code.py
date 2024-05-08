def encode(st):
    encode_string = ""
    dict = {"a": 1, 
            "e": 2, 
            "i": 3, 
            "o": 4, 
            "u": 5}
    for letter in st:
        if letter in dict: encode_string += f"{dict.get(letter)}"
        else: encode_string += letter
    return encode_string
def decode(st):
    decode_string = ""
    dict = {"a": 1, 
            "e": 2, 
            "i": 3, 
            "o": 4, 
            "u": 5}
    x= dict.items()
    for letter in st:
        if letter in list("12345"):
            for key, value in x: 
                if value == int(letter): decode_string += key
        else: decode_string += letter
    return decode_string
