# https://stackoverflow.com/questions/46074841/why-coroutines-cannot-be-used-with-run-in-executor
# https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-5.html

import asyncio
from concurrent.futures import ThreadPoolExecutor


def run(corofn, *args):
    loop = asyncio.new_event_loop()
    try:
        coro = corofn(*args)
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    finally:
        loop.close()


async def main():
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(max_workers=5)
    futures = [
        loop.run_in_executor(executor, run, asyncio.sleep, 1, x)
        for x in range(10)]
    print(await asyncio.gather(*futures))
    # Prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())