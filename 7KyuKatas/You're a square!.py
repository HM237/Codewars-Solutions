def is_square(n):    
    if n<0:
        return False
    if int(n**0.5)==n**0.5:
        return True
    else:
        return False
