import asyncio
import logging
import random

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

colors = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def make_random(thread_number: int, threshold: int = 6) -> int:
    color = colors[thread_number]
    logging.info(f"{color}Thread: {thread_number} -> Initiate make_random")

    rand_num = random.randint(0, 10)

    while rand_num < threshold:
        logging.info(f"{color}Thread: {thread_number} -> make_random == {rand_num} too low. Retrying...")
        await asyncio.sleep(5)
        rand_num = random.randint(0, 10)

    logging.info(f"{color} Thread: {thread_number} -> Got a random number {rand_num} above threshold {threshold}")

    return rand_num


async def collector():
    #  res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    r = await asyncio.gather(make_random(1, 5), make_random(2, 6), make_random(3, 8))
    return r


if __name__ == "__main__":
    random.seed(444)
    result = asyncio.run(collector())

    logging.info(f"Result is: {result}")
