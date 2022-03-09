"""
# implementation with Python built in list
"""
# define a stack
s = []
# add some items to it
s.append("eat")
s.append("sleep")
s.append("code")

print("list implementation", s)

print(s.pop())  # code
print(s.pop())  # sleep
print(s.pop())  # eat
# print(s.pop()) #error


"""
# implementation with Python collections.deque
"""
from collections import deque

q = deque()
q.append("eat")
q.append("sleep")
q.append("code")
print("deque implementation", q)
print(q.pop())  # code
print(q.pop())  # sleep
print(q.pop())  # eat
# print(q.pop()) #error - pop from an empty queue

"""
# implementation with Python class
add elements to end of list, pop from the end (n)
"""
# define a stack class
class StackEND:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"{[str(item) for item in self.items]}"

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def display_all_items(self):
        return self.items


new_stack = StackEND()

new_stack.push("eat")
new_stack.push("sleep")
new_stack.push("code")
print("Class implementation", new_stack.__str__())
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.display_all_items())
print(new_stack.isEmpty())


"""
# implementation with Python class
add elements to beginning of list, pop from the 0th index
main diff is using insert method to add items at 0th index
"""


class StackBEG:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"{[str(item) for item in self.items]}"

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def display_all_items(self):
        return self.items


new_stack2 = StackBEG()

new_stack2.push("eat")
new_stack2.push("sleep")
new_stack2.push("code")

print("Class implementation2", new_stack2.__str__())

"""
Time complexity for all the above operations is O(1) constant time
"""
