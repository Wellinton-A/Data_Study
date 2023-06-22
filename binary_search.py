import random

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
numbers2 = range(1,100)
numbers.sort()

def binarySearchRecursion(list, n):
    mid = len(list) // 2
    if mid > len(list)-1:
        return False
    elif list[mid] == n:
        return list[mid]
    elif list[mid] < n:
        print(list[mid+1:len(list)])
        return binarySearchRecursion(list[mid+1:len(list)], n)
    else:
        print(list[0:mid])
        return binarySearchRecursion(list[0:mid], n)

print(numbers)

print(binarySearchRecursion(numbers, 105))

def binarySearchLoops(list, n):
    lower = 0
    greater = len(list)-1
    while lower <= greater:
        mid = (lower + greater) // 2
        if list[mid] == n:
            return True
        elif list[mid] > n:
            greater = mid - 1
        else:
            lower = mid +1
    return False

print(binarySearchLoops(numbers, 44))