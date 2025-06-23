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

def knapsack_recursive(weights, values, capacity, n):
    # Base case: no items left or capacity is 0
    if n == 0 or capacity == 0:
        return 0

    # If the weight of the nth item is more than the capacity, skip it
    if weights[n - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, n - 1)

    # Return the maximum of two cases: including the nth item or excluding it
    else:
        include_item = values[n - 1] + knapsack_recursive(weights, values, capacity - weights[n - 1], n - 1)
        exclude_item = knapsack_recursive(weights, values, capacity, n - 1)
        return max(include_item, exclude_item)

# Example usage:
if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [10, 15, 40]
    capacity = 6
    max_value = knapsack(weights, values, capacity)
    print(f"Maximum value in Knapsack with capacity {capacity}: {max_value}")
    # Output should be: Maximum value in Knapsack with capacity 6: 55
    max_value_recursive = knapsack_recursive(weights, values, capacity, len(weights))
    print(f"Maximum value in Knapsack with capacity {capacity} (recursive): {max_value_recursive}")
    # Output should be: Maximum value in Knapsack with capacity 6 (recursive): 55