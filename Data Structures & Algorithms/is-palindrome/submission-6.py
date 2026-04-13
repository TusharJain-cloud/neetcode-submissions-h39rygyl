class Solution:
    def isPalindrome(self, s: str) -> bool:
        # The T.C -> O(n) and S.C -> O(n)
        # s_alpha = ""
        # for c in s:
        #     if c.isalnum():
        #         s_alpha += c.lower()
        
        # return s_alpha == s_alpha[::-1]

        # The T.C -> O(n) and S.C -> O(1)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alpha_num(s[l]):
                l += 1
            while l < r and not self.alpha_num(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True 
            
    
    # checks whether the character is alpha numeric using ascii codes
    def alpha_num(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))