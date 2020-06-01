# Solution 1: Backtracking

# Time Complexity: O(E + V^2), where E is the number of edges and
# V is the number of vertex.
# Space Complexity: O(E + V)

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = defaultdict(list)
        for nextCourse, preCourse in prerequisites:
            courseDict[preCourse].append(nextCourse)

        path = [False] * numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, path):
                return False
        return True

    def isCyclic(self, currCourse, courseDict, path):
        if path[currCourse]:
            # Come across a previously visited node, i.e. detect the cycle.
            return True

        # Before backtracking, mark the node in the path.
        path[currCourse] = True

        # Backtracking
        res = False
        for nextCourse in courseDict[currCourse]:
            res = self.isCyclic(nextCourse, courseDict, path)
            if res:
                break

        # After backtracking, remove the node from the path.
        path[currCourse] = False
        return res

# Solution 2: Poster DFS

# Time Complexity: O(E + V)
# Space Complexity: O(E + V)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = defaultdict(list)
        for nextCourse, preCourse in prerequisites:
            courseDict[preCourse].append(nextCourse)

        visited = [False] * numCourses
        path = [False] * numCourses

        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, visited, path):
                return False
        return True

    def isCyclic(self, currCourse, courseDict, visited, path):
        if visited[currCourse]:
            return False

        if path[currCourse]:
            return True

        path[currCourse] = True

        res = False
        for nextCourse in courseDict[currCourse]:
            res = self.isCyclic(nextCourse, courseDict, visited, path)
            if res:
                break

        path[currCourse] = False

        visited[currCourse] = True
        return res























