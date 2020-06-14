# Solution 1: Sort List by Key

# Time Complexity: O(nlogn), where n is the number of logs
# Space Complexity: O(n)

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []

        for log in logs:
            if log.split(' ')[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: x.split(' ')[0])
        letters.sort(key=lambda x: x.split(' ')[1:])

        return letters + digits