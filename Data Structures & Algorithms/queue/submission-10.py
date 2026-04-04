class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)

        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node 
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        new_node.next = first_node
        first_node.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        last_node = self.tail.prev
        
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev

        return last_node.value


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        
        target_node = self.head.next
        target_value = target_node.value

        self.head.next = target_node.next
        target_node.next.prev = self.head

        return target_value 