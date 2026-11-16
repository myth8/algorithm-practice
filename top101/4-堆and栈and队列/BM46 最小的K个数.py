#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        # write code here
        import heapq
        if k <= 0 or k > len(input):
            return []

        # python 只有小顶堆，存相反数，作为大顶堆用
        max_heap = []

        for x in input:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -x)
            else:
                if -x > max_heap[0]:
                    heapq.heapreplace(max_heap, -x)

        return sorted(-x for x in max_heap)
