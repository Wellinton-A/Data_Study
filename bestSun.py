

def bestSum(n, nums):
    if n == 0:
        return []
    if n < 0:
        return None
    shortest = None
    for i in nums:
        remainder = n - i
        remainderResult = bestSum(remainder, nums)
        if remainderResult != None:
            remainderResult.append(i)
            combination =  remainderResult
        if shortest == None or len(shortest) > len(combination):
            shortest = remainderResult
    return shortest

print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
# print(bestSum(100, [1, 2, 5, 25]))