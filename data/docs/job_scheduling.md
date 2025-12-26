
# Job Scheduling in Operating Systems

## Core Idea
Job scheduling is the mechanism by which the operating system decides **which job or process should enter the system and when**. It primarily operates at the long-term scheduling level.

---

## Why Job Scheduling Matters
Efficient job scheduling:
- Maximizes CPU utilization
- Reduces waiting time
- Improves system throughput
- Balances system load

Poor scheduling can lead to starvation or underutilization of resources.

---

## Types of Job Scheduling

### 1. First Come First Serve (FCFS)
- Jobs are executed in the order of arrival
- Simple but can cause long waiting times

### 2. Shortest Job First (SJF)
- Job with the smallest execution time is scheduled first
- Optimal average waiting time
- Requires prior knowledge of job length

### 3. Priority Scheduling
- Jobs are scheduled based on priority
- Can be preemptive or non-preemptive
- May cause starvation

---

## Real-World Analogy
Think of a print queue:
- FCFS: First document submitted prints first
- Priority: Urgent documents jump ahead
- SJF: Small documents print first

---

## Try This (Mini Task)
Given job burst times:  
`J1 = 10, J2 = 5, J3 = 2`

1. Schedule them using FCFS
2. Schedule them using SJF
3. Compare average waiting times

---

## Reflect (Heutagogical Prompt)
- Which scheduling strategy would *you* choose if fairness mattered more than speed?
- Can you think of a real system where FCFS is actually better?

---

## Extend Your Learning
- Modify job scheduling to avoid starvation
- Explore aging techniques
- Compare batch systems vs time-sharing systems
