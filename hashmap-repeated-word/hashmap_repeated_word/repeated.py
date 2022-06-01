import re

class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)
        return index

def repeated_word(string):
    arr_of_index=[]
    hash_map=HashTable()
    list=string.split(' ')
    for word in list:
        
        word=word.lower()
        word=re.sub(f'\W','',word)
        index = hash_map.add(word,word)
        if index in arr_of_index:
            return word
        arr_of_index.append(index)