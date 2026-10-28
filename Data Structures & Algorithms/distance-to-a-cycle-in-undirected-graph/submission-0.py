class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        degree = list(map(len, adj))
        leaves = deque(i for i in range(n) if degree[i] == 1)
        while leaves:
            node = leaves.popleft()
            degree[node] = 0
            for other in adj[node]:
                if degree[other] > 0:
                    degree[other] -= 1
                    if degree[other] == 1:
                        leaves.append(other)
        distance = [-1] * n
        queue = deque()
        for i in range(n):
            if degree[i] > 0:
                distance[i] = 0
                queue.append(i)
        while queue:
            node = queue.popleft()
            for other in adj[node]:
                if distance[other] < 0:
                    distance[other] = distance[node] + 1
                    queue.append(other)
        return distance
