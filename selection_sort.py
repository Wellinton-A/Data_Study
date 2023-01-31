import random

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

numbers2 = random.sample(range(-100,100),58)

print(numbers2)

def selectionSort(list):
    for i in range(len(list)):
        index = i
        for j in range(i+1, len(list)):
            if list[j] < list[index]:
                index = j
        aux = list[i]
        list[i] = list[index]
        list[index] = aux
        
                
selectionSort(numbers2)

print(numbers2)