#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
class Solution:
    def solve(self, s: str) -> int:
        # write code here
        num_stack = []
        op_stack = []
        expect_num = True
        pr = {'*': 2, '+': 1, '-': 1}

        def calc():
            op = op_stack.pop()
            y = num_stack.pop()
            x = num_stack.pop()
            z = x * y
            if op == '+': z = x + y
            if op == '-': z = x - y
            num_stack.append(z)

        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
                expect_num = False
                continue
            if c == '(':
                op_stack.append(c)
                i += 1
                expect_num = True
                continue
            if c == ')':
                while op_stack[-1] != '(':
                    calc()
                op_stack.pop()
                i += 1
                expect_num = False
                continue

            if c == '-' and expect_num:
                num_stack.append(0)
                op_stack.append('-')
                i += 1
                continue

            while op_stack and op_stack[-1] != '(' and pr[op_stack[-1]] >= pr[c]:
                calc()
            op_stack.append(c)
            i += 1
            expect_num = True

        while op_stack:
            calc()

        return num_stack[-1]
