#https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = None
        for j in range(1,int(len(s)/2)+1):
            a = s[j-1]
            s[j-1] = s[-j]
            s[-j] = a
        