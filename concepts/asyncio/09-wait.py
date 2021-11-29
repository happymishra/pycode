# Difference between gather and wait
# https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait

import asyncio


async def foo(value, sleep_time):
    print(f"foo -> {value}, sleeping for {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"foo -> {value}, Awake after {sleep_time} seconds")
    print(f"foo -> {value}")
    return value


async def main():
    tasks = [
        foo(value=1, sleep_time=6),
        foo(value=2, sleep_time=4),
        foo(value=3, sleep_time=2)
    ]

    finished, unfinished = await asyncio.wait(tasks)
    # finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in finished:
        print(f"Result -> {task.result()}")


asyncio.run(main())
