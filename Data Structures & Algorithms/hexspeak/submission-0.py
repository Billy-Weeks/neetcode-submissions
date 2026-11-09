class Solution:
    def toHexspeak(self, num: str) -> str:
        result = format(int(num), 'X').replace('0', 'O').replace('1', 'I')
        return result if all(c in 'ABCDEFIO' for c in result) else 'ERROR'
