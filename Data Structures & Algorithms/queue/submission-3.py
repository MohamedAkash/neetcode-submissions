class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        cur = self.head

        while cur.next != self.tail:
            cur = cur.next
        
        new_node = Node(value)
        new_node.next = self.tail
        cur.next = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)

        new_node.next = self.head.next
        self.head.next = new_node


    def pop(self) -> int:
        if self.isEmpty():
            return -1

        cur = self.head

        while cur.next != self.tail:
            prev = cur
            cur = cur.next
        
        prev.next = self.tail
        return cur.val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        pop_val = self.head.next.val
        self.head.next = self.head.next.next

        return pop_val
        
