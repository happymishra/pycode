from concurrent.futures import ThreadPoolExecutor
import logging
import threading
import time

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

VALUE = 0

# https://realpython.com/intro-to-python-threading/#race-conditions

lock = threading.Lock()


# To acquire lock - lock.acquire()
# To release lock - lock.release()

def thread_function(name):
    global VALUE
    logging.info(f"Thread {name}: Start. Value: {VALUE}")
    # Modifying the value is a critical section. Let's take the lock

    with lock:
        logging.info(f"Thread {name} has lock")
        local_value = VALUE
        local_value += 1

        logging.info(f"Thread {name}: Between. Value: {VALUE}")

        time.sleep(5)
        VALUE = local_value
        logging.info(f"Thread {name}: Finished. Value: {VALUE}")
        logging.info(f"Thread {name} has released lock")


if __name__ == '__main__':
    logging.info(f"Main: before creating thread, Value: {VALUE}")

    with ThreadPoolExecutor(max_workers=3) as executor:
        list_params = ["ABC", "DEF", "GHI"]
        # executor.map(thread_function, list_params)

        for index in list_params:
            executor.submit(thread_function, index)

    logging.info(f"Main: All Done. Value: {VALUE}")

# lock lets you acquire the lock only one time
# RLock lets you acquire the lock on the same critical section multiple time
