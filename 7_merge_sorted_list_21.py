class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

# Create linked lists
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))

# Call the mergeTwoLists function
merged_list = ListNode.mergeTwoLists(list1, list2)

# Print the result
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next

    