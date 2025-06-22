'''
Given two strings, find the length of the longest common subsequence.
Problem: Find the length of the longest common subsequence between the strings ABCBDAB and BDCABA.
Output: 4
'''

def longest_common_subsequence(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    # Create a 2D array to store lengths of longest common subsequences
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]  # The result is in the bottom-right corner of the table

def longest_common_subsequence_recursive(s1: str, s2: str) -> int:
    def helper(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + helper(i - 1, j - 1)
        else:
            return max(helper(i - 1, j), helper(i, j - 1))

    return helper(len(s1), len(s2))

# Example usage:
if __name__ == "__main__":
    s1 = "ABCBDAB"
    s2 = "BDCAB"
    print(f"Length of the longest common subsequence between '{s1}' and '{s2}': {longest_common_subsequence(s1, s2)}")
    # Output should be: Length of the longest common subsequence between 'ABCBDAB' and 'BDCAB': 4
    print(f"Length of the longest common subsequence between '{s1}' and '{s2}' (recursive): {longest_common_subsequence_recursive(s1, s2)}")
    # Output should be: Length of the longest common subsequence between 'ABCBDAB' and 'BDCAB' (recursive): 4