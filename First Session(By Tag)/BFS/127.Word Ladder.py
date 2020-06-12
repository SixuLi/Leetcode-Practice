# Solution 1: BFS

# Time Complexity: O(m^2 * n), where m is the length of each word,
# and n is the length of wordList.
# Space Complexity: O(m^2 * n)

from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        L = len(beginWord)

        all_combin_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combin_dict[word[:i] + "*" + word[i + 1:]].append(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = {beginWord: True}

        while queue:
            cur_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = cur_word[:i] + "*" + cur_word[i + 1:]

                for word in all_combin_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        queue.append((word, level + 1))
                all_combin_dict[intermediate_word] = []
        return 0
