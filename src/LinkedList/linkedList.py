from node import Node

class LinkedList():

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def printList(self) -> None:
        temp: Node | None = self.head
        idx: int = 0
        while temp is not None:
            print(idx, temp.value)
            temp = temp.next
            idx += 1
        if self.head is None:
            print("list empty")

    def append(self, value: int) -> Node:
        newNode = Node(value)
        # list is empty so new node is tail and head
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return newNode

        # list has just one entry. Node is tail and head
        # so new node becomes new tail
        if self.head == self.tail:
            self.head.next = newNode
            self.tail = newNode
            return newNode

        # list is not empty and longer than one
        # set next node of tail to new node
        # set tail to new node
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        return newNode

    def pop(self) -> Node | None:
        # if list is empty return None
        if self.head is None:
            return None

        # is list has just one entry return entry
        # set tail and head to none
        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None

        pre: Node  = self.head # type: ignore
        temp: Node  = self.head # type: ignore
        # as long as next of temp is not none end is not reached
        # pre is set to temp and temp to next of temp so pre is always node in before temp
        while temp.next is not None:
            pre = temp
            temp = temp.next

        # pre is second to last so is new tail
        # tail is last so next is set to none
        self.tail = pre
        self.tail.next = None
        return temp

    def prepend(self, value: int)  -> Node:

        newNode = Node(value)

        # if list is empty set head and tail to new Node
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return self.head

        # else just set next of ne Node to head
        # set head to new node
        newNode.next = self.head
        self.head = newNode
        return self.head

    def insert(self, position: int, value: int) -> Node:
        if position < 0:
            raise IndexError("index out of range")

        if self.head is None:
            raise IndexError("index out of range - list is empty")

        if position == 0:
            return self.prepend(value)

        newNode = Node(value)
        counter: int = 0
        pre: Node = self.head
        temp: Node = self.head
        while counter < position:
            if temp.next is None:
                raise IndexError("index out of range")
            pre = temp
            temp = temp.next
            counter += 1

        newNode.next = temp
        pre.next = newNode
        if temp.next is None:
            self.tail = newNode

        return newNode

    def remove(self, position: int) -> Node:
        if position < 0:
            raise IndexError("index out of range")

        if self.head is None:
            raise IndexError("index out of range - list is empty")

        if self.head == self.tail and position == 0:
            temp = self.head
            self.head = None
            self.tail = None
            return temp

        if position == 0:
            removedNode = self.head
            self.head = self.head.next
            return removedNode

        counter: int = 0
        pre: Node = self.head
        temp: Node = self.head
        while counter < position:
            if temp.next is None:
                raise IndexError("index out of range")
            pre = temp
            temp = temp.next
            counter += 1

        removedNode = temp
        pre.next = temp.next
        if temp.next is None:
            self.tail = pre

        return removedNode

    def prev(self, prev: Node, temp: Node) -> Node:
        # as long as end of list not reached recursive call this method again
        if temp.next is not None:
            self.prev(temp, temp.next)

        # if temp.next is None end of list is reached
        # end of list becomes new head
        if temp.next is None:
            self.head = temp

        # previouse node becomes next node
        temp.next = prev
        # return next node
        return temp.next


    def reverse(self) -> None:
        # list is empty so no reversal needed
        if self.head is None:
            return
        # list has length of 1 so no reversal needed
        if self.head == self.tail:
            return

        prev: Node = self.head
        temp: Node = self.head
        # recurse
        self.tail = self.prev(prev, temp)
        self.tail.next = None
