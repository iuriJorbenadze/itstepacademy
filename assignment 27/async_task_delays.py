
import asyncio

async def task_delay_two_seconds():
    print("Task 2 seconds start")
    await asyncio.sleep(2)
    print("Task 2 seconds end")

async def task_delay_five_seconds():
    print("Task 5 seconds start")
    await asyncio.sleep(5)
    print("Task 5 seconds end")

async def main():
    task1 = asyncio.create_task(task_delay_two_seconds())
    task2 = asyncio.create_task(task_delay_five_seconds())

    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())
