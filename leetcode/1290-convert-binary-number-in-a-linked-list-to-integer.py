# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
            TC: O(N)
            SC: O(N)
        """
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next

        return int(''.join(map(str, values)), 2)

    def getDecimalValue(self, head: ListNode) -> int:
        """
            TC: O(N)
            SC: O(1)
        """
        cur = head
        ans = 0
        while cur:
            ans = 2 * ans + cur.val
            cur = cur.next
        return ans

    def getDecimalValue(self, head: ListNode) -> int:
        """
            TC: O(N)
            SC: O(1)
        """
        ans = head.val
        while head.next:
            ans = (ans << 1) | head.next.val
            head = head.next
        return ans


