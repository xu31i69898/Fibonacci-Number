# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dA24JM3Qd7PnsctLYRtx3ivuh_5a5Qbl
"""

import time

# Pure recursive method to calculate Fibonacci number
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Dynamic programming method to calculate Fibonacci number
def fib_dynamic(n):
    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n]

n_list = range(10, 60, 10)
recursive_time = []
dynamic_time = []

for n in n_list:
    # Measure execution time for pure recursive method
    start_time = time.time()
    fib_recursive(n)
    end_time = time.time()
    recursive_time.append(end_time - start_time)

    # Measure execution time for dynamic programming method
    start_time = time.time()
    fib_dynamic(n)
    end_time = time.time()
    dynamic_time.append(end_time - start_time)

# Plot execution time as a line chart
import matplotlib.pyplot as plt
plt.plot(n_list, recursive_time, label='Pure Recursive')
plt.plot(n_list, dynamic_time, label='Dynamic Programming')
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time Comparison')
plt.legend()
plt.show()