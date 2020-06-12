# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS(preorder traversal)

# Time Complexity: O(N)
# Space Complexity: O(N)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper_s(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = helper_s(root.left, string)
                string = helper_s(root.right, string)
            return string

        return helper_s(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper_d(l):
            if l:
                if l[0] == 'None':
                    l.pop(0)
                    return None
                root = TreeNode(l[0])
                l.pop(0)
                root.left = helper_d(l)
                root.right = helper_d(l)
                return root

        data_list = data.split(',')
        root = helper_d(data_list)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Solution 2: BFS with Stack

# Time Complexity: O(N)
# Space Complexity: O(N)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        stack = [root]
        res = ''
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                if not node:
                    res += 'None,'
                else:
                    res += str(node.val) + ','
                    stack.append(node.left)
                    stack.append(node.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(ls[0])
        stack = [root]
        i = 1
        while stack and i < len(ls):
            node = stack.pop(0)
            if ls[i] != 'None':
                left = TreeNode(ls[i])
                node.left = left
                stack.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(ls[i])
                node.right = right
                stack.append(right)
            i += 1
        return root


