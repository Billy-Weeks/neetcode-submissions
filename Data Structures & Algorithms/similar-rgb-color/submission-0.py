class Solution:
    def similarRGB(self, color: str) -> str:
        digits = "0123456789abcdef"
        return "#" + "".join(digits[(int(color[i:i+2],16)+8)//17]*2 for i in (1,3,5))
