#https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return (len(set(candyType)) if len(set(candyType)) <= len(candyType)/2 else int(len(candyType)/2) )