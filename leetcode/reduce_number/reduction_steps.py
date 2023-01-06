class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            steps += 1
            if num & 1:
                num -= 1
            else:
                num //= 2
        return steps


solution = Solution()
assert solution.numberOfSteps(14) == 6
assert solution.numberOfSteps(8) == 4
assert solution.numberOfSteps(123) == 12
