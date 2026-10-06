# cp-implementation-variation

Checkpoint: implement two variations of a Queue and a Priority Queue to practice understanding their implementation trade-offs.

## What this project covers

### 1. Queue
- **Array-based Queue (fixed size)** — `array_queue.py`
  `ArrayQueue(capacity)` backed by a circular buffer.
  `enqueue(element)` / `dequeue()` / `peek()` / `isEmpty()` (+ `isFull()`, `size()`).
- **Linked List-based Queue (dynamic size)** — `linked_list_queue.py`
  `LinkedListQueue` backed by a singly linked list with front/rear pointers.
  Same API, grows dynamically (never full).

### 2. Priority Queue
- **Min-Heap-based Priority Queue** — `min_heap_priority_queue.py`
  `MinHeapPriorityQueue` implemented from scratch (`_sift_up` / `_sift_down`).
  `insert(element)` O(log n) / `extractMin()` O(log n) / `peekMin()` O(1) / `isEmpty()`.
- **Ordered Array-based Priority Queue** — `ordered_array_priority_queue.py`
  `OrderedArrayPriorityQueue` keeping a sorted list (via `bisect`).
  `insert(element)` O(n) / `extractMin()` O(1) / `peekMin()` O(1) / `isEmpty()`.

Elements for the priority queues just need to support `<` (numbers or `(priority, value)` tuples work).

## Edge cases handled
- `dequeue` / `peek` / `extractMin` / `peekMin` on an empty structure raise `IndexError`.
- `enqueue` into a full array-based queue raises `OverflowError`.
- The array queue uses a circular buffer so freed slots are reused (wrap-around).
- The linked-list queue resets its rear pointer when the last element is removed.

## Quick check
```bash
python3 -c "
from array_queue import ArrayQueue
from linked_list_queue import LinkedListQueue
from min_heap_priority_queue import MinHeapPriorityQueue
from ordered_array_priority_queue import OrderedArrayPriorityQueue
"
```
