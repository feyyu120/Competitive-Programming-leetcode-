class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cp = ""
        small = min(strs,key=len)
        n = len(small)
        for i in range(n):
            if all(el[i] == strs[0][i] for el in strs):
                cp += strs[0][i]
            else:
                break
        return cp
        