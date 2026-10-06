"""Array-based Queue (fixed size) using a circular buffer.

Trade-offs:
  - Pros: O(1) enqueue/dequeue, cache-friendly, no per-element allocations.
  - Cons: Fixed capacity; enqueue on a full queue must be rejected/resized.
"""


class ArrayQueue:
    """Fixed-capacity FIFO queue backed by a Python list (circular buffer)."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self._capacity = capacity
        self._data = [None] * capacity
        self._front = 0   # index of the front element
        self._size = 0    # number of stored elements

    def enqueue(self, element):
        """Add an element to the rear of the queue.

        Raises:
            OverflowError: if the queue is full.
        """
        if self.isFull():
            raise OverflowError("enqueue on a full queue")
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = element
        self._size += 1

    def dequeue(self):
        """Remove and return the front element of the queue.

        Raises:
            IndexError: if the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("dequeue from an empty queue")
        element = self._data[self._front]
        self._data[self._front] = None  # help GC
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return element

    def isEmpty(self) -> bool:
        """Check if the queue is empty."""
        return self._size == 0

    def peek(self):
        """Return the front element without removing it.

        Raises:
            IndexError: if the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("peek from an empty queue")
        return self._data[self._front]

    # --- helpful extras (not required, but standard) ---
    def isFull(self) -> bool:
        """Check if the queue is full."""
        return self._size == self._capacity

    def size(self) -> int:
        """Return the number of elements in the queue."""
        return self._size

    def __len__(self):
        return self._size

    def __repr__(self):
        items = [self._data[(self._front + i) % self._capacity] for i in range(self._size)]
        return f"ArrayQueue({items}, capacity={self._capacity})"
