#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#


class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        # write code here
        n = len(num)
        num.sort()
        ans = []
        for i in range(n - 1):
            if i > 0 and num[i] == num[i - 1]:  # 外部去重
                continue
            if num[i] > 0: break  # 剪枝：升序，最小值如果大于0，三元组之和必定大于0
            target = -num[i]
            seen = set()
            j = i + 1
            while j < n:  # j 是第三个 所以可以遍历到
                need = target - num[j]
                if need in seen:
                    ans.append([num[i], need, num[j]])
                    # 内部去重
                    while j + 1 < n and num[j + 1] == num[j]:
                        j += 1
                else:
                    seen.add(num[j])
                j += 1
            ans.sort()
        return ans
