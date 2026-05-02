import threading
import multiprocessing
import asyncio
import random
import time
import string


def thread_worker(file_name):
    with open(file_name, 'w') as f:
        for _ in range(100):
            number = random.randint(1, 10000)
            f.write(f'{number}\n')

def process_worker(lock):
    chars = string.ascii_letters
    length = random.randint(15, 20)
    random_str = ''.join(random.choice(chars) for _ in range(length))
    with lock:
        with open('shared.txt', 'a') as f:
            f.write(f'{random_str}\n')
            time.sleep(0.1)

class Parallel:
    def run_sequential(self):
        for i in range(1, 11):
            thread_worker(f'file_{i}.txt')

    def run_threads(self):
        threads_list = []
        for i in range(1, 11):
            file_name = f'file_{i}.txt'
            t = threading.Thread(target=thread_worker, args=(file_name, ))
            threads_list.append(t)
            t.start()
        for t in threads_list:
            t.join()

    def run_processes(self):
        lock = multiprocessing.Lock()
        proc_list = []
        with open('shared.txt', 'w') as f:
            f.write('')
        for _ in range(5):
            p = multiprocessing.Process(target=process_worker, args=(lock, ))
            proc_list.append(p)
            p.start()
        for p in proc_list:
            p.join()
            
    async def read_file_sim(self):
        wait_time = random.uniform(0.1, 5.0)
        await asyncio.sleep(wait_time)
        print('Файл прочитан за', round(wait_time, 2), 'сек')


    async def run_asyncio_tasks(self):
        tasks = []
        for _ in range(3):
            tasks.append(self.read_file_sim())
        await asyncio.gather(*tasks)
