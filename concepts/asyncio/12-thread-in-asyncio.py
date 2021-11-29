import asyncio
import logging
import concurrent.futures

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

colors = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


def blocking_io(thread_number):
    color = colors[thread_number]
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.

    logging.info(f'{color}Thread -> {thread_number} Inside blocking IO')

    with open("/dev/urandom", "rb") as f:
        output = f.read(100)
        logging.info(f'{color}Thread -> {thread_number} Done blocking IO')
        return output


def cpu_bound(thread_number):
    color = colors[thread_number]
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    logging.info(f'{color}Thread -> {thread_number} Inside CPU')
    output = sum(i * i for i in range(10 ** 7))
    logging.info(f'{color}Thread -> {thread_number} Done CPU')
    return output


async def main():
    loop = asyncio.get_event_loop()

    # # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(None, blocking_io, 1)
    print("default thread pool", result)

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as thread_pool:
        result = await loop.run_in_executor(thread_pool, blocking_io, 2)
        print("custom thread pool", result)
    #
    # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound, 3)
        print("custom process pool", result)


if __name__ == '__main__':
    asyncio.run(main())
