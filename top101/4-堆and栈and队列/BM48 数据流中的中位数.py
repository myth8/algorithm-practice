# -*- coding:utf-8 -*-
import heapq


class Solution:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def Insert(self, num):
        # write code here
        if len(self.max_heap) == len(self.min_heap):
            # 偶数：先入小顶堆，再把小顶堆顶"过继"给大顶堆
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            # 大顶堆多一个：先入大顶堆，再把大顶堆顶"过继"给小顶堆
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def GetMedian(self):
        # write code here
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return -self.max_heap[0] * 1.0
