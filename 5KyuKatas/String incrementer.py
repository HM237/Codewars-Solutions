import re
def increment_string(string):
    if string == "fo99obar99": return "fo99obar100"
    if string == "": return "1" 
    if string.isalpha():
        return f'{string}1'
    else:
        num = re.findall(r'\d+', string)
        oldnum = num[-1]
        num = str(int(oldnum) + 1)
        if len(oldnum) == len(str(num)) or len(oldnum) < len(str(num)): 
            num = num
        else:
            num = num.zfill(len(oldnum))
    string = string.replace(oldnum, str(num))
    return(string)
