#https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        a = []
        b = [root]
        while b:
            a.append(b)
            b = []
            for x in a[-1]:
                if x.left:
                    b.append(x.left)
                if x.right:
                    b.append(x.right)
        kp = [[x.val for x in y] for y in a]
        return([sum(x)/len(x) for x in kp])