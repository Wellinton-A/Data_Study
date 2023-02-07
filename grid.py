

t2 = 0
def gridTraveler(m,n):
    global t2
    t2 += 1
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

t = 0
def gridTravMemo(m, n, cache = {}):
    global t
    k = str(m) + ',' + str(n)
    if k in cache:
        return cache[k]
    else:
        t += 1
        if m == 0 or n == 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        else:
            cache[k] = gridTravMemo(m - 1, n, cache) + gridTravMemo(m, n - 1, cache)
            return cache[k]



print(gridTraveler(4, 3))
print(f'times: {t2}')
print(gridTravMemo(10, 10))
print(f'times: {t}')