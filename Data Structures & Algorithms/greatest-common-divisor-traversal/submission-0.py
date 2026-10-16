class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return
        if p1 > p2:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]  
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.count -= 1  

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        fact = {}

        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in fact:
                        uf.union(i, fact[f])
                    else:
                        fact[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in fact:
                    uf.union(i, fact[n])
                else:
                    fact[n] = i
        
        return uf.count == 1