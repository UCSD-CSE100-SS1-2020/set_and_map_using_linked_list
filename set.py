class ListNode:
    next = None
    val = None

    def __init__(self, v):
        self.val = v

class Set:
    head = None
    size = 0

    def __init__(self, h=None):
        if h:
            self.head = ListNode(h)
            self.size += 1

    def add(self, e):
        if not self.contains(e):
            temp = self.head
            self.head = ListNode(e)
            self.head.next = temp
            self.size += 1
    
    def remove(self, e):
        prev = None
        curr = self.head
        while curr:
            if curr.val == e:
                if not prev:
                    if self.head:
                        self.head = self.head.next
                else:
                    prev.next = curr.next

                self.size -= 1
                return

            prev = curr
            curr = curr.next
    
    def contains(self, e):
        curr = self.head
        while curr:
            if curr.val == e:
                return True

            curr = curr.next

        return False
    
    def isEmpty(self):
        return self.size == 0



if __name__ == "__main__":
    print("Hello World")
    my_set = Set(1)
    my_set.add(2)
    my_set.add(3)

    print("contains 2?", my_set.contains(2))
    print("size", my_set.size)
    my_set.remove(2)
    print("contains 2?", my_set.contains(2))
    print("size", my_set.size)
    