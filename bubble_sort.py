import random

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
numbers2 = list(range(1,100,50))

def bubbleSort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                print(list)
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux


bubbleSort(numbers)

print(numbers)