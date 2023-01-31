import random

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
numbers2 = random.sample(range(1,100),58)
print(numbers2)

def bubbleSort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux


# bubbleSort(numbers)
bubbleSort(numbers2)


print(numbers2)