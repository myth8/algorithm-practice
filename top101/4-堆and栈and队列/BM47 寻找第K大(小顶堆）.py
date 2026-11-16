#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
import heapq


class Solution:
    def findKth(self, a: List[int], n: int, K: int) -> int:
        # write code here
        heap = []
        for x in a:
            if len(heap)<K:
                heapq.heappush(heap,x)
            else:
                if x > heap[0]:
                    heapq.heapreplace(heap,x)
        return heap[0]

