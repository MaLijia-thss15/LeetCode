from math import log10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        # length of string
        l = int(log10(x)) + 1
        rev_list = []
        for i in range(l):
            digit = int(x % (10 ** (i + 1)) / (10 ** i))
            rev_list.append(digit)
            # y = y + digit * (10 ** (l - i - 1))
        ori_list = rev_list[::-1]
        return (ori_list == rev_list)


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(x=121))
    print(s.isPalindrome(x=1221))
