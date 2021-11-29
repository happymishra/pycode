import asyncio
import logging
import time

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")


# *await* passes function control back to the event loop
# await can only be used with async keyword. async can be used with return, await and yield keyword also

async def count_one():
    logging.info(f"One: Wait at sleep")

    # Here, await tells event loop suspend execution of `count_one`, till I get result from sleep.
    #  asyncio.sleep function is in event loop and event loop is executed after all the main thread is done
    # so even though here time is 0 seconds, it is executed only after count_two and count_three methods are exectued
    # and are in await state
    await asyncio.sleep(0)
    logging.info(f"One: Sleep complete")


async def count_two():
    logging.info(f"Two: Wait at sleep")
    await asyncio.sleep(5)
    logging.info(f"Two: Sleep complete")


async def count_three():
    logging.info(f"Three: Wait at sleep")
    await asyncio.sleep(5)
    logging.info(f"Three: Sleep complete")


# This method is created because await can only be called from async functions.
async def collector():
    logging.info(f"Collector: Start")
    # Collector is blocked here, till all the counts are done
    await asyncio.gather(count_one(), count_two(), count_three())
    logging.info(f"Collector: Collector done")


if __name__ == '__main__':
    logging.info("Main: start")
    s = time.perf_counter()

    logging.info(f"Main: Waiting for collector to finish")
    # Thread is blocked here, till all the collector is done
    asyncio.run(collector())
    logging.info(f"Main: Collector completed")

    elapsed = time.perf_counter() - s

    logging.info(f"Main: Done in {elapsed} time")

""""
# Valid async use

async def f():
    y = await z()
    return y
    
    
async def g(x):
    yield x
    
    
# Invalid async use
async def m(x):
    yield from gen(x)
    
# await cannot be used without async
def m(x):
    y = await z()
    return y
"""
