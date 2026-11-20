class Solution:
    def findGameWinner(self, n: int) -> bool:
        grundy = [0] * (n + 1)
        grundy[1] = 1
        for order in range(2, n + 1):
            grundy[order] = (grundy[order-2] ^ grundy[order-1]) + 1
        return grundy[n] != 1
