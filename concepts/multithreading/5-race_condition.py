from concurrent.futures import ThreadPoolExecutor
import logging
import threading
import time

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

VALUE = 0


# https://realpython.com/intro-to-python-threading/#race-conditions

def thread_function(name):
    global VALUE
    logging.info(f"Thread {name}: Start. Value: {VALUE}")
    # All variables that are scoped (or local) to a function are thread-safe like local_value.
    local_value = VALUE
    local_value += 1

    logging.info(f"Thread {name}: Between. Value: {VALUE}")

    time.sleep(5)
    VALUE = local_value
    logging.info(f"Thread {name}: Finished. Value: {VALUE}")


if __name__ == '__main__':
    logging.info(f"Main: before creating thread, Value: {VALUE}")

    with ThreadPoolExecutor(max_workers=3) as executor:
        list_params = ["ABC", "DEF", "GHI"]
        # executor.map(thread_function, list_params)

        for index in list_params:
            executor.submit(thread_function, index)

    logging.info(f"Main: All Done. Value: {VALUE}")
