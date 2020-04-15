import heapq

# heapq.heapify()
list1 = [4, 6, 8 ,1]
print(list1)
heapq.heapify(list1)
print(list1)
print()

# heapq.heappush(heap, item)
h = []
heapq.heappush(h, (1, 'food'))
heapq.heappush(h, (2, 'have fun'))
heapq.heappush(h, (3, 'work'))
heapq.heappush(h, (4, 'study'))
print(h)
print()

# heapq.heappop(heap) : 가장 작은 항목을 제거하고 반환
print(heapq.heappop(list1))
print(list1)
print()

# heapq.heappushpop(heap, item) : 새 항목을 힙에 추가한 후, 가장 작은 항목을 제거하고 반환
# heapq.heapreplace(heap, item) : 가장 작은 항목을 제거하고 반환한 후, 새 항목을 추가
# heappush(), heappop() 따로 쓰는 것 보다 상황에 따라 heappushpop(), heapreplace()를 사용하면 효율적

for x in heapq.merge([1, 3, 5], [2, 4, 6]):
    print(x)
