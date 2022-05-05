from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur_pt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if cur_pt != i:
                    nums[cur_pt] = nums[i]
                cur_pt = cur_pt + 1

        return cur_pt


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums=[1, 1, 2], val=1))
    print(s.removeElement(nums=[3, 2, 2, 3], val=3))
    print(s.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))