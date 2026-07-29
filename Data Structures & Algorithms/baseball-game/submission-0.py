class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for x in operations:
            if x == "C":
                stack.pop()
            elif x == "D":
                double = 2 * stack[-1]
                stack.append(double)
            elif x == "+":
                add = stack[-1] + stack[-2]
                stack.append(add)
            else:
                stack.append(int(x))

        return sum(stack)
        