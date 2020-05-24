# Solution 1: Brute Force(TLE)

# Time Complexity: O(nk)
# Space Complexity: O(n-k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i:i+k]) for i in range(n-k+1)]

# Solution 2: Deque


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Checking the basic cases
        if n*k == 0:
            return []
        if n == 1:
            return nums

        # Defining Deque and result list
        deq = deque()
        res = []

        # First traversing through K in the nums and only adding maximum value's
        # index to the deque.
        # Now, comparing the new value in the nums with the last index value
        # from deque, and if new value is less, we don't need it.
        # In this way, we always maintain the max value in the current sliding
        # window at the front of the deque.
        for i in range(k):
            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        # Now, we will traverse from k to the end of array and do 4 things
        # 1. Appending left most indexed value to the result
        # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
        # 3. Checking if right most indexed element in deque is less than the new element we encounter,
        # if yes, we will remove it.
        # 4. Append i at the end of the deque.
        for i in range(k, n):
            res.append(nums[deq[0]])
            if deq[0] < i-k+1:
                deq.popleft()
            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        # Adding the maximum for last subsequence
        res.append(nums[deq[0]])
        return res