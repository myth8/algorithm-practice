#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s: str) -> bool:
        # write code here
        stack = []
        pairs = {')':'(',']':'[','}':'{'};
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                # 就近匹配
                if not stack or stack[-1]!=pairs[c]:
                    return False
                stack.pop()

        return not stack
