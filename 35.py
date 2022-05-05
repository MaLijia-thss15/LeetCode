from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left = 0
        right = l - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left



if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert(nums=[1, 3, 5, 6], target=5))
    print(s.searchInsert(nums=[1, 3, 5, 6], target=2))
    print(s.searchInsert(nums=[1, 3, 5, 6], target=7))
