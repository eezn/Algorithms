# linkedlist -> queue : pop(0) 할 때 모든 원소를 한 칸씩 이동하는 연산이 필요 없다.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None



# Singly linked list
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # Add new node at the end of the linked list
    def enqueue(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def dequeue(self):
        if self.head == None:
            return -1

        v = self.head.data
        self.head = self.head.next

        if self.head == None:
            self.tail = None
        return v

    # 출력
    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)

if __name__=="__main__":
    s = SinglyLinkedList()
    # 원소 추가
    s.enqueue(Node(1))
    s.enqueue(Node(2))
    s.enqueue(Node(3))
    s.enqueue(Node(4))
    s.print() # 1->2->3->4

    # 원소 삭제
    print(s.dequeue()) # 1
    print(s.dequeue()) # 2
    s.print()
    print(s.dequeue()) # 3
    print(s.dequeue()) # 4