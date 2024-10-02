def valid_phone_number(phone_number):
    if len(phone_number) > 14 or len(phone_number) < 14: return False    
    elif phone_number[0] != "(": return False
    elif phone_number[4] != ")": return False
    elif len(phone_number) > 14 or len(phone_number) < 14: return False
    elif phone_number[1] not in list ("1234567890"): return False
    elif phone_number[2] not in list ("1234567890"): return False
    elif phone_number[3] not in list ("1234567890"): return False
    elif phone_number[5] != " ": return False
    elif phone_number[6] not in list ("1234567890"): return False
    elif phone_number[7] not in list ("1234567890"): return False
    elif phone_number[8] not in list ("1234567890"): return False
    elif phone_number[9] != "-": return False
    elif phone_number[10] not in list ("1234567890"): return False
    elif phone_number[11] not in list ("1234567890"): return False
    elif phone_number[12] not in list ("1234567890"): return False
    elif phone_number[13] not in list ("1234567890"): return False
    else: return True

  #THIS SOLUTION WAS DONE FOR FUN HENCE WHY SOO MANY IF/ELIF STATEMENTS!!!
