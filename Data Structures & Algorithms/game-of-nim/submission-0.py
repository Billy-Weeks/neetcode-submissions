class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        value = 0
        for pile in piles:
            value ^= pile
        return value != 0
