class ListNode:
    next = None
    val = None

    def __init__(self, v):
        self.val = v

class Set:
    head = None
    size = 0

    def add(self, e):
        raise(NotImplementedError)

    def remove(self, e):
        raise(NotImplementedError)
    
    def contains(self, e):
        raise(NotImplementedError)
    
    def isEmpty(self):
        raise(NotImplementedError)



if __name__ == "__main__":
    print("Hello World")
    my_set = Set()
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)

    print("contains 2?", my_set.contains(2))
    print("size", my_set.size)
    my_set.remove(2)
    print("contains 2?", my_set.contains(2))
    print("size", my_set.size)
    