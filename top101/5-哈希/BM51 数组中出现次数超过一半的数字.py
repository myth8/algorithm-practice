#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self, numbers: List[int]) -> int:
        # write code here
        n = len(numbers)
        pr = {}
        for x in numbers:
            pr[x] = pr.get(x, 0) + 1
            if pr[x] * 2 > n:
                return x
        return -1
