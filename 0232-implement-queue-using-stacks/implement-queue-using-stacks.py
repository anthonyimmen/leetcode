class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        if not len(self.inStack):
            self.inStack.append(x)
        else:
            for val in self.outStack:
                self.inStack.append(self.outStack.pop)
            self.inStack.append(x)

    def pop(self) -> int:
        if not len(self.outStack):
            for _ in range(len(self.inStack)):
                popped = self.inStack.pop()
                self.outStack.append(popped)
        popped = self.outStack.pop()
        return popped
        
    def peek(self) -> int:
        if len(self.outStack):
            return self.outStack[len(self.outStack)-1]
        else:
            return self.inStack[0]

    def empty(self) -> bool:
        return len(self.inStack) == 0 and len(self.outStack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()