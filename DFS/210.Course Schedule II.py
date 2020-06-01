# Solution 1: Postorder DFS

# Time Complexity: O(E + V)
# Space Complexity: O(E + V)

from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseDict = defaultdict(list)
        for nextCourse, preCourse in prerequisites:
            courseDict[preCourse].append(nextCourse)

        visited = [False] * numCourses
        path = [False] * numCourses

        self.res = []

        for currCourse in range(numCourses):
            if self.dfs(currCourse, courseDict, visited, path):
                return []
        return self.res[::-1]

    def dfs(self, currCourse, courseDict, visited, path):
        if visited[currCourse]:
            return False

        if path[currCourse]:
            return True

        path[currCourse] = True
        res = False
        for nextCourse in courseDict[currCourse]:
            res = self.dfs(nextCourse, courseDict, visited, path)
            if res:
                break
        self.res.append(currCourse)
        path[currCourse] = False
        visited[currCourse] = True
        return res