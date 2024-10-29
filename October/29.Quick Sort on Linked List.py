class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

class Res:
    def __init__(self):
        self.new_head = None
        self.new_end = None

class GfG:
    @staticmethod
    def quick_sort(head):
        if head is None:
            return None
        tail = GfG.get_tail(head)
        return GfG.quick_sort_rec(head, tail)

    @staticmethod
    def get_tail(node):
        while node is not None and node.next is not None:
            node = node.next
        return node

    @staticmethod
    def quick_sort_rec(head, last):
        if head is None or head == last:
            return head

        r = Res()
        s = Res()

        pivot = GfG.partition(head, last, r, s)

        if r.new_head != pivot:
            tmp = r.new_head
            while tmp.next != pivot:
                tmp = tmp.next
            tmp.next = None
            r.new_head = GfG.quick_sort_rec(r.new_head, tmp)

            tmp = GfG.get_tail(r.new_head)
            tmp.next = pivot

        pivot.next = GfG.quick_sort_rec(pivot.next, s.new_end)

        return r.new_head

    @staticmethod
    def partition(head, last, r, s):
        pivot = last
        prev = None
        cur = head
        tail = pivot

        while cur != pivot:
            if cur.data < pivot.data:
                if r.new_head is None:
                    r.new_head = cur
                prev = cur
                cur = cur.next
            else:
                if prev is not None:
                    prev.next = cur.next

                tmp = cur.next
                cur.next = None
                tail.next = cur
                tail = cur
                cur = tmp

        if r.new_head is None:
            r.new_head = pivot

        s.new_end = tail

        return pivot
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=' -> ' if current.next else '')
        current = current.next
    print()

if __name__ == "__main__":
    head = Node(4)
    head.next = Node(8)
    head.next.next = Node(8)
    head.next.next.next = Node(3)

    print("Original Linked List:")
    print_linked_list(head)

    sorted_head = GfG.quick_sort(head)

    print("Sorted Linked List:")
    print_linked_list(sorted_head)