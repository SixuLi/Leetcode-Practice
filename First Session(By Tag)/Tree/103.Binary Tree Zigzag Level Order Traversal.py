# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1:
# Similar to problem 102, but here when doing level order traverse, we need to record which
# line should reverse after traverse.

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        sign = 1
        while queue:
            level = []
            for i in range(len(queue)):
                p = queue.pop(0)
                level.append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            level.append(sign)
            sign *= -1
            res.append(level)
        for i in range(len(res)):
            if res[i][-1] == -1:
                res[i].pop()
                res[i].reverse()
            else:
                res[i].pop()
        return res