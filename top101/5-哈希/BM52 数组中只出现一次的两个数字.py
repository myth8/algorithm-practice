#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self, nums: List[int]) -> List[int]:
        # write code here
        """
        先全异或得 a^b，取 a^b 最低位的 1 作为分水岭，把 a 和 b 分到两边；各自异或，两边分别剩下 a 和 b。
        """
        xorres = 0
        for x in nums:
            xorres ^= x
        groupnum = xorres & (-xorres)
        a, b = 0, 0
        for x in nums:
            if x & groupnum == 0: # & 的优先级高于 ==
                a ^= x
            else:
                b ^= x
        return [a, b] if a < b else [b, a]
