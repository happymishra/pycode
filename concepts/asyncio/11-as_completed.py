import asyncio


async def first():
    print("first start")
    await asyncio.sleep(5)
    print("first done")
    return 'first'


async def second():
    print("second start")
    await asyncio.sleep(1)
    print("second done")
    return 'second'


async def third():
    print("third start")
    await asyncio.sleep(3)
    print("third Done")
    return 'third'


async def main():
    for future in asyncio.as_completed([first(), second(), third()]):
        print("Hello")
        result = await future
        print(f"Result -> {result}")


# Prints 'second', then 'third', then 'first'
asyncio.run(main())
