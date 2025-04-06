class MyQueue:

    # Amortized O(1) solution, push only to input list, pop/peek from output list
    # Average case is O(1)

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        popped = int
        if not len(self.outStack):
            for i in range(len(self.inStack)-1, -1, -1):
                self.outStack.append(self.inStack.pop())
        popped = self.outStack.pop()
        return popped
                
    def peek(self) -> int:
        if not len(self.outStack):
            for i in range(len(self.inStack)-1, -1, -1):
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self) -> bool:
        return len(self.inStack) == 0 and len(self.outStack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()