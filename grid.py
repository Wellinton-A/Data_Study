

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

def gridTraveler2(m, n):
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp)
    return dp[m][n]

print(gridTraveler2(3, 3))