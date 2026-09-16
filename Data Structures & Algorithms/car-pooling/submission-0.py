class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        min_heap = []
        cur_cap = 0

        for t in trips:
            num_pass, start, end = t
            while min_heap and min_heap[0][0] <= start:
                cur_cap -= min_heap[0][1]
                heapq.heappop(min_heap)

            cur_cap += num_pass
            if cur_cap > capacity:
                return False
            
            heapq.heappush(min_heap, [end, num_pass])
        
        return True

