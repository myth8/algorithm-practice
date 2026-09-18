#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # write code here
        """
        如果 nums[mid] < nums[mid+1]，那么右半部分一定存在峰值（因为右边是往上走的，要么继续升到边界，要么在某个点下降形成峰值）。
        反之，左半部分一定存在峰值。
        不是在"直接找峰值"，而是在不断排除"不可能有峰值"的那一半。
        每步都保证"峰值还活着"，保证"峰值还在区间里"，最后活下来的那个位置，只能是峰值。
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l