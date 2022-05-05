class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or len(needle) > len(haystack):
            return -1
        # From the discussion
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr_lazy(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return -1
        return haystack.find(needle)


if __name__ == '__main__':
    s = Solution()
    print(s.strStr(haystack="hello", needle="ll"))
    print(s.strStr(haystack="aaaaa", needle="bba"))
