class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        seen = [[0] * n for _ in range(m)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        r = c = d = answer = 0
        while not seen[r][c] & (1 << d):
            if seen[r][c] == 0:
                answer += 1
            seen[r][c] |= 1 << d
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and room[nr][nc] == 0:
                r, c = nr, nc
            else:
                d = (d + 1) % 4
        return answer

