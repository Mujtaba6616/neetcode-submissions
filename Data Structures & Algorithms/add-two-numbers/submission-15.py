# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        if l1==None:
            return l2
        elif l2==None:
            return l1
        dummy=ListNode(0)
        curr=dummy
        while l1!=None and l2!=None:
            if l1.val+l2.val+carry<=9:
                curr.val=l1.val+l2.val+carry
                carry-=carry
                if l1.next!=None or l2.next!=None or carry!=0:
                    curr.next=ListNode(0)
                    curr=curr.next
            else:
                curr.val=(l1.val+l2.val+carry)%10
                carry=(l1.val+l2.val+carry)//10
                if l1.next!=None or l2.next!=None or carry!=0:
                    curr.next=ListNode(0)
                    curr=curr.next
            l1=l1.next
            l2=l2.next
        
        
        while l1!=None:
            
            if l1.val+carry<=9:
                curr.val=l1.val+carry
                carry-=carry
            else:
                curr.next=ListNode(0)
                curr.val=(l1.val+carry)%10
                carry=(l1.val+carry)//10
                curr=curr.next
            l1=l1.next
        while l2!=None:
            if l2.val+carry<=9:
                curr.val=l2.val+carry
                carry-=carry
            else:
                curr.next=ListNode(0)
                curr.val=(l2.val+carry)%10
                carry=(l2.val+carry)//10
                curr=curr.next
            l2=l2.next
        if carry!=0:
            curr.val=carry
        return dummy
            