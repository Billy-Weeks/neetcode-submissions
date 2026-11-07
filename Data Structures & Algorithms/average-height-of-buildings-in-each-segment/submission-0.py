class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        events = defaultdict(lambda: [0, 0])
        for left, right, height in buildings:
            events[left][0] += height
            events[left][1] += 1
            events[right][0] -= height
            events[right][1] -= 1
        total = count = previous = 0
        answer = []
        for x in sorted(events):
            if count and previous < x:
                height = total // count
                if answer and answer[-1][1] == previous and answer[-1][2] == height:
                    answer[-1][1] = x
                else:
                    answer.append([previous, x, height])
            total += events[x][0]
            count += events[x][1]
            previous = x
        return answer
