"""Min-Heap-based Priority Queue (implemented from scratch).

Trade-offs:
  - Pros: O(log n) insert and extractMin; good all-round choice.
  - Cons: peekMin is O(1) but arbitrary search/removal is O(n);
          more code than the ordered-array version.

Elements must be comparable with `<` (e.g. numbers, or (priority, value)
tuples). Smaller == higher priority (min-heap).
"""


class MinHeapPriorityQueue:
    """Priority queue backed by a binary min-heap stored in a Python list."""

    def __init__(self):
        self._heap = []

    # --- required API ---
    def insert(self, element):
        """Insert an element into the priority queue. O(log n)."""
        self._heap.append(element)
        self._sift_up(len(self._heap) - 1)

    def extractMin(self):
        """Remove and return the element with minimum priority. O(log n).

        Raises:
            IndexError: if the priority queue is empty.
        """
        if self.isEmpty():
            raise IndexError("extractMin from an empty priority queue")
        minimum = self._heap[0]
        last = self._heap.pop()
        if self._heap:
            self._heap[0] = last
            self._sift_down(0)
        return minimum

    def peekMin(self):
        """Return (without removing) the minimum element. O(1).

        Raises:
            IndexError: if the priority queue is empty.
        """
        if self.isEmpty():
            raise IndexError("peekMin from an empty priority queue")
        return self._heap[0]

    def isEmpty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self._heap) == 0

    # --- helpers ---
    def size(self) -> int:
        return len(self._heap)

    def __len__(self):
        return len(self._heap)

    def __repr__(self):
        return f"MinHeapPriorityQueue({self._heap})"

    # --- heap internals ---
    def _sift_up(self, idx: int):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._heap[idx] < self._heap[parent]:
                self._heap[idx], self._heap[parent] = self._heap[parent], self._heap[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx: int):
        n = len(self._heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < n and self._heap[right] < self._heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            self._heap[idx], self._heap[smallest] = self._heap[smallest], self._heap[idx]
            idx = smallest
