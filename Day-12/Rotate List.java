class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // Handle base cases
        if (head == null || head.next == null || k == 0) {
            return head;
        }
        
        // Step 1: Calculate the length and find the old tail
        ListNode tail = head;
        int length = 1;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }
        
        // Step 2: Minimize rotations using modulo
        k = k % length;
        if (k == 0) {
            return head;
        }
        
        // Step 3: Connect tail to head to make it circular
        tail.next = head;
        
        // Step 4: Find the new tail position
        // The new tail is at (length - k) steps from the current head
        int stepsToNewTail = length - k;
        ListNode newTail = head;
        for (int i = 1; i < stepsToNewTail; i++) {
            newTail = newTail.next;
        }
        
        // Step 5: Break the ring and set the new head
        ListNode newHead = newTail.next;
        newTail.next = null;
        
        return newHead;
    }
}
