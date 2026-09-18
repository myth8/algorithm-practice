#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def minNumberInRotateArray(self, nums: List[int]) -> int:
        # write code here
        l = 0
        r = len(nums) - 1
        """
        每个分支要么 l 右移，要么 r 左移，区间长度严格减小。
        且每个分支都保证"最小值仍在 [l, r] 里"（这是不变量）。
        区间长度是有限正整数，不断减小，最终必然到 1，即 l == r。
        此时区间 [l, l] 里唯一的位置，就是那个从头到尾没被丢掉的最小值。
        """
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1

        return nums[l]
