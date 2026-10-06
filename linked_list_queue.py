"""Linked List-based Queue (dynamic size) using a singly linked list.

Trade-offs:
  - Pros: Unbounded (grows/shrinks dynamically), no wasted slots, no overflow.
  - Cons: O(n) memory overhead per node (pointer + allocation), less cache-friendly.
"""


class _Node:
    __slots__ = ("data", "next")

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    """FIFO queue backed by a singly linked list with front/rear pointers."""

    def __init__(self):
        self._front = None  # head: dequeue/peek end
        self._rear = None   # tail: enqueue end
        self._size = 0

    def enqueue(self, element):
        """Add an element to the rear of the queue. Never full (dynamic size)."""
        node = _Node(element)
        if self.isEmpty():
            self._front = self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def dequeue(self):
        """Remove and return the front element of the queue.

        Raises:
            IndexError: if the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("dequeue from an empty queue")
        element = self._front.data
        self._front = self._front.next
        if self._front is None:  # queue became empty
            self._rear = None
        self._size -= 1
        return element

    def isEmpty(self) -> bool:
        """Check if the queue is empty."""
        return self._front is None

    def peek(self):
        """Return the front element without removing it.

        Raises:
            IndexError: if the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("peek from an empty queue")
        return self._front.data

    def size(self) -> int:
        """Return the number of elements in the queue."""
        return self._size

    def __len__(self):
        return self._size

    def __repr__(self):
        items = []
        cur = self._front
        while cur is not None:
            items.append(cur.data)
            cur = cur.next
        return f"LinkedListQueue({items})"
