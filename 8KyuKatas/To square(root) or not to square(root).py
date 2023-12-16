def square_or_square_root(arr):
    new_arr=[]
    for x in arr:
        if x**0.5 == int(x**0.5):
            new_arr.append(int(x**0.5))
        else:
            new_arr.append(x**2)
    return new_arr
