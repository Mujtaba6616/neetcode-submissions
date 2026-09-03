# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1=list1
        t2=list2
        if t1==None:
            return t2
        elif t2==None:
            return t1
        
        if t1.val<=t2.val:
            head=t1
            t1=t1.next
        else:
            head=t2
            t2=t2.next
        ind=head
        
        while t1!=None and t2!=None:
            if t1.val<t2.val:
                ind.next=t1
                ind=t1
                t1=t1.next
            else:
                ind.next=t2
                ind=t2
                t2=t2.next
        while t1!=None:
            ind.next=t1
            ind=t1
            t1=t1.next
        while t2!=None:
            ind.next=t2
            ind=t2
            t2=t2.next
        return head
            
            
