# https://projecteuler.net/problem=31

def count_coin_combinations(target, coins):
    # Initialize a DP array where dp[i] = number of ways to make amount i
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: 1 way to make 0p (using no coins)

    for coin in coins:

        for j in range(coin, target + 1):
            dp[j] += dp[j - coin]  # Add ways to make (j - coin) to dp[j]

    return dp[target]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

result = count_coin_combinations(target, coins)
print(result)
