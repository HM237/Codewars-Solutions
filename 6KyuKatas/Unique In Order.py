def unique_in_order(sequence):
    array = []
    for character in sequence:
        if character not in array:
            array.append(character)
        else:
            if array[-1] != character:
                array.append(character)
    return array
