# Solution 1: Categorize by Sorted String
# Two strings are anagrams if and only if their
# sorted strings are equal.

# Time Complexity: O(NKlogK), where N is the length of strs,
# and K is the maximum length of a string in strs.
# Space Complexity: O(NK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = dict()
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in Dict:
                Dict[sorted_str].append(string)
            else:
                Dict[sorted_str] = [string]
        return Dict.values()

# Solution 2: Categorize by Count
# Two strings are anagrams if and only if their character counts(
# respective number of occurences of each character) are the same.

# Time Complexity: O(NK)
# Space Complexity: O(NK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = dict()
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in Dict:
                Dict[tuple(count)].append(s)
            else:
                Dict[tuple(count)] = [s]
        return Dict.values()














