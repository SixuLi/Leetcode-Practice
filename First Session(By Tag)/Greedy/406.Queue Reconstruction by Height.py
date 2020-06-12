# Solution 1: Greedy
# k is only determined by people with equal or larger height, so makes sense to
# insert in non-increasing order of height. Because when we insert some person
# with height h and count k, we know that we have found its correct position relative
# to people with equal and larger height. And when we later insert other people with
# equal or smaller height, we know that it will not affect this relative position.
# So can deal with people in the descending height.

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

