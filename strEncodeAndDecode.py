class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
strs = ["neet", "code", "love", "you"]
solution = Solution()
encoded = solution.encode(strs)
print(encoded)  
decoded = solution.decode(encoded)
print(decoded)  