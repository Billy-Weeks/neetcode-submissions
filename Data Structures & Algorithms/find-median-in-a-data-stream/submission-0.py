class MedianFinder:

    def __init__(self):
        # initialize 2 heaps for each object
        self.small = [] # small is a max-heap and stores smaller half of numbers 
        self.large = [] # large is a min-heap and stores larger half of numbers
        
    def addNum(self, num: int) -> None:
        # Push to max-heap (i.e. small)
        # Push -num because built in heapq is min-heap by defualt (so inverted)
        heapq.heappush(self.small, -num)

        # Step1: Ensure each element in small is less than/equal to each element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small) # remove from small heap
            heapq.heappush(self.large, val) # add to large
        
        # Step2: Balance sizes, allowing one heap to be larger by at most 1 element
        # If small is too big, move bax of small to large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # If large is too big, move the min of large to small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If the lengths are uneven, the median is the root of the larger heap
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])

        # If lengths are even, the median is the average of the two roots
        return (-self.small[0] + self.large[0]) / 2.0
        
        