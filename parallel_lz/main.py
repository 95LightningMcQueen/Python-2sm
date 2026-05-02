import asyncio
import time
from parallel import Parallel


def main():
    obj = Parallel()
    start_seq = time.perf_counter()
    obj.run_sequential()
    end_seq = time.perf_counter()
    start_th = time.perf_counter()
    obj.run_threads()
    end_th = time.perf_counter()
    time_seq = end_seq - start_seq
    time_th = end_th - start_th
    print('Время без потоков:', time_seq)
    print('Время с потоками:', time_th)
    print('Метод 1 завершен')
    obj.run_processes()
    print('Метод 2 завершен')
    asyncio.run(obj.run_asyncio_tasks())
    print('Метод 3 завершен')
    
if __name__ == '__main__':
    main()
