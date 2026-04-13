class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int( "".join(map(str,digits)))
        digit = digits + 1
        result = list(map(int, str(digit)))
        return result
        
        