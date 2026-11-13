class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        seen={};answer=0
        for row in grid:
            ones=[i for i,v in enumerate(row) if v]
            for i in range(len(ones)):
                for j in range(i+1,len(ones)):
                    pair=(ones[i],ones[j]);answer+=seen.get(pair,0);seen[pair]=seen.get(pair,0)+1
        return answer
