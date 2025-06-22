'''
Longest Common Subsequence: Find the longest common subsequence between two strings.
'''

def longest_common_subsequence(str1, str2):
    """
    Find the longest common subsequence (LCS) between two strings using dynamic programming.
    
    :param str1: First string.
    :param str2: Second string.
    :return: Length of the longest common subsequence.
    """
    m, n = len(str1), len(str2)
    
    # Create a 2D array to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def longest_common_subsequence_recursive(str1, str2, m, n):
    """
    Find the longest common subsequence (LCS) between two strings using recursion.
    
    :param str1: First string.
    :param str2: Second string.
    :param m: Length of the first string.
    :param n: Length of the second string.
    :return: Length of the longest common subsequence.
    """
    if m == 0 or n == 0:
        return 0
    if str1[m - 1] == str2[n - 1]:
        return 1 + longest_common_subsequence_recursive(str1, str2, m - 1, n - 1)
    else:
        return max(longest_common_subsequence_recursive(str1, str2, m - 1, n),
                   longest_common_subsequence_recursive(str1, str2, m, n - 1))

# Example usage
if __name__ == "__main__":
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    lcs_length = longest_common_subsequence(str1, str2)
    print(f"The length of the longest common subsequence is: {lcs_length}")
    # Output: The length of the longest common subsequence is: 4
    lcs_length_recursive = longest_common_subsequence_recursive(str1, str2, len(str1), len(str2))
    print(f"The length of the longest common subsequence (recursive) is: {lcs_length_recursive}")
    # Output: The length of the longest common subsequence (recursive) is: 4