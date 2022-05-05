from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_v = -101
        cur_pt = 0
        for i in range(len(nums)):
            cur_v = nums[i]
            if last_v != cur_v:
                if cur_pt != i:
                    nums[cur_pt] = cur_v
                cur_pt = cur_pt + 1
                last_v = cur_v
        return cur_pt


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates(nums=[1, 1, 2]))
    print(s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(s.removeDuplicates(nums=[1, 2, 4, 5, 5, 6, 6, 10]))
