#https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        total = 0
        for x in ops:
            if(x == "C"):
               result.pop()
            elif ( x == "D"):
                result.append(result[-1]*2)
            elif ( x == "+"):
                result.append(result[-1]+result[-2])
            else:
                result.append(int(x))
                
        for y in result:
            total = total + y
        return total
                