class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        count = Counter(nums)         
        return heapq.nlargest(k,count.keys(),key=count.get)
nums = [1,2,2,3,3,3]
k = 2
solution = Solution()
result = solution.topKFrequent(nums,k)
print(result)