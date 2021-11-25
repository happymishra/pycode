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

    threads = list()

    for index in range(10):
        logging.info(f"Main: Create and start Thread: {index}")
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)

        x.start()

    # Wait for all the threads to finish
    for index, thread in enumerate(threads):
        logging.info(f"Main: before joining Thread: {index}")
        thread.join()
        logging.info(f"Main: Done Thread: {index}")

    logging.info("Main: all done")
