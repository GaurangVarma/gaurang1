class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        anagrams = defaultdict(list)        
        for s in strs:            
            sorted_str = ''.join(sorted(s))            
            anagrams[sorted_str].append(s)        
        return list(anagrams.values())
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
solution = Solution()
result = solution.groupAnagrams(strs)
print(result) 