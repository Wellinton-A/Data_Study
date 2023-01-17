import random

list1 = [26, 73, 55, 88, 10, 10, 3, 4, 4,14,14,14,28,39,40,40,1,2] 
# 5, 42, 51, 27, 71, 66, 45, 8, 26, 21, 56, 92, 36, 91, 91, 63, 14, 31, 61, 1, 98, 54, 25, 33, 3, 24, 75, 95, 61, 61, 52, 19, 99, 13, 9, 40, 59, 86, 64, 99, 99, 17, 69, 68, 72, 39, 16, 60, 30, 94]
print(list1)
sum2 = 3
# def pair_sum(li, sum1):
#     k = 0
#     j = len(li)-1
#     while k < j:
#         if li[k] + li[j] == sum1:
#             return li[k], li[j]
#         elif li[k] + li[j] > sum1:
#             j -= 1
#         else:
#             k += 1
#     return f'there\'s not a sum pair'

# print(pair_sum(list1, sum2))


def pair_sum_unsorted(li, sum1):
    comp = set()
    for i in range(len(li)):
        print(comp)
        if li[i] not in comp:
            comp.add(sum1 - li[i])
        else:
            return True
    return False

print(pair_sum_unsorted(list1, sum2))


array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'y', 'y']
array3 = ['z', 'y', 'x']

def arrays_contain(arr1, arr2):
    return not set(arr1).isdisjoint(arr2)

print(arrays_contain(array2, array1))
print(arrays_contain(array1, array3))

def arrays_contain_dict(arr1, arr2): #O(n+m) time complexity
    a = {k:True for k in arr1}       #O(n) space complexity
    for i in arr2:
        if i in a.keys():
            return True
    return False

print(arrays_contain_dict(array1, array2))
print(arrays_contain_dict(array1, array3))