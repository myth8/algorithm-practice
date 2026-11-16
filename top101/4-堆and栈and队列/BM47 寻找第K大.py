#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
import random


class Solution:
    def partition(self, a, l, r):
        idx = random.randint(l, r)
        a[idx], a[l] = a[l], a[idx]
        pivot = a[l]
        i, j = l, r
        while i < j:
            while i < j and a[j] >= pivot:
                j -= 1
            while i < j and a[i] <= pivot:
                i += 1
            a[i], a[j] = a[j], a[i]
        a[l], a[i] = a[i], a[l]
        return i

    # 顺便复习快排
    def quick_sort(self, a, l, r):
        if l >= r:  # 区间 ≤1 个元素，天然有序
            return
        p = self.partition(a, l, r)  # pivot 归位，返回下标 p
        self.quick_sort(a, l, p - 1)  # 递归左半边
        self.quick_sort(a, p + 1, r)  # 递归右半边

    def findKth(self, a: List[int], n: int, K: int) -> int:
        # write code here
        target = n - K
        l, r = 0, n - 1
        while l <= r:
            p = self.partition(a, l, r)
            if p == target:
                return a[p]
            elif p < target:
                l = p + 1
            else:
                r = p - 1
        return -1
