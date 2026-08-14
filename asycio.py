import asyncio
import time
async def task(name,delay):
    print(f"task {name} started")
    await asyncio.sleep(delay)
    print(f"task {name} finished")

async def main():
    await asyncio.gather(
    task('Task1',2),
    task('Task2',3),
    task('Task3',1)
    )

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(end_time - start_time)
