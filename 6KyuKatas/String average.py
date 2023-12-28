def average_string(s):
    temp=[]
    count = 0
    dict = {"zero":0,
            "one":1,
            "two": 2, 
            "three":3, 
            "four":4,
            "five":5,
            "six":6,
            "seven":7,
            "eight":8,
            "nine":9}
    for i in s.split(" "):
        if i in dict:
            number = dict[i]
            temp.append(number)
            count +=1
        else: return "n/a"
    average = int(sum(temp) / count)
    for key, value in dict.items():
        if average == value: return key
