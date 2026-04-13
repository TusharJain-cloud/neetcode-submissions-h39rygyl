class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute Force but the T.C -> O(n^2)
        if len(s) != len(t):
            return False
        for i in s:
            if i in t:
                t = t.replace(i, "", 1)

        return t == ""
        # Now using Hashmaps
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in countS:
            countS[i] = 1 + countS.get(countS[i], 0)
            countT[i] = 1 + countT.get(countT[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(countT[c],0):
                return False
        
        return True
        