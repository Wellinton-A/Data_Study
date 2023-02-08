
l = [7,14]

def howSun(n, nums):
    if n == 0:
        return []
    if n < 0:
        return None
    for i in nums:
        remainder = n - i
        remainderResult = howSun(remainder, nums)
        if remainderResult != None:
            remainderResult.append(i)
            return remainderResult

print(howSun(100, l))

def howSun2(n, nums, cache = {}):
    if n in cache:
        return cache[n]
    if n == 0:
        return []
    if n < 0:
        return None
    else:
        for i in nums:
            remainder = n - i
            remainderResult = howSun2(remainder, nums, cache)
            if remainderResult != None:
                remainderResult.append(i)
                cache[n] = len(remainderResult)
                return remainderResult
    cache[n] = None
    return None

print(howSun2(140, l))