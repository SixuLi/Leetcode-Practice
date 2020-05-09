# Solution 1: Minimum Pairs
# Instead of only store one element in each position in the stack,
# we can store minimum pairs in the stack and the second position
# in the each pair contains the current minimum in the stack.
# And every time we push a new element in stack, we can compare
# it with current minimum for updating.

# Time Complexity: O(1) for all operations
# Space Complexity: O(n)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(current_min, x)))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Solution 2: Two Stacks
# We can use two stacks, one for the standard stack and the other
# is used to keep tracking of the current minimum.

# Time Complexity: O(1) for all operations
# Space Complexity: O(n)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_tracker = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_tracker or x <= self.min_tracker[-1]:
            self.min_tracker.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min_tracker[-1]:
            self.min_tracker.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracker[-1]

# Solution 3: Improved Two Stacks
# In the minimum tracker, we can store the number of replication
# of current minimum.

# Time Complexity: O(1) for all operations
# Space Complexity: O(n)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_tracker = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_tracker or x < self.min_tracker[-1][0]:
            self.min_tracker.append((x, 1))
        elif x == self.min_tracker[-1][0]:
            self.min_tracker[-1] = (self.min_tracker[-1][0], self.min_tracker[-1][1] + 1)

    def pop(self) -> None:
        if self.stack[-1] == self.min_tracker[-1][0]:
            if self.min_tracker[-1][1] == 1:
                self.min_tracker.pop()
            else:
                self.min_tracker[-1] = (self.min_tracker[-1][0], self.min_tracker[-1][1] - 1)
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracker[-1][0]


















