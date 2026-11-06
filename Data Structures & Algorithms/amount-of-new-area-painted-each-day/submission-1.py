class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        parent = list(range(max(end for _, end in paint) + 1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        answer = []
        for start, end in paint:
            x = find(start)
            count = 0
            while x < end:
                count += 1
                parent[x] = find(x + 1)
                x = parent[x]
            answer.append(count)
        return answer

