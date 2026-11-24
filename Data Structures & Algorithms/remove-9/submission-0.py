class Solution:
    def newInteger(self, n: int) -> int:
        answer=0;place=1
        while n:
            answer+=(n%9)*place
            n//=9;place*=10
        return answer
