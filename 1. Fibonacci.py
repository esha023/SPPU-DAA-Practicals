def fibonacci_iterative(n:int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        dp = [0] * n
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

def fibonacci_recursive(n):
    cache = {1:0, 2:1}
    return helper(n,cache)

def helper(n:int, cache):
    if n in cache:
        return cache[n]
    else:
        result = helper(n-1, cache) + helper(n-2, cache)
        cache[n] = result
        return result
        
print(fibonacci_iterative(5))
print(fibonacci_recursive(5))