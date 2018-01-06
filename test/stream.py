from  heapq import *


class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))

    def findMedian(self):
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (self.large[0] - self.small[0]) / 2.0
