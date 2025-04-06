class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        print(self.stack)

    def pop(self) -> int:
        popped = self.stack.pop(len(self.stack)-1)
        return popped
        
    def peek(self) -> int:
        return self.stack[len(self.stack)-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()