class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for a in s:
            if a == '(' or a == '[' or a == '{':
                stack.append(a)
            elif len(stack) == 0:
                return False
            else:
                b = stack.pop()
                if pairs[b] != a:
                    return False
        return (len(stack) == 0)


if __name__ == '__main__':
    s = Solution()
    print(s.isValid(s="()"))
    print(s.isValid(s="()[]{}"))
    print(s.isValid(s="(]"))
    print(s.isValid(s="("))