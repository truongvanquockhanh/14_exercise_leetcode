#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = [-1]*256
        i = 0
        max_len = 0
        for j in range(len(s)):
            if a[ord(s[j])] >= i:
                i = a[ord(s[j])] + 1
            a[ord(s[j])] = j
            max_len = max(max_len, j -i +1)
        return max_len