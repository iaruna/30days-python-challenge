import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def main():
    time1 = time.perf_counter()
    # Normal Code
    func(4)
    func(2)
    func(1)

    # Same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    # Calculating Time
    time2 = time.perf_counter()
    print(time2 - time1)


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)


poolingDemo()
# Python program to illustrate the concept of threading importing the threading module

# Another example


def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
