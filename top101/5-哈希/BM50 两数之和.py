#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # write code here
        pr = {}
        for i in range(len(numbers)):
            j = pr.get(target - numbers[i])
            if j is not None:
                return [j + 1, i + 1]
            pr[numbers[i]] = i
        return []
