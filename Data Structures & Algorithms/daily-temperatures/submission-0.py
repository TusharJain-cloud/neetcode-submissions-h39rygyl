class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp : index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_ind = stack.pop()
                res[stack_ind] = i - stack_ind
            stack.append([temp, i])
        
        return res