def sumNatural(int):
    if int == 0:
        return int
    return sumNatural(int-1) + int

print(sumNatural(14))

