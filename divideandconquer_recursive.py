def divideAndConquer(li, x, right, left=0):
    mid = (left + right) // 2
    print(mid)
    if left > right:
        return False
    elif li[mid] == x:
        return True, mid
    elif x < li[mid]:
        return divideAndConquer(li, x, mid-1)
    else:
        return divideAndConquer(li, x, right, mid+1)
    


list1 = list(range(1,55))
print(divideAndConquer(list1, 60, len(list1)-1))

list2 = [ 2, 65, 34, 2, 1, 7, 8]

list2.sort(reverse=True)
print(list2)
