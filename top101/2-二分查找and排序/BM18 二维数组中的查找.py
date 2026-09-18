#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
class Solution:
    def Find(self, target: int, array: List[List[int]]) -> bool:
        # write code here
        m = len(array)
        if m == 0:
            return False
        n = len(array[0])
        i, j = m - 1, 0
        while i >= 0 and j <= n - 1:
            if array[i][j] == target:
                return True
            elif target > array[i][j]:
                j += 1
            else:
                i -= 1

        return False
