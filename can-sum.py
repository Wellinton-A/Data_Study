l = [7,14]

def canSum(n, nums, cache = {}, li = []):
    if n == 0:
        return True
    if n < 0:
        return False
    if n in cache:
        return cache[n]
    else:
        for i in nums:
            remainder = n - i
            cache[n] = canSum(remainder, nums, cache, li)
            if canSum(remainder, nums, cache, li) == True:
                return True
    return False


print(canSum(0, l))