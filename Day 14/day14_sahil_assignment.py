# =============================================================================
# Day 14 Assignment - Stack and Queue
# =============================================================================

from collections import deque


def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# -----------------------------------------------------------------------------
# Question 1: Build Your Own Stack
# -----------------------------------------------------------------------------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is Empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack:", self.items)


# -----------------------------------------------------------------------------
# Question 2: Balanced Parentheses Checker
# -----------------------------------------------------------------------------
def is_balanced(expression):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in expression:
        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":
            if not stack:
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return len(stack) == 0


# -----------------------------------------------------------------------------
# Question 3: Build Your Own Queue
# -----------------------------------------------------------------------------
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return "Queue is Empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Queue:", list(self.items))


# -----------------------------------------------------------------------------
# Question 4: Movie Ticket Counter Simulation
# -----------------------------------------------------------------------------
def ticket_counter():
    people = ["Asha", "Ravi", "Meena", "Karan", "Priya"]
    queue = Queue()

    print("People joining the queue:")

    for person in people:
        queue.enqueue(person)
        print(f"{person} joined the queue.")
        print("Current Queue:", list(queue.items))

    print("\nServing Customers:")

    while not queue.is_empty():
        person = queue.dequeue()
        print(
            f"Serving: {person}. "
            f"Tickets remaining in queue: {len(queue.items)}"
        )

    print("\nQueue is now empty.")


# =============================================================================
# DEMO / OUTPUT SECTION
# =============================================================================

section("Question 1: Build Your Own Stack")

stack = Stack()

for num in [1, 2, 3, 4]:
    stack.push(num)
    print(f"Pushed {num}")
    stack.display()

print("\nPopping two items...")

print("Popped:", stack.pop())
stack.display()

print("Popped:", stack.pop())
stack.display()

print("Top Element:", stack.peek())


section("Question 2: Balanced Parentheses Checker")

test_cases = [
    "{[()()]}",
    "{[(])}",
    "([]{})",
    "((())"
]

for exp in test_cases:
    print(f"{exp} -> {is_balanced(exp)}")


section("Question 3: Build Your Own Queue")

queue = Queue()

for name in ["Asha", "Ravi", "Meena"]:
    queue.enqueue(name)
    print(f"Enqueued: {name}")
    queue.display()

print("\nServing Customers:")

while not queue.is_empty():
    person = queue.dequeue()
    print(f"Served: {person}")
    queue.display()


section("Question 4: Movie Ticket Counter Simulation")
ticket_counter()


# -----------------------------------------------------------------------------
# Question 5: Stack vs Queue (Written Answer)
# -----------------------------------------------------------------------------
"""
A Stack follows the LIFO (Last In, First Out) principle, which means the
last item added is removed first. A Queue follows the FIFO (First In,
First Out) principle, which means the first item added is removed first.
In a Stack, insertion and deletion happen at the same end called the top.
In a Queue, items are added at the rear and removed from the front.
A real-life example of a Stack is the Undo feature in a text editor.
A real-life example of a Queue is the print queue of a printer where
documents are printed in the order they were sent.
"""