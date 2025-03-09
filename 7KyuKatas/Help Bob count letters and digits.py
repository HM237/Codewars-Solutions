def count_letters_and_digits(s): return len([x for x in s if x.lower() in 'abcedfghijklmnopqrstuvwxyz' or x in '1234567890'])
