# Solution 1: Dynamic Programming
# Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be
# a palindrome sine the two left and right end letters are the same.
# We define P(i,j) to store that whether substring S[i:j+1] is a palindrome. If it is, let P(i,j) = True, else False.
# Then we can update P(i,j) by P(i+1,j-1), S[i] and S[j]. Specifically, write as P(i,j) = P(i+1,j-1) and S[i] == S[j].
# And the basic cases are: P(i,i) = True and P(i,i+1) = (S[i] == S[i+1]).

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        ans = ''
        maxlen = 0
        dp = [n*[False] for _ in range(n)]
        for i in range(n):   # Initialize sub-palindrome with length 1.
            dp[i][i] = True
            ans = s[i]
            maxlen = 1
        for i in range(n-1): # Initialize sub-palindrome with length 2.
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]
                maxlen = 2
        for lens in range(3, n+1): # Loop by the length of sub-palindrome.
            for i in range(n):
                j = i + lens - 1
                if j < n:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                    if dp[i][j] == True:
                        ans = s[i:j+1]
                else:
                    break
        return ans

# Solution 2: Expand from the Center.
# There are two kinds of centers, one only contains 1 letter and the other contains two same letters.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ans = ""
        for i in range(len(s)):
            str1 = self.getLongest(s, i, i)
            str2 = self.getLongest(s, i, i + 1)
            if len(str1) > len(str2) and len(str1) > len(ans):
                ans = str1
            elif len(str1) < len(str2) and len(str2) > len(ans):
                ans = str2
        return ans

    def getLongest(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


























