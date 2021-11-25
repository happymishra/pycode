# Join is used when we want one thread to wait before the other thread is finished

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
    x.join()

    # See time diff in logs
    logging.info("Main: all done")

# Output with non-daemonic thread
"""
16:51:02: Main: before creating thread
16:51:02: Main: Before starting thread
16:51:02: Thread 1: starting
16:51:02: Main: Wait for thread to finish

## After 5 second i.e. once Thread 1 is finished
16:51:07: Thread 1: finishing
16:51:07: Main: all done
"""

# Here, Main thread waits for Thread 1 to finish and then exits.
