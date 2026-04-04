class MyQueue:

    def __init__(self):
        self.stk = []
        self.stkSeek = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        
    def pop(self) -> int:
        if self.stkSeek:
            return self.stkSeek.pop()
        else:
            while self.stk:
                self.stkSeek.append(self.stk.pop())
            return self.stkSeek.pop()
        
    def peek(self) -> int:
        return self.stkSeek[-1] if self.stkSeek else self.stk[0]

    def empty(self) -> bool:
        return True if not self.stkSeek and not self.stk else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()