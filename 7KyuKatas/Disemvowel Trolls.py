def disemvowel(string):
    disemvowel = string
    list1 = list("aeiouAEIOU")
    for vowel in list1:
        if vowel in string: disemvowel = disemvowel.replace(vowel, "")
    return disemvowel
