class LinkedListZipListManagerClass:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert_item(self, item):
        #Inserts an item at the front of the linked list.
        new_node = self.Node(item)
        new_node.next = self.head
        self.head = new_node

    def print_items(self):
        #Prints all items in the linked list.
        current = self.head
        while current:
            print(f"{current.data}", end=" -> " if current.next else "\n")
            current = current.next

    def get_last_node(self):
    #Returns the last node in the linked list.
        current = self.head
        while current and current.next:
            current = current.next
        return current

    def quick_sort_helper(self, start, end):
        if start is None or start == end or start == end.next:
            return

        pivot_prev = self.partition(start, end)
        self.quick_sort_helper(start, pivot_prev)

        if pivot_prev is not None and pivot_prev == start:
            self.quick_sort_helper(pivot_prev.next, end)
        elif pivot_prev is not None and pivot_prev.next is not None:
            self.quick_sort_helper(pivot_prev.next.next, end)

    def partition(self, start, end):
#Partition the linked list for quick sort.
        if start == end or start is None or end is None:
            return start

        pivot_prev = start
        curr = start
        pivot = end.data

        while start != end:
            if start.data < pivot:
                pivot_prev = curr
                curr.data, start.data = start.data, curr.data
                curr = curr.next
            start = start.next

        curr.data, end.data = end.data, curr.data

        return pivot_prev

    def quick_sort(self):
#Public method to sort the linked list using QuickSort.
        last_node = self.get_last_node()
        self.quick_sort_helper(self.head, last_node)
