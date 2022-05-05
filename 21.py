# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val <= list2.val:
                result_rec = self.mergeTwoLists(list1.next, list2)
                list1.next = result_rec
                return list1
            else:
                result_rec = self.mergeTwoLists(list1, list2.next)
                list2.next = result_rec
                return list2


if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4]))
    print(s.mergeTwoLists(list1=[], list2=[]))
    print(s.mergeTwoLists(list1=[], list2=[0]))
