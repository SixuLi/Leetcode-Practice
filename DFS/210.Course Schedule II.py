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

# Solution 2: Topological Sort

# Time Complexity: O(E + V)
# Space Complexity: O(E + V)

from collections import Counter, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c = Counter()
        graph = defaultdict(list)
        ready = []
        topo = []

        for nextCourse, preCourse in prerequisites:
            c[nextCourse] += 1
            graph[preCourse].append(nextCourse)

        for u in range(numCourses):
            if c[u] == 0:
                ready.append(u)

        while ready:
            u = ready.pop()
            topo.append(u)
            for v in graph[u]:
                c[v] -= 1
                if c[v] == 0:
                    ready.append(v)

        return topo if len(topo) == numCourses else []












