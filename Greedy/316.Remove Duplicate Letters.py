# Solution 1: Greedy--Solving with Stack

# As we iterate over our string, if character i is greater than character i+1
# and another occurrence of character i exists later in the string, deleting
# character i will always lead to the optimal solution. Characters that come
# later in this calculation because i is in a more significant spot. Even if
# character i+1 isn't the best yet, we can always replace it for a smaller
# character down the line if possible.
# Therefore, we will keep a stack to store the solution we have built as we iterate
# over the string, and we will delete characters off the stack whenever it is
# possible and it makes our string smaller.
# Each iteration we add the current character to the solution if it hasn't already
# been used. We try to remove as many characters as possible off the top of the
# stack, and then add the current character.

# The conditions for deletion are:
# 1. The character is greater than the current characters.
# 2. The character can be removed because it occurs later on.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        seen = set()

        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)
















