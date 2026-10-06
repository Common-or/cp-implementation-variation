"""Ordered Array-based Priority Queue (array kept sorted by priority).

Trade-offs:
  - Pros: O(1) peekMin / extractMin (min always at index 0); simple code.
  - Cons: O(n) insert (must shift elements to keep sorted order); good only
          for small n or removal-heavy workloads.

Array is kept in ascending order so index 0 always holds the minimum.
Elements must be comparable with `<` (e.g. numbers, or (priority, value) tuples).
"""

import bisect


class OrderedArrayPriorityQueue:
    """Priority queue backed by a sorted Python list (ascending)."""

    def __init__(self):
        self._data = []

    def insert(self, element):
        """Insert an element, maintaining the array in sorted order. O(n).

        Uses binary search (bisect) to find the position, then list.insert
        shifts elements — the shift dominates at O(n).
        """
        idx = bisect.bisect_left(self._data, element)
        self._data.insert(idx, element)

    def extractMin(self):
        """Remove and return the element with minimum priority. O(1)*.

        (*O(n) list-shift cost at C speed; logically just pops index 0.)

        Raises:
            IndexError: if the priority queue is empty.
        """
        if self.isEmpty():
            raise IndexError("extractMin from an empty priority queue")
        return self._data.pop(0)

    def peekMin(self):
        """Return (without removing) the minimum element. O(1).

        Raises:
            IndexError: if the priority queue is empty.
        """
        if self.isEmpty():
            raise IndexError("peekMin from an empty priority queue")
        return self._data[0]

    def isEmpty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"OrderedArrayPriorityQueue({self._data})"
