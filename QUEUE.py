from collections import deque
from queues import Queue 
from queues import Stack

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

    fifo = Queue()
    fifo.enqueue("1st")
    fifo.enqueue("2nd")
    fifo.enqueue("3rd")

    fifo.dequeue()
    fifo.dequeue()
    fifo.dequeue()

     
    fifo = Queue("1st", "2nd", "3rd")
    len(fifo)

    for element in fifo:
        print(element)
    len(fifo)

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

    lifo = Stack("1st", "2nd", "3rd")
    for element in lifo:
        print(element)
    lifo = []
    lifo.append("1st")
    lifo.append("2nd")
    lifo.append("3rd")
    lifo.pop()
    lifo.pop()
    lifo.pop()
 
