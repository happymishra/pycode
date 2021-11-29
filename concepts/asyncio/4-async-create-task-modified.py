import asyncio


async def msg(text):
    print(f"msg: started")
    await asyncio.sleep(0.1)
    print(f"msg: between")
    await asyncio.sleep(0.1)
    print(f"msg: Done. Text {text}")


async def long_operation():
    print('long_operation started')
    await asyncio.sleep(3)
    print('long_operation finished')


async def main():

    # Now you want to start long_operation, but you don't want to wait for it to finish:
    # long_operation should be started, but second msg should be printed immediately.
    # Create task to do so:
    task = asyncio.ensure_future(long_operation())
    await msg("First")

    print("Start long operations")

    await msg('second')

    # Now, when you want, you can await task finised:
    await task


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
