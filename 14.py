from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min({len(s) for s in strs})
        result = ""
        for i in range(l):
            first_flag = True
            success_flag = True
            c = ''
            for s in strs:
                if first_flag is True:
                    c = s[i]
                    first_flag = False
                else:
                    if s[i] != c:
                        success_flag = False
                        break
            if success_flag is False:
                break
            else:
                result = result + c

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(strs=["flower","flow","flight"]))
    print(s.longestCommonPrefix(strs=["dog","racecar","car"]))
