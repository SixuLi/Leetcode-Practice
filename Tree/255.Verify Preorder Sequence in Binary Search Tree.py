# Solution 1: Using Stack
# The property of BST: for a given node in the tree, the value of any node in the left subtree will less than
# the value of this node and for the right subtree is opposite.

# We try to use this property of BST to solve this question:
# We set a check point and scan the preorder list. When scanning the list,
# if the value of current node is less than check point, we know that it will not be a valid BST, then return False.
# We first push the root into stack and during the scanning,
# 1. If the value of current node is less than the one on the top of stack,
# we know that this node belongs to the left subtree and we push this node into the stack.
# 2. If we find a value that larger than the top of stack,
# than we know that this node should be in the right subtree and we need to find out which node has this right child.
# So, we pop out the top stack value and let it to be the check point. And we continue this step until
# the stack is empty or the value of top stack is larger than current node. Next, push this node into stack.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack, pre_root = [], None
        for node in preorder:
            if pre_root and node < pre_root:
                return False
            while stack and node > stack[-1]:
                pre_root = stack.pop()
            stack.append(node)
        return True