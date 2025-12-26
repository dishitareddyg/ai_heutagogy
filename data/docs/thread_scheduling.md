
# Thread Scheduling in Operating Systems

## Core Idea
Thread scheduling determines **how CPU time is shared among threads** within the same or different processes.

Threads are lighter than processes and share memory, making scheduling decisions more frequent and critical.

---

## Why Thread Scheduling Matters
- Affects responsiveness
- Determines parallelism efficiency
- Impacts application performance

Poor thread scheduling can cause:
- Deadlocks
- Priority inversion
- CPU thrashing

---

## Types of Thread Scheduling

### 1. User-Level Thread Scheduling
- Managed by user-level libraries
- Faster context switches
- OS is unaware of threads

### 2. Kernel-Level Thread Scheduling
- Managed by the OS kernel
- True parallelism on multi-core systems
- Higher overhead

---

## Scheduling Policies

### Round Robin
- Each thread gets a time slice
- Fair and responsive

### Priority-Based Scheduling
- Threads with higher priority execute first
- Risk of starvation

---

## Real-World Analogy
Imagine a group project:
- Round Robin: Everyone speaks in turns
- Priority-based: Team leader speaks more often

---

## Try This (Mini Task)
Design a scenario where:
- One low-priority thread blocks a high-priority thread
- Explain how priority inversion occurs

---

## Reflect (Heutagogical Prompt)
- Should all threads be treated equally?
- When is unfair scheduling actually beneficial?

---

## Extend Your Learning
- Study priority inheritance
- Compare thread scheduling in Linux vs Windows
- Analyze multi-core scheduling challenges
