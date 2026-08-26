# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i, j = list1, list2
        current = None

        if i == None and j == None:
            return None
        if i == None:
            return j
        if j == None:
            return i

        if i.val > j.val:
            current = j
            j = j.next
        else:
            current = i
            i = i.next
        head = current

        while i or j:
            if not i:
                current.next = j
                break
            if not j:
                current.next = i
                break

            if i.val < j.val:
                current.next = i
                current = i
                i = i.next
            else:
                current.next = j
                current = j
                j = j.next

        return head




        



        