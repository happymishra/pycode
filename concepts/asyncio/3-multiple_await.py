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

    logging.info(f"{color}Thread: {thread_number} -> Got a random number {rand_num} above threshold {threshold}")

    return rand_num


# Here the await make the program sequential
async def get_multiple_random_numbers():
    logging.info(f"get_multiple_random_numbers: Start")
    r1 = await make_random(1, 5)
    logging.info(f"******************** Got r1 -> {r1} *********************************")
    r2 = await make_random(2, 5)
    logging.info(f"Got r2 -> {r2}")

    return r1, r2


async def collector():
    #  res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    r = await get_multiple_random_numbers()
    return r


if __name__ == "__main__":
    random.seed(444)
    result = asyncio.run(collector())

    logging.info(f"Result is: {result}")
