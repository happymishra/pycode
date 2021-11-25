from concurrent.futures import ThreadPoolExecutor
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

    with ThreadPoolExecutor(max_workers=3) as executor:
        list_params = ["ABC", "DEF", "GHI"]
        executor.map(thread_function, list_params)

    logging.info("Main: All Done")
