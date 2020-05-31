# Solution 1: Two pass Solution
# In the first pass, we calculate the max depth of given nested list.
# And in the second pass, we use the same strategy in Question 339 to calculate the total sum.

# Time Complexity: O(n), where n is the number of integers in the nested list.
# Space Complexity: O(logd), where d is the max depth of nested list.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.total = 0
        self.max_depth = self.getDepth(nestedList)
        self.helper(nestedList, 1)
        return self.total

    def getDepth(self, nestedList):
        max_depth = 1
        for List in nestedList:
            if not List.isInteger():
                max_depth = max(max_depth, 1 + self.getDepth(List.getList()))
        return max_depth

    def helper(self, nestedList, level):
        for List in nestedList:
            if List.isInteger():
                self.total += List.getInteger() * (self.max_depth - level + 1)
            else:
                self.helper(List.getList(), level + 1)
