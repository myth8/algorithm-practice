#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def minNumberDisappeared(self, nums: List[int]) -> int:
        # write code here
        """
        我们希望做到：让数值 x 待在数组下标 x-1 的位置上（即 nums[x-1] == x）。
        把每个在 [1, n] 范围内的数，"归位"到它该在的下标。
        全部归位后，从头扫一遍，第一个 nums[i] != i+1 的下标，答案就是 i+1。
        如果全都对上了，说明 1..n 都齐了，答案就是 n+1。
        这本质上就是用数组自己当哈希表：下标 i 的"桶"里存的值应该是 i+1。不需要额外空间。
        """
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
