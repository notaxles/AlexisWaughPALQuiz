for number in range(int(-200),1):
    if number%3 == 0:
        number = number - number - number
        print(f"{number}")