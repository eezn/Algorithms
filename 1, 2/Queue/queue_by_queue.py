# Queue 모듈은 Queue, PriorityQueue, LIFO_Queue(Stack)을 제공

import queue

# Queue 선언
q = queue.Queue()

# q에 데이터 추가
q.put(1)
q.put(2)
q.put(3)
q.put(4)

# q에서 첫번째 원소 제거
print(q.get()) # 1
print(q.get()) # 2
print(q.get()) # 3
print(q.get()) # 4

from collections import deque

class Queue(deque):

    def enqueue(self, x):
        super().append(x)

    def dequeue(self):
        super().popleft()

    def display(self):
        for node in self.__iter__():
            print(node)