# import asyncio
# async def fn():
#     print("one")
#     await asyncio.sleep(1)
#     await fn2()
#     print('four')
#     await asyncio.sleep(1)
#     print('five')
#     await asyncio.sleep(1)
# async def fn2():
#     await asyncio.sleep(1)
#     print("two")
#     await asyncio.sleep(1)
#     print("three")
# asyncio.run(fn())

import asyncio
import time


async def async_say(delay, msg):
    await asyncio.sleep(delay)
    print(msg)


async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(async_say(4, 'hello'))
    task2 = loop.create_task(async_say(6, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
