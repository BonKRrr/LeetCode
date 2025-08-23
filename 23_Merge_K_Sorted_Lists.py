# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for idx, l in enumerate(lists):
            if l is not None:
        
                pq.append((l.val, idx))
        heapq.heapify(pq)
        dummy = ListNode()
        cur = dummy
        while len(pq) > 0:
            _, l_idx = heapq.heappop(pq)
            cur.next = lists[l_idx]
            cur = cur.next
            if cur.next is not None:
                lists[l_idx] = lists[l_idx].next
                heapq.heappush(pq, (cur.next.val, l_idx))
        return dummy.next
