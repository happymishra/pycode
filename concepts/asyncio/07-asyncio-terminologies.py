# https://stackoverflow.com/questions/50592540/asyncio-create-task-to-run-forever

import asyncio

loop = asyncio.get_event_loop()


async def while_loop():
    n = 0

    while True:
        print(f"{n}")
        await asyncio.sleep(2)
        n += 1


async def some_func():
    await asyncio.sleep(5)
    print("Some Func")


future = loop.create_task(while_loop())
loop.run_until_complete(some_func())

# Output
"""
0
1
2
Some Func

I expected the while_loop function to run forever but it seems to only executes as a result of calling 
run_until_complete and it stops printing the while loop once some_func is finished executing
"""

# Argument to run_until_complete controls how long the event loop runs. In this case as some_func is the argument
# of the run_until_complete, so loop will run for 5 seconds. Once the loop end, all the coroutines are suspended.
# while_loop coroutine will also end.

"""
loop.run_until_complete(some_func()) - what you already used; run the event loop until the some_func coroutine 
finishes. Executes other coroutines in parallel during that time as well, 
but also stops executing them as soon as the event loop finishes.

loop.run_forever() - run the event loop until some coroutine or callback invokes loop.stop(). If none of them do that, 
then the event loop will not halt, even if all the coroutines come to an end. In your case you'd call 
loop.create_task(while_loop()) followed by loop.create_task(some_func()) and then loop.run_forever().

loop.run_until_complete(asyncio.gather(while_loop(), some_func())) run the event loop until both the specified 
coroutines finish. This (wait for all the tasks) is apparently what you expected loop.run_until_complete() to do 
automatically even if you name only one, except it doesn't work like that, it stops as soon as the specified coroutine 
finishes. asyncio.gather can be used to wait for multiple coroutines at once. 
For a more fine-tuned control of waiting, also see asyncio.wait.
"""
