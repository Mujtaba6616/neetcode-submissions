class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        temp=head

        while temp!= None:
            length+=1
            temp=temp.next

        ind=length-n

        if ind==0:
            return head.next

        d=head

        for i in range(ind-1):
            d=d.next

        s=None
        if d.next.next!=None:
            s=d.next.next

        d.next=s

        return head