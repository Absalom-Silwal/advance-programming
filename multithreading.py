import time
import concurrent.futures

def task(name,delay):
    print(f"Task {name} Started")
    time.sleep(delay)
    print(f"Task {name} completed")

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(task,'Task1',2)
        task2 = executor.submit(task, 'Task2',3)
        task3 = executor.submit(task,'Task3',1)
        concurrent.futures.wait([task1,task2,task3])

start_time = time.time()

main()

end_time = time.time() - start_time

print(end_time)