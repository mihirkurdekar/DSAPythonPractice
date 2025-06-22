'''
Given a string, find the length of the longest palindromic subsequence.
'''

def longest_palindromic_subsequence(s: str) -> int:
    n = len(s)
    # Create a 2D array to store lengths of longest palindromic subsequences
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the table in bottom-up manner
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of the substring
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]  # The result is in the top-right corner of the table   


def longest_palindromic_subsequence_recursive(s: str) -> int:
    def helper(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return 2 + helper(i + 1, j - 1)
        else:
            return max(helper(i + 1, j), helper(i, j - 1))

    return helper(0, len(s) - 1)

# Example usage:
if __name__ == "__main__":
    s = "bbabcbcab"
    print(f"Length of the longest palindromic subsequence in '{s}': {longest_palindromic_subsequence(s)}")
    # Output should be: Length of the longest palindromic subsequence in 'bbabcbcab': 7
    print(f"Length of the longest palindromic subsequence in '{s}' (recursive): {longest_palindromic_subsequence_recursive(s)}")
    # Output should be: Length of the longest palindromic subsequence in 'bbabcbcab' (recursive): 7