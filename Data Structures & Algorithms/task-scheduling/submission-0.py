class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()

        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    queue.append([val, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
        