class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        numindex = {}        
        for index, num in enumerate(nums):            
            c = target - num            
            if c in numindex:
                return [numindex[c], index]             
            numindex[num] = index
nums = [3, 4, 5, 6]
target = 7
solution = Solution()
result = solution.twoSum(nums, target)
print(result) 