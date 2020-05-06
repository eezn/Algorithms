# 내부적으로 doublylinkedlist로 구현되어 데이터 처리속도가 O(1)으로 매우 빠름

from collections import deque

# deque 선언
dq - deque([])

# deque에 데이터 추가
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
print(dq) # deque([1, 2, 3, 4])

# deque 첫번째 원소 제거
print(dq.popleft()) # 1
print(dq.popleft()) # 2
print(dq.popleft()) # 3
print(dq.popleft()) # 4
print(dq) # deque([])