# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None:
            return 
        s,f=head,head
        while f!=None and f.next!=None:
            s=s.next
            f=f.next.next

        second=s.next
        s.next=None
        
        prev=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        
        first,second=head,prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
        