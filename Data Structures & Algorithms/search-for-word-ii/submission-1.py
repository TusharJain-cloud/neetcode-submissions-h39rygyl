class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def add(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for w in words:
            root.add(w)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if(r < 0 or c < 0 or r == rows or c == cols or board[r][c] not in node.children or (r,c) in visit):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            

            visit.remove((r, c))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")

        return list(res)