class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [] # to store the final result after merging

        # now we want to sort the intervals by their start time.
        intervals.sort(key = lambda i : i[0])

        # Now we insert the first interval to our result list as we want to overcome the edge case of empty result.
        res.append(intervals[0])

        for start, end in intervals[1:]:
            last_end = res[-1][1]

            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return res