import concurrent.futures
import requests
import numpy as np
import time
import itertools
import os

# https://docs.python.org/3/library/concurrent.futures.html

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} with status {response.status_code}")

def matrix_multiplication(size):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    for i in range(100):
        np.dot(A, B)

def run_workers(tasks, task_func, executor_cls):
    start_time = time.time()
    
    with executor_cls() as executor:
        # Map tasks to the executor
        results = list(executor.map(task_func, tasks))
    
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    # Define mode and task type mappings
    modes = {
        1: 'threading',
        2: 'multiprocessing'
    }

    task_types = {
        1: 'fibonacci',
        2: 'urls',
        3: 'matrix'
    }

    # Prompt user for mode and task type
    try:
        mode_number = int(input("Enter mode (1 for threading, 2 for multiprocessing): ").strip())
        task_type_number = int(input("Enter task type (1 for fibonacci, 2 for urls, 3 for matrix): ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit(1)

    # Determine mode
    mode = modes.get(mode_number)
    if not mode:
        print("Invalid mode. Please enter 1 for threading or 2 for multiprocessing.")
        exit(1)

    # Determine task type
    task_type = task_types.get(task_type_number)
    if not task_type:
        print("Invalid task type. Please enter 1 for fibonacci, 2 for urls, or 3 for matrix.")
        exit(1)

    # Set tasks and task function based on the selected task type
    if task_type == 'fibonacci':
        tasks = itertools.repeat(35, os.cpu_count())
        task_func = fibonacci
    elif task_type == 'urls':
        tasks = [
            "http://example.com",
            "http://example.org",
            "http://example.net",
            "http://example.edu",
            "http://google.com",
            "http://bing.com",
            "http://yahoo.com",
            "http://ir.baidu.com",
        ]
        task_func = fetch_url
    elif task_type == 'matrix':
        tasks = itertools.repeat(1000, os.cpu_count())
        task_func = matrix_multiplication

    # Choose the appropriate executor class based on mode
    if mode == 'threading':
        executor_cls = concurrent.futures.ThreadPoolExecutor
    elif mode == 'multiprocessing':
        executor_cls = concurrent.futures.ProcessPoolExecutor

    duration = run_workers(tasks, task_func, executor_cls)
    print(f"{mode.capitalize()} took {duration:.2f} seconds")

"""

fibonacci
Threading took 10.99 seconds
Multiprocessing took 5.25 seconds

urls
Threading took 1.37 seconds
Multiprocessing took 3.02 seconds

matrix
Threading took 15.82 seconds
Multiprocessing took 29.52 seconds

"""