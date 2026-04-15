class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26 # a....z

        #     for c in s:
        #         count[ord(c) - ord("a")] += 1

        #     res[tuple(count)].append(s)
        
        # return list(res.values())
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(word)
        
        return list(res.values())

        