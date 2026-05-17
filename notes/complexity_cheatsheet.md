# Complexity Cheatsheet

## Common time complexities

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Hash map lookup, array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop through array |
| O(n log n) | Linearithmic | Merge sort, quicksort (avg) |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2ⁿ) | Exponential | Naive recursive Fibonacci |
| O(n!) | Factorial | Generating all permutations |

## Common data structure operations (average case)

| Operation | Array | Hash Map | Linked List | BST (balanced) |
|-----------|-------|----------|-------------|----------------|
| Access | O(1) | O(1) | O(n) | O(log n) |
| Search | O(n) | O(1) | O(n) | O(log n) |
| Insert | O(n) | O(1) | O(1) | O(log n) |
| Delete | O(n) | O(1) | O(1) | O(log n) |

## Patterns to recognize

- **Sorted array + find pair** → Two Pointers
- **Subarray / substring with constraint** → Sliding Window
- **"Find Kth largest/smallest"** → Heap
- **Tree traversal** → DFS (recursive) or BFS (queue)
- **Shortest path** → BFS (unweighted) or Dijkstra (weighted)
- **"All combinations / permutations"** → Backtracking
- **Optimization with overlapping subproblems** → Dynamic Programming