def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = [int(i) for i in numbers]
    return (f"{max(numbers)} {min(numbers)}")
