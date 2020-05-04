# CircularQueue
# linkedlist를 이용하지 않고 list를 이용하여 이동이 필요없는 Queue를 구현
# 주어진 공간을 활용 / 쓰이지 않는 메모리가 낭비될 수 있음 / 크기 조정이 어려움

class CircularQueue():

    def __init__(self, max=5):
        self.max = max
        self.queue = [None]*self.max
        self.size = self.front = 0
        self.rear = None

    def is_empty(self):
        return self.size == 0

    def is_full(self):

        if self.rear == None:
            return False
        return self.next_index(self.rear) == self.front

    def next_index(self, idx):
        return (idx + 1) % self.max

    def enqueue(self, data):
        if self.is_full():
            raise Exception("Queue is Full")

        # 시작 index를 0으로 한다.
        if self.rear == None:
            self.rear = 0
        else:
            self.rear = self.next_index(self.rear)

        self.queue[self.rear] = data
        self.size += 1
        return self.queue[self.rear]

    def deque(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.queue[self.front] = None
        self.front = self.next_index(self.front)
        return self.queue[self.front]

    def display(self):
        print(self.queue)


if __name__=="__main__":
    cq = CircularQueue()
    cq.display() # [None, None, None, None, None]
    print(cq.enqueue(1))
    print(cq.enqueue(2))
    print(cq.enqueue(3))
    print(cq.enqueue(4))
    cq.display() # [1, 2, 3, 4, None]
    print(cq.deque())
    print(cq.deque())
    cq.display() # [None, None, 3, 4, None]
    print(cq.enqueue(5))
    print(cq.enqueue(6))
    cq.display()