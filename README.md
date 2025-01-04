# Parallel-And-Distributed-Computing

# A Comprehensive Guide

Welcome to the **Parallel-And-Distributed-Computing** repository! This project serves as a resource hub to understand and implement parallelism, concurrency, and distributed computing concepts in Python. Inspired by *Python Parallel Programming Cookbook, Second Edition*, it includes well-documented code samples, exercises, and real-world examples for building efficient, scalable, and high-performance applications.

## 📖 Table of Contents
- [Introduction](#-introduction)
- [Chapters Overview](#-chapters-overview)
  - [Chapter 1: Getting Started with Parallel Computing](#chapter-1-getting-started-with-parallel-computing)
  - [Chapter 2: Thread-Based Parallelism](#chapter-2-thread-based-parallelism)
  - [Chapter 3: Process-Based Parallelism](#chapter-3-process-based-parallelism)
  - [Chapter 4: Message Passing](#chapter-4-message-passing)
  - [Chapter 5: Asynchronous Programming](#chapter-5-asynchronous-programming)
- [Setup and Running Instructions](#-setup-and-running-instructions)
- [References](#-references)

## ⚡ Introduction

This repository explores Python's powerful ecosystem for parallel programming. It covers foundational concepts such as threads and processes to advanced topics like message-passing and asynchronous programming. Whether you're new to parallel computing or a seasoned developer, this repository offers a comprehensive learning experience.

### Key Highlights:

- Dive into **threading** and **multiprocessing** for concurrency.
- Explore **distributed systems** with message-passing techniques using MPI.
- Master **asynchronous programming** with Python's `asyncio`.

# 📚 Chapters Overview

## Chapter 1: Getting Started with Parallel Computing
- **Flynn’s Taxonomy**: Understanding SISD, SIMD, MISD, and MIMD.
- **Memory Organization**: Shared vs. distributed memory models.
- **Performance Metrics**: Speedup, efficiency, and Amdahl’s/Gustafson’s laws.

## Chapter 2: Thread-Based Parallelism
- **Threading Concepts**: Learn to use Python’s threading module.
- **Synchronization**: Manage thread safety using Locks, Conditions, and Semaphores.
- **Thread Communication**: Share data between threads with Queues.

## Chapter 3: Process-Based Parallelism
- **Process Creation**: Spawn and manage processes with the multiprocessing module.
- **Inter-Process Communication**: Use Pipes and Queues for sharing data.
- **Process Pools**: Efficiently handle parallel workloads with pools.

## Chapter 4: Message Passing
- **MPI Basics**: Use mpi4py for distributed computing.
- **Point-to-Point Communication**: Send and receive messages between processes.
- **Collective Operations**: Implement scatter, gather, and broadcast mechanisms.

## Chapter 5: Asynchronous Programming
- **Event Loops**: Manage tasks with Python’s asyncio.
- **Coroutines**: Write non-blocking code for efficient I/O operations.
- **Task Management**: Handle task scheduling, cancellation, and monitoring.

## 🛠️ Setup and Running Instructions

1. Clone the repository to your local machine using the following command:

    ```bash
    git clone https://github.com/etrazia17/Parallel-And-Distributed-Computing.git
    cd Parallel-And-Distributed-Computing
    ```

2. Install the required dependencies by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the desired chapter and run the specific script. For example, to run the `threading_basics.py` script in Chapter 2, use:

    ```bash
    cd chapter02
    python threading_basics.py
    ```

## 📝 References
Python Parallel Programming Cookbook, Second Edition by Giancarlo Zaccone