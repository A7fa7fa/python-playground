from typing import List


class MaxHeap():
    def __init__(self, initValues: List[int] | None = None) -> None:
        self.heap = [0]
        if initValues is not None:
            for v in initValues:
                self.push(v)

    def push(self, value: int) -> None:
        # append new value to end of list
        self.heap.append(value)
        # call floatUp with index of added value
        self.__floatUp(self.__getLastIndex())

    def peek(self) -> int | None:
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def pop(self) -> int | None:
        # if list is empty there is no item to return
        if len(self.heap) < 2:
            return None
        # if list has only one item no need to rearange. hust pop and return the item
        if len(self.heap) == 2:
            return self.heap.pop()

        self.__swap(1, self.__getLastIndex())
        head = self.heap.pop()
        self.__floatDown(1)
        return head

    def __floatDown(self, index: int) -> None:
        iLeft = self.__getIndexLeftChild(index)
        iRight = self.__getIndexRightChild(index)
        iLargest = index

        if self.__getLastIndex() > iLeft and self.heap[iLargest] < self.heap[iLeft]:
            iLargest = iLeft
        if self.__getLastIndex() > iRight and self.heap[iLargest] < self.heap[iRight]:
            iLargest = iRight
        if iLargest != index:
            self.__swap(index, iLargest)
            self.__floatDown(iLargest)

    def __getIndexLeftChild(self, index: int) -> int:
        return index * 2

    def __getIndexRightChild(self, index: int) -> int:
        return self.__getIndexLeftChild(index) + 1

    def __floatUp(self, index: int) -> None:
        # if len of smaller or equal than 1 there is only 1 item.
        if len(self.heap) <= 1:
            return
        if self.__parentIndex(index) == 0:
            return

        if self.__getParent(index) < self.heap[index]:
            self.__swap(index, self.__parentIndex(index))
            self.__floatUp(self.__parentIndex(index))
            return

    def __swap(self, n: int, m: int) -> None:
        self.heap[n], self.heap[m] = self.heap[m], self.heap[n]

    def __getParent(self, index: int) -> int:
        return self.heap[self.__parentIndex(index)]

    def __parentIndex(self, index: int) -> int:
        return index // 2

    def __getLastIndex(self) -> int:
        return len(self.heap) - 1

    def __str__(self) -> str:
        '''returns entry of table as string'''
        res = str(self.heap)
        res += "\n"
        for index, v in enumerate(self.heap[1:]):
            iLeft = self.__getIndexLeftChild(index + 1)
            iRigth = self.__getIndexRightChild(index + 1)
            left = 0
            right = 0
            if self.__getLastIndex() > iLeft:
                left = self.heap[iLeft]
            if self.__getLastIndex() > iRigth:
                right = self.heap[iRigth]
            res += f"{'ERROR! ' if left > v or right > v else ''}{v} -> ({left}, {right})\n"
        return res
