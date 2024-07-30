import multiprocessing
import os

def worker(num):
    """Thread worker function"""
    print(f'Worker: {num}, PID: {os.getpid()}')

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

# **Explanation:** This script spawns five processes, each running the `worker` function, and prints the process ID.