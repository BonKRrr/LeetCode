# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        pick = self.head.val
        node = self.head.next
        i = 2
        while node is not None:
            if random.randint(0, i - 1) == 0:
                pick = node.val
            i += 1
            node = node.next
        return pick

