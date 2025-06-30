def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    
    # Step 1: Create a 2D table with (m+1) x (n+1), filled with 0s
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the table from bottom to top, right to left
    for i in range(m - 1, -1, -1):     
        for j in range(n - 1, -1, -1):  
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    # Step 3: The final result is in dp[0][0]
    return dp[0][0]

text1 = "abcde"
text2 = "ace"
print("LCS length:", longestCommonSubsequence(text1, text2))

