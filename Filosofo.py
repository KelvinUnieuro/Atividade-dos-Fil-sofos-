import threading
import time
import random

num_philosophers = 5
forks = [threading.Semaphore() for _ in range(num_philosophers)]

def philosopher(num):
    left_fork = forks[num]
    right_fork = forks[(num + 1) % num_philosophers]

    while True:
        time.sleep(random.uniform(1, 3))
        left_fork.acquire()
        right_fork.acquire()
        print(f"Filósofo {num} está comendo.")
        time.sleep(random.uniform(1, 3))
        right_fork.release()
        left_fork.release()
        print(f"Filósofo {num} está pensando.")
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(num_philosophers)]
    for p in philosophers:
        p.start()
    for p in philosophers:
        p.join()
