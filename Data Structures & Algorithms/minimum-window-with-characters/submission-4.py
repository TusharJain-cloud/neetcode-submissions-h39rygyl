class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        window, count_T = {}, {}
        res, res_len = [-1, -1], float("infinity")

        for c in t:
            count_T[c] = 1 + count_T.get(c, 0)

        l = 0
        have, need = 0, len(count_T)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_T and window[c] == count_T[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in count_T and window[s[l]] < count_T[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if res_len != float("infinity") else ""
