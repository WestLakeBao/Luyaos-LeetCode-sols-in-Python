# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
import heapq
from heapq import *

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])
        return heappop(min_heap)
