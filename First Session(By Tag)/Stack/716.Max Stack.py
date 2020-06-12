# Solution 1: Two Stacks
# The only different with Min Stack Question is the popMax operation.
# For this operation, we know what the current maximum(peekMax) is.
# We can pop until we find the maximum, and then push back the poped
# elements back to the stack.

# Time Complexity: popMax is O(n) for the worst-case and other
# operations are O(1).
# Space Complexity: O(n)

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_tracker = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_tracker or self.max_tracker[-1] <= x:
            self.max_tracker.append(x)

    def pop(self) -> int:
        if self.max_tracker[-1] == self.stack[-1]:
            self.max_tracker.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_tracker[-1]

    def popMax(self) -> int:
        pre = []
        while self.stack[-1] != self.max_tracker[-1]:
            pre.append(self.stack.pop())
        max_pop = self.max_tracker.pop()
        self.stack.pop()
        for x in reversed(pre):
            self.push(x)
        return max_pop


