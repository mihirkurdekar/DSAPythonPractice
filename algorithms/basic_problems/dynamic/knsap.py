'''
Implement dynamic programming to solve the 0/1 Knapsack problem.
'''
def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # The maximum value is in the bottom-right corner of the table

# Example usage:
if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [10, 15, 40]
    capacity = 6
    max_value = knapsack(weights, values, capacity)
    print(f"Maximum value in Knapsack with capacity {capacity}: {max_value}")
    # Output should be: Maximum value in Knapsack with capacity 6: 55