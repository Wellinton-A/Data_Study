import random

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

numbers2 = random.sample(range(0,100),58)

print(numbers2)

def insertionSort(list):
    for i in range(len(list)-1):
        if list[i+1] < list[i]:
            for j in range(0,i+1):
                if list[i+1] < list[j]:
                    list[i+1], list[j] = list[j], list[i+1]

insertionSort(numbers2)
print(numbers2)
