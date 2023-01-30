def decimalToBinary(int):
    if int == 1:
        return 1
    if int == 0:
        return 0
    return str(decimalToBinary(int // 2)) + str(int % 2)

print(decimalToBinary(400))