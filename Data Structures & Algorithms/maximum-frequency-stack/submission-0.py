class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.max_cnt = 0
        self.stack = {}

    def push(self, val: int) -> None:
        count = 1 + self.cnt.get(val, 0)
        self.cnt[val] = count
        if count > self.max_cnt:
            self.max_cnt = count
            self.stack[count] = []
        self.stack[count].append(val)

    def pop(self) -> int:
        res = self.stack[self.max_cnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.max_cnt]:
            self.max_cnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()