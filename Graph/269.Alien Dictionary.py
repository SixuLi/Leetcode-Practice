# Solution 1: Topological Sort

# Time Complexity: O(C), where C is the total length of the all the words.
# Space Complexity: O(1), the number of alphabets is fixed.

from collections import defaultdict, Counter, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict(list)
        c = Counter({c: 0 for word in words for c in word})
        queue = deque()
        res = ""

        # Covert the alien dictionary into a directed acyclic graph
        for i in range(n - 1):
            s1, s2 = words[i], words[i + 1]
            Pre, Next, signal = self.compare(s1, s2)
            if not signal:
                return ""

            graph[Pre].append(Next)
            if Pre != Next:
                c[Next] += 1

        # Topological Sort
        for u in c.keys():
            if c[u] == 0:
                queue.append(u)

        while queue:
            u = queue.popleft()
            res += u
            for v in graph[u]:
                c[v] -= 1
                if c[v] == 0:
                    queue.append(v)

        return res if len(c.keys()) == len(res) else ""

    def compare(self, s1, s2):
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                return (s1[i], s2[i], True)
            i += 1
        return (s1[i - 1], s2[i - 1], True) if len(s1) <= len(s2) else (s1[i - 1], s2[i - 1], False)