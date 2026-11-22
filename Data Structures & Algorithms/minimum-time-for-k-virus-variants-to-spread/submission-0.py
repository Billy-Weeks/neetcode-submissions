class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        answer = 200
        for x in range(min(p[0] for p in points), max(p[0] for p in points)+1):
            for y in range(min(p[1] for p in points), max(p[1] for p in points)+1):
                distances = sorted(abs(x-px)+abs(y-py) for px, py in points)
                answer = min(answer, distances[k-1])
        return answer
