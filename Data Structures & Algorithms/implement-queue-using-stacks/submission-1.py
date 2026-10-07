class MyQueue:

    def __init__(self):
        # s1 = input stack: new elements 
        # s2 = output stack: elements ready to leave the queue 
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # Always push new elements onto s1
        self.s1.append(x)

    def pop(self) -> int:
        # If s2 is empty, move everything from s1 -> s2
        # This reverses the order and fgives us FIFO behavior 
        if not self.s2: 
            while self.s1:
                self.s2.append(self.s1.pop())
        
        # Oldest element is now on top of s2
        return self.s2.pop()

    def peek(self) -> int:
        # Same transfer logic as pop()
        if not self.s2: 
            while self.s1:
                self.s2.append(self.s1.pop())
        
        # Look at the oldest element without removing it 
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue is empty only when BOTH stacks are empty 
        return max(len(self.s1), len(self.s2)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()