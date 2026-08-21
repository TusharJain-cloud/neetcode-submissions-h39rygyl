class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def add(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add(word)
        
        path, res = set(), set()
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, node, word):
            if (r < 0 or c < 0 or c >= cols or r >= rows or (r, c) in path or board[r][c] not in node.children):
                return
            
            path.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end_of_word:
                res.add(word)
            backtrack(r + 1, c, node, word)
            backtrack(r - 1, c, node, word)
            backtrack(r, c + 1, node, word)
            backtrack(r, c - 1, node, word)

            path.remove((r, c))
            
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root, "")
        
        return list(res)
        
