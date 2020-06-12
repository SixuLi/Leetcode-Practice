# Solution 1
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            three_sum_res = self.threeSum(nums[i + 1:], target - nums[i])
            if len(three_sum_res) != 0:
                for k in three_sum_res:
                    k.append(nums[i])
                    res.append(k)
        return res

    def threeSum(self, nums, target):
        res = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r:
                        l += 1
                        if nums[l] != nums[l - 1]:
                            break
                    while l < r:
                        r -= 1
                        if nums[r] != nums[r + 1]:
                            break
                elif three_sum < target:
                    l += 1
                else:
                    r -= 1
        return res

# Solution 2: HashTable
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        numLen, res, Dict = len(nums), set(), {}
        if numLen < 4:
            return []
        nums.sort()
        for p in range(numLen-1):
            for q in range(p+1, numLen):
                if nums[p] + nums[q] not in Dict:
                    Dict[nums[p] + nums[q]] = [(p,q)]
                else:
                    Dict[nums[p] + nums[q]].append((p,q))
        for i in range(numLen-1):
            for j in range(i+1, numLen):
                T = target - nums[i] - nums[j]
                if T in Dict:
                    for k in Dict[T]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]