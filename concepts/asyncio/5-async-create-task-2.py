import asyncio


async def say_hello(msg, delay):
    print(f"msg: started. {msg}")
    await asyncio.sleep(delay)
    print(f"msg: between {msg}")
    await asyncio.sleep(delay)
    print(f"msg: Done. Text {msg}")


async def main():
    task1 = asyncio.create_task(say_hello("hello", 1))
    task2 = asyncio.create_task(say_hello("world", 2))

    print("Start")
    await task1
    await task2

    print("Done")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
