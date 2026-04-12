class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # res = {} #value : index

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in res:
        #         return [res[diff], i]
            
        #     res[n] = i
         
        # res = [];

        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             res.append(i)
        #             res.append(j)
                
        # return res
        res = {}  # value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in res:
                return [res[diff], i]

            res[n] = i
        