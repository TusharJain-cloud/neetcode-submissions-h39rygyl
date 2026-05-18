class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y)
            

        stones.append(0)
        return -stones[0]

