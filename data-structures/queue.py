"""
# implementation with Python built in list
"""
fruits = []
fruits.append("banana")
fruits.append("strawberry")
fruits.append("orange")

print(fruits.pop(0))
print(fruits.pop(0))
print(fruits)

"""
# implementation with Python collections.deque
"""
from collections import deque

fruits = deque()
fruits.append("banana")
fruits.append("strawberry")
fruits.append("orange")

print(fruits.popleft())
print(fruits.popleft())
print(fruits)

"""
# implementation with Python class
"""


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def display_items(self):
        return f"{[item for item in self.items]}"


queue_class = Queue()

queue_class.enqueue("hi")
queue_class.enqueue("bye")
queue_class.enqueue("see ya later")

print("Class implementation", queue_class.display_items())
print(queue_class.dequeue())
print(queue_class.dequeue())
print(queue_class.dequeue())


"""
Time complexity for all the above operations is O(1) constant time
"""
