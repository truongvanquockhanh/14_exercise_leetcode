#https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q=0
        p=0
        if (m*n!=r*c):
            return mat
        if (r == m):
            return mat
        result = []
        for x in range(r):
            result.append([])
            for y in range(c):
                result[x].append(1)
        for j in range(m):
                for i in range(n):
                    if q==c:
                        p += 1
                        q=0
                    result[p][q]=mat[j][i]
                    q += 1
        return result