class ListNode:
    next = None
    key = None
    val = None

    def __init__(self, k, v):
        self.key = k
        self.val = v

class Map:
    head = None
    size = 0

    # Put(k, v) Adds value v under key k in the map
    def put(self, k, v):
        raise(NotImplementedError)

    # Remove(k) Removes key k and its corresponding value from the map (if present)
    def remove(self, k):
        raise(NotImplementedError)

    # Get(k) Returns the value that key k maps to
    def get(self, k):
        raise(NotImplementedError)

    def __get_node(self, k):
        raise(NotImplementedError)

    # isEmpty( ) Returns True if the map is empty
    def isEmpty(self):
        raise(NotImplementedError)




if __name__ == "__main__":
    print("Hello World")
    my_map = Map()
    print("empty?", my_map.isEmpty())
    my_map.put("US", "USD")
    my_map.put("JP", "JPY")
    my_map.put("NL", "NLG")
    my_map.put("FR", "FRF")
    print("empty?", my_map.isEmpty())
    print("size", my_map.size)
    print("Dutch currency pre-01-2002:", my_map.get("NL"))

    # Year 2002 rolls along
    my_map.put("NL", "EUR")
    my_map.put("FR", "EUR")
    print("size after introducing the euro:", my_map.size)
    print("Dutch currency post-01-2002:", my_map.get("NL"))

    my_map.remove("US")
    print("size after removing US:", my_map.size)
