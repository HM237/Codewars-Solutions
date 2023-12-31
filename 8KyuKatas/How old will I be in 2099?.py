def calculate_age(year_of_birth, current_year):
    if current_year < year_of_birth:
        n = year_of_birth - current_year
        if n== 1: return f'You will be born in {n} year.'
        return f'You will be born in {n} years.'
    elif current_year == year_of_birth:
        return "You were born this very year!"
    else:
        n = current_year - year_of_birth
        if n== 1: return f'You are {n} year old.'
        return f"You are {n} years old."
