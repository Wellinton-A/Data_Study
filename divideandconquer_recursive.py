def divideAndConquer(li, x, right, left=0):
    if left > right:
        return False
    mid = (left + right) // 2
    if li[mid] == x:
        return True, li[mid]
    elif x < li[mid]:
        print(mid)
        return divideAndConquer(li, x, mid-1)
    else:
        print(mid)
        return divideAndConquer(li, x, right, mid+1)
    


list1 = list(range(1,51))
print(divideAndConquer(list1, 50, len(list1)-1))