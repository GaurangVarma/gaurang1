class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        streak = 0
        for num in s:
            if num - 1 not in s: 
                n = num
                current_streak = 1
                while n + 1 in s:
                    n += 1
                    current_streak += 1 
                streak = max(streak, current_streak)
        return streak
nums = [2, 20, 4, 10, 3, 4, 5]
solution = Solution()
result = solution.longestConsecutive(nums)
print(result)  