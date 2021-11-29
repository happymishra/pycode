import asyncio


async def foo():
    print("Inside foo")
    await asyncio.sleep(10)
    print("Awake: Inside foo")
    return "Foo!"


def got_result(future):
    print(f"got the result! {future.result()}")


async def hello_world():
    print(f"Adding foo to event loop")
    task = asyncio.create_task(foo())
    print(f"Added foo to event loop")

    # add callback
    task.add_done_callback(got_result)

    print("Callback added")

    print(task)

    await asyncio.sleep(5)

    print("Awake after 5 seconds")

    print("Sleeping for 9 seconds")
    await asyncio.sleep(9)
    print("Awake after  9 seconds")

    print(task)


asyncio.run(hello_world())
