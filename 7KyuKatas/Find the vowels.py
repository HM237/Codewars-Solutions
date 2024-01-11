def vowel_indices(word):
    vowels = []
    count = 0
    for i in range(len(word)):
        if word[count].lower() in "aeiouy":
            vowels.append(count + 1)
        count+=1
    return(vowels)
