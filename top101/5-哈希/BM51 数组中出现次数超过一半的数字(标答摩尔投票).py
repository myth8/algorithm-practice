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
        """
        如果一个数出现次数超过数组长度的一半，那么把它和"其他所有数"两两配对互相抵消，最后一定会剩下它。
        """
        cand, cnt = -1, 0
        for x in numbers:
            if cnt == 0:
                cand = x
                cnt += 1
            elif x == cand:
                cnt += 1
            else:
                cnt -= 1
        return cand if numbers.count(cand) * 2 > len(numbers) else -1 # 验证是否有解
