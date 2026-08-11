class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Find Peak
        l, r = 1, mountainArr.length() - 2

        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        
        peak = m

        # Finding the target in the ascending sorted array
        l, r = 0, peak
        
        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)

            if value > target:
                r = m - 1
            elif value < target:
                l = m + 1
            else:
                return m

        # Finding the target in the descending sorted array
        l, r = peak, mountainArr.length() - 1

        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)

            if value > target:
                l = m + 1
            elif value < target:
                r = m - 1
            else:
                return m

        return -1