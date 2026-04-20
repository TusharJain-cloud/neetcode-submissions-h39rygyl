class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbour = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbour[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                
                if endWord == word:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neig in neighbour[pattern]:
                        if neig not in visit:
                            visit.add(neig)
                            q.append(neig)
            res += 1
            
        return 0
        