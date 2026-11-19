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
        for i in range(n - 2):
            if i > 0 and num[i] == num[i - 1]:  # 外部去重
                continue
            if num[i] > 0: break  # 剪枝：升序，最小值如果大于0，三元组之和必定大于0
            l, r = i + 1, n - 1
            while l < r:
                s = num[i] + num[l] + num[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([num[i], num[l], num[r]])
                    # 去重
                    while l < r and num[l + 1] == num[l]:
                        l += 1
                    while l < r and num[r - 1] == num[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans
