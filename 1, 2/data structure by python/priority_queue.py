# PriorityQueue
# Dijkstra, Huffman, Prim 알고리즘 등 다양한 알고리즘에서 활용
# 각 원소에 우선순위 값이 존재, 값이 낮을수록 급하게 처리해야 하는 데이터

# Heapq 모듈 사용

import heapq

class PriorityQueue():
    def __init__(self):
        self.queue = []
        self.count = 0

    def enqueue(self, priority, v):
        self.count += 1
        heapq.heappush(self.queue, (priority, self.count, v))

    def dequeue(self):
        heapq.heappop(self.queue)

    def display(self):
        print(self.queue)


if __name__=="__main__":
    pq = PriorityQueue()
    print(pq.enqueue(1, 'test1'))
    print(pq.enqueue(4, 'test2'))
    print(pq.enqueue(3, 'test3'))
    print(pq.enqueue(1, 'test4'))
    print(pq.enqueue(2, 'test5'))
    print(pq.enqueue(1, 'test6'))
    pq.display()

