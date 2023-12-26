def is_int_array(arr):
    answer = True
    if arr == None or arr == "" or arr == [None]: 
        return False
    elif arr == []: 
        return answer
    elif type(arr) in [str,int, float]: 
        return False
    elif type(arr) in [bool, set, dict]: return False
    for i in arr:
        if i in [None, False] or type(i) == str: answer = False
        elif type(i) == float:
            n = i * 10
            if n % 10 != 0:
                answer = False
    return answer
