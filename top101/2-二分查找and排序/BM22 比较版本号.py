#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 比较版本号
# @param version1 string字符串
# @param version2 string字符串
# @return int整型
#
class Solution:
    def compare(self, version1: str, version2: str) -> int:
        # write code here
        m, n = len(version1), len(version2)
        i, j = 0, 0
        while i < m or j < n:
            num1 = 0
            while i < m and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i+=1

            num2 = 0
            while j < n and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j+=1

            if num1 < num2:
                return -1
            if num1 > num2:
                return 1

            # 跳过.
            if i < m:
                i += 1
            if j < n:
                j += 1

        return 0
