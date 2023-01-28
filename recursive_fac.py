def rec_factorial(number):
    if number == 1:
        return 1
    return number * rec_factorial(number - 1)

def factorial(number):
    answer = number
    for i in range(number):
        if number == 1:
            return answer
        answer = answer * (number-1)
        number -= 1

print(rec_factorial(2))