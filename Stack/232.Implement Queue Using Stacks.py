# Solution 1: (Two Stacks)
# Push - O(n) per operation,
# Pop - O(1) per operation.

# A queue is FIFO(first-in-first-out) but a stack is LIFO.
# This means the newest element must be pushed to the bottom of
# the stack. To do so, we first transfer all the elements in s1
# to the auxiliary stack s2. Then push the new arrived element
# to the bottom of the s1 and all the elements in s2 are popped
# and pushed back to s1.

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0

# Solution 2: Two Stacks
# Push - O(1) per operation
# Pop - Amortized O(1) per operation

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

