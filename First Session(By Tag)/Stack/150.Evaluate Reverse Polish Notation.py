# Solution 1: Using Stack

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        stack = []
        for ch in tokens:
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                operation = operations[ch]
                stack.append(operation(num2, num1))
        return stack[0]