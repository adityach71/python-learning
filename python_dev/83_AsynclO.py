import time
import asyncio
async def function1():
    await asyncio.sleep(1)
    print("func 1")
async def function2():
    await asyncio.sleep(1)
    print("func 2")
async def function3():
    await asyncio.sleep(4)
    print("func 3")
    
async def main():
    task1 = asyncio.create_task(function1())
    task2 = asyncio.create_task(function2())
    task3 = asyncio.create_task(function3())
    await task1
    await task2
    await task3

asyncio.run(main())