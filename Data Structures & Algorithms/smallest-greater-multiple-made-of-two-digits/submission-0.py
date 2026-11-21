class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        digits = sorted(set([digit1, digit2]))
        queue = [d for d in digits if d != 0]
        for value in queue:
            if value > k and value % k == 0:
                return value
            for digit in digits:
                child = value * 10 + digit
                if child <= 2147483647:
                    queue.append(child)
        return -1
