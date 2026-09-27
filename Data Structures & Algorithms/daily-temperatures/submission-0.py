class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We need to count the number of days til a greater temp
        # Stack for max temp?

        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res              