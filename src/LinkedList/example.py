from linkedList import LinkedList


myLinkedList = LinkedList()

for i in range(100):
    myLinkedList.append(i)

myLinkedList.printList()
myLinkedList.reverse()
print("----")
myLinkedList.printList()