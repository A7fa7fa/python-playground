from random import randint
from heap import MaxHeap

testList = {randint(1, 10000) for _ in range(500)}
heap = MaxHeap(initValues=list(testList))

print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
