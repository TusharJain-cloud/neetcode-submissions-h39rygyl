class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resLen = 0
        res = ""

        for i in range(len(s)):
            # For odd length string
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = max(resLen, (r - l + 1))
                    res = s[l : r + 1]
                l -= 1
                r += 1
            # For even length string
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = max(resLen, (r - l + 1))
                    res = s[l : r + 1]
                l -= 1
                r += 1

        return res