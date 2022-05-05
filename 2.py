from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# For debug
def pylist_to_ListNode(input:List):
    if len(input) == 0:
        return None
    result = ListNode(input[0], None)
    result.next = pylist_to_ListNode(input[1:])
    return result


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, extra: int = 0) -> ListNode:
        result = ListNode(0, None)

        val = l1.val + l2.val + extra
        result.val = val % 10

        # Recursion
        next_extra = val // 10
        if l1.next is None and l2.next is None:
            if next_extra == 0:
                result.next = None
            else:
                result.next =  ListNode(next_extra, None)
        elif l1.next is None:
            new_l1 = ListNode(0, None)
            result.next = self.addTwoNumbers(new_l1, l2.next, next_extra)
        elif l1.next is not None and l2.next is None:
            new_l2 = ListNode(0, None)
            result.next = self.addTwoNumbers(l1.next, new_l2, next_extra)
        else:
            result.next = self.addTwoNumbers(l1.next, l2.next, next_extra)

        return result


if __name__ == '__main__':
    l1 = pylist_to_ListNode([9, 9, 9, 9, 9, 9, 9])
    l2 = pylist_to_ListNode([9, 9, 9, 9])
    s = Solution()
    result = s.addTwoNumbers(l1, l2)

    print("Success.")
