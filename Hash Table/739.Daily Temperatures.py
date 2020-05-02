# Solution 1: Reversal Traverse
# We know that the interval of temperatures is [30, 100], therefore,
# in the inner loop, traversing all the temperatures is affordable.
# So, we can solve this problem as following:
# In the outer loop, we traverse the original daily temperature
# in reverse mode, and the newest day of every temperature in a Dict.
# And for the current temperature, we use the Dict to find all the position
# that have higher temperature than current one and save the smallest one.
# If no such position exists, save 0.

# Time Complexity: O(MN), where M is the range of temperature,
# and N is the numbers of daily temperature.
# Space Complexity: O(N + M)

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        save = {}
        res = []
        for day in range(len(T)-1, -1, -1):
            temp = T[day]
            save[temp] = day
            large = []
            for i in range(temp+1, 102):
                if i in save:
                    large.append(save[i] - day)
            if large:
                res.append(min(large))
            else:
                res.append(0)
        return res[::-1]

# Solution 2: Stack
# If the stack is empty or the top element is smaller than current element,
# this means that the previous day's temperature is lower than current day's.
# Therefore, we push out the previous day and set the result as the difference
# of current position and previous one.

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0]*n
        stack = []
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                oi = stack.pop()[1]
                res[oi] = i - oi
            stack.append((t, i))
        return res

