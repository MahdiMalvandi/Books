import asyncio

import asyncio
from asyncio import CancelledError


async def delay(delay_seconds: int, task_number: int = 0) -> int:
    print(f'sleeping for {delay_seconds} second(s)- {task_number}')
    count = delay_seconds
    for i in range(delay_seconds):
        await asyncio.sleep(1)
        print(f'sleeping for {count}')
        count -= 1
    print(f'finished sleeping for {delay_seconds} second(s)- {task_number}')
    return delay_seconds


async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


async def main():
    delay_task = asyncio.create_task(delay(4))
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())

    await task_one
    await task_two
    await delay_task


asyncio.run(main())
