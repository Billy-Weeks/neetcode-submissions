class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        freq = Counter(nums)
        answer = 0
        for a in freq:
            for b in freq:
                for c in freq:
                    total = a + b + c
                    if (total % a == 0) + (total % b == 0) + (total % c == 0) == 1:
                        answer += freq[a] * (freq[b] - (a == b)) * (freq[c] - (a == c) - (b == c))
        return answer

