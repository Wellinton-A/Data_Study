
list1 = [6,44,8,1,68,4,98]

def bubble_sort(list):
    for i in range(len(list)-1):
        print(list)
        if list[i] > list[i+1]:
            for j in range(0, i+1):
                if list[j] > list[i+1]:
                    list[i+1], list[j] = list[j], list[i+1]


bubble_sort(list1)