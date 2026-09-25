class LRUCache:

    def __init__(self, capacity: int):
        self.map = defaultdict(LinkedListNode)
        self.llist = LinkedList()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.llist.add(self.llist.remove(node))
        # self.llist.printList()
        return node.val
        

    def put(self, key: int, value: int) -> None:
        node = LinkedListNode(key, value)
        if key in self.map:
            self.llist.remove(self.map[key])
        self.map[key] = node
        self.llist.add(node)
        if len(self.map)>self.cap:
            invalidated_node = self.llist.removeLast()
            del self.map[invalidated_node.key]
        # self.llist.printList()
        
        
class LinkedListNode:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.front = LinkedListNode()
        self.back = LinkedListNode()
        self.front.next = self.back
    
    def add(self, node): # Adds at the front
        temp = self.front.next
        self.front.next = node
        node.next = temp
    
    def remove(self, node): # removes node from its position
        head = self.front.next
        prev, cur = self.front, head
        while cur!=node:
            prev = prev.next
            cur = cur.next
        prev.next = cur.next
        cur.next = None
        return cur
    
    def removeLast(self):
        head = self.front.next
        prev, cur = self.front, head
        # self.printList()
        while cur.next != self.back:
            cur = cur.next
            prev = prev.next
        prev.next = cur.next
        cur.next = None
        return cur
    
    def printList(self):
        cur = self.front
        print("--------")
        print("")
        while cur:
            print("[ ", cur.key, cur.val, "]")
            cur = cur.next    
        print("")
        print("--------")

