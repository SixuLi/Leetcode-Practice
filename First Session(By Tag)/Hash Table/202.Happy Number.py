# Solution 1: Hash Set
# If n is a Happy Number, it will eventually get to 1.
# If n is not a Happy Number, it will get stuck in a cycle.
# Therefore, we can use a hash set to store the chain of numbers and detect whether we have entered a cycle.

# Time Complexity: O(logN)
# Space Complexity: O(logN)

class Solution:
    def isHappy(self, n: int) -> bool:
        Dict = set()
        while True:
            tmp = self.sumSquareDigits(n)
            if tmp == 1:
                return True
            if tmp in Dict:
                return False
            else:
                Dict.add(tmp)
            n = tmp

    def sumSquareDigits(self, n):
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total

# Floyd's Cycle-Finding Algorithm
# We use slowRunner and fastRunner in this problem. If there exists a cycle, then the fastRunner will finally
# catch up the slowRunner. And in this way, we do not need to use extra O(logN) space.

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def isHappy(self, n: int) -> bool:
        slowRunner = n
        fastRunner = self.sumSquareDigits(n)
        while fastRunner != 1 and fastRunner != slowRunner:
            slowRunner = self.sumSquareDigits(slowRunner)
            fastRunner = self.sumSquareDigits(self.sumSquareDigits(fastRunner))
        return fastRunner == 1

    def sumSquareDigits(self, n):
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total
























