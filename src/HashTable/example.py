from hashTable import HashTable


hTable = HashTable(size = 10)

hTable.add("first entry", 1256)
hTable["second entry"] = 222
print(hTable["second entry"])
print(hTable["1234"])
print(hTable.getEntrys())
