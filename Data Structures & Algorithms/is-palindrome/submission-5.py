class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = ""
        for c in s:
            if c.isalnum():
                s_alpha += c.lower()
        
        return s_alpha == s_alpha[::-1]