
from typing import Any, List, Tuple

# TODO generic type


class HashTable:
    '''This is a Custome Hashtable.
    Stores key value pairs as tupple in array by hashing value to index.
    if hash returns the same hash from simple hashing. values are chained'''

    def __init__(self, size: int = 100) -> None:
        '''Creates new HashTable. default size 100'''
        self.MAX = size
        self.arr: List[List[Tuple[str, Any]]] = [[] for _ in range(self.MAX)]

    def getEntrys(self) -> List[Tuple[str, Any]]:
        '''returns list'''
        result: List[Tuple[str, Any]] = []
        for element in self.arr:
            if element:
                for entries in element:
                    result.append(entries)
        return result

    def getSimpleHash(self, key: str) -> int:
        '''simple hashing funxtion. generates integer Hash from key'''
        checksum = 0
        for char in key:
            checksum += ord(char)
        return checksum % self.MAX

    def add(self, key: str, value: Any) -> None:
        '''adds value as tupple(key, value) at index of integer hash of key.
        if there is already a tupple with different key at array position, new tupple is chained'''
        hashInt = self.getSimpleHash(key)

        # if list at hash index is empty just append key value as tupple and return
        if not self.arr[hashInt]:
            self.arr[hashInt].append((key, value))
            return

        found = False
        for idx, element in enumerate(self.arr[hashInt]):
            if len(element) == 2 and element[0] == key:
                self.arr[hashInt][idx] = (key, value)
                found = True
                break
            if not found:
                self.arr[hashInt].append((key, value))

    def __setitem__(self, key: str, value: Any) -> None:
        '''allows use of default python operator hashtable["key"] = value '''
        self.add(key, value)

    def get(self, key: str):
        '''return value of key.'''
        hashInt = self.getSimpleHash(key)
        for element in self.arr[hashInt]:
            if len(element) == 2 and element[0] == key:
                return element[1]
        return None

    def __getitem__(self, key: str):
        '''allows use of default python operator hashtable["key"]'''
        return self.get(key)

    def deleteItem(self, key: str) -> None:
        '''deletes value from hashtable'''
        hashInt = self.getSimpleHash(key)

        for idx, element in enumerate(self.arr[hashInt]):
            if len(element) == 2 and element[0] == key:
                del self.arr[hashInt][idx]
                break

    def __delitem__(self, key: str) -> None:
        '''allows use of default python operator del hashtable["key"]'''
        self.deleteItem(key)
