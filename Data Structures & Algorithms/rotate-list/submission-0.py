class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        k %= length
        if k == 0:
            return head

        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        newHead = curr.next
        curr.next = None

        tail = newHead
        while tail.next:
            tail = tail.next

        tail.next = head

        return newHead
        