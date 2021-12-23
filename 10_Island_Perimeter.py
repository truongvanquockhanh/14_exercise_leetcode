#https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        x = len(grid[0])
        y = len(grid)
        for j in range(y):
            for i in range(x):
                if (grid[j][i] == 1):
                    result = result + 4
                    if (i != 0):
                        if (grid[j][i-1] == 1):
                            result = result - 1
                    if (i < x-1):
                        if (grid[j][i+1] == 1):
                            result = result - 1
                    if (j != 0):
                        if (grid[j-1][i] == 1):
                            result = result - 1
                    if (j < y - 1):
                        if (grid[j+1][i] == 1):
                            result = result - 1
        return result