class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        m = len(set(s))
        longest = 0
        if  m == 1:
            return 1
        if  m == 0:
            return 0
        for i in range(n):
            for j in range(i+1,n+1):
                if len(s[i:j]) == len(set(s[i:j])):
                    val = len(s[i:j])
                    if val > longest:
                        longest = val
                else:
                    break
        return longest


        