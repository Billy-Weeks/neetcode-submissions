class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counts = sorted(collections.Counter(s).values(), reverse=True)
        return sum(count * (i // 9 + 1) for i, count in enumerate(counts))
