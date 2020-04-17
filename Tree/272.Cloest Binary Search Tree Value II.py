# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Inorder Traversal
# Time Complexity: O(N+K)
# Space Complexity: O(N)

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return []
        in_order = []
        self.inorder(root, in_order)
        distance = float('inf')
        for i in range(len(in_order)):
            if distance > abs(target - in_order[i]):
                distance = abs(target - in_order[i])
                idx = i
        res = []
        left, right = idx - 1, idx + 1
        for i in range(k):
            res.append(in_order[idx])
            if left >= 0 and right < len(in_order):
                if abs(target - in_order[left]) > abs(target - in_order[right]):
                    idx = right
                    right += 1
                else:
                    idx = left
                    left -= 1
            elif left >= 0:
                idx = left
                left -= 1
            elif right < len(in_order):
                idx = right
                right += 1
        return res

    def inorder(self, root, in_order):
        if not root:
            return
        self.inorder(root.left, in_order)
        in_order.append(root.val)
        self.inorder(root.right, in_order)
        return