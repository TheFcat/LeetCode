class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        list_remain = []
        num = ''
        operator = ['+', '-', '*', '/']
        for c in s:
            if c not in operator:
                num += c
            else:
                list_remain.append(int(num))
                num = ''
                list_remain.append(c)
        list_remain.append(int(num))

        if len(list_remain) == 1:
            return list_remain[0]
        only_plus_minus = [list_remain[0], list_remain[1]]
        for i in range(2, len(list_remain)):
            if only_plus_minus[-1] == '*':
                only_plus_minus.pop()
                only_plus_minus.append(only_plus_minus.pop() * list_remain[i])
            elif only_plus_minus[-1] == r'/':
                only_plus_minus.pop()
                only_plus_minus.append(only_plus_minus.pop() // list_remain[i])
            else:
                only_plus_minus.append(list_remain[i])

        total = only_plus_minus[0]

        for op_index in range(1, len(only_plus_minus), 2):
            if only_plus_minus[op_index] == '+':
                total += only_plus_minus[op_index + 1]
            elif only_plus_minus[op_index] == '-':
                total -= only_plus_minus[op_index + 1]

        return total
print(Solution().calculate('3+5 / 2'))