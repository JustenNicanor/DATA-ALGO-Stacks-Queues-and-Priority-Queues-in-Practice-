from collections import deque
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from itertools import count
from typing import Any

class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter  = count()
    
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]
    
@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")




        