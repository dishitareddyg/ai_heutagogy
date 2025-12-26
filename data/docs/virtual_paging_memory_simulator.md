
# Virtual Paging and Memory Simulation

## Core Idea
Virtual paging allows programs to use **more memory than physically available** by dividing memory into pages and swapping them between RAM and disk.

---

## Why Virtual Paging Matters
- Enables multitasking
- Improves memory utilization
- Isolates processes for safety

Without paging:
- Programs must fit entirely in RAM
- Memory fragmentation increases

---

## Key Concepts

### Page
A fixed-size block of memory

### Frame
A fixed-size block in physical memory

### Page Table
Maps virtual pages to physical frames

---

## Page Replacement Algorithms

### FIFO (First In First Out)
- Oldest page is replaced
- Simple but inefficient

### LRU (Least Recently Used)
- Replaces least recently accessed page
- Better performance but complex

### Optimal
- Replaces page not used for longest future time
- Theoretical benchmark

---

## Real-World Analogy
Think of a desk with limited space:
- Keep frequently used books on desk
- Move unused books to shelf

---

## Try This (Mini Task)
Given page reference string:  
`7, 0, 1, 2, 0, 3, 0, 4`

1. Simulate FIFO
2. Count page faults
3. Compare with LRU

---

## Reflect (Heutagogical Prompt)
- Is perfect memory management possible?
- How would increasing RAM change algorithm choice?

---

## Extend Your Learning
- Build a paging simulator
- Analyze thrashing conditions
- Explore demand paging
