import logging
import threading
import time

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")


def thread_function(name):
    logging.info(f"Thread {name}: starting")
    time.sleep(5)
    logging.info(f"Thread {name}: finishing")


if __name__ == '__main__':
    logging.info("Main: before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main: Before starting thread")

    x.start()

    logging.info("Main: Wait for thread to finish")

    # x.join()

    logging.info("Main: all done")

# Output with non-daemonic thread
"""
16:42:54: Main: before creating thread
16:42:54: Main: Before starting thread
16:42:54: Thread 1: starting
16:42:54: Main: Wait for thread to finish
16:42:54: Main: all done

## After 5 seconds 
16:42:59: Thread 1: finishing
"""

# Python program will wait to finish the program. By default, for all non daemonic thread it calls join internally

# To Create daemonic thread
# x = threading.Thread(target=target_function, args=(1,), daemon=True)

# Output with daemonic thread
"""
16:42:54: Main: before creating thread
16:42:54: Main: Before starting thread
16:42:54: Thread 1: starting
16:42:54: Main: Wait for thread to finish
16:42:54: Main: all done
"""

