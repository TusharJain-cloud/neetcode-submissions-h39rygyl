class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pos_diag = set()
        neg_diag = set()

        res = 0

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return res

            for c in range(n):
                if c in col or (r - c) in neg_diag or (r + c) in pos_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return res