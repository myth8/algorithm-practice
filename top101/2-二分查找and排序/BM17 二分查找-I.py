#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # write code here
        r = len(nums)
        if r < 1:
            return -1
        l = 0
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid + 1

        return -1
