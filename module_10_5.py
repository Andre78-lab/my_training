import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


def file_n(wtime, str_):
    file = open("file_n.txt", "a", encoding='utf-8')
    file.write(f'{wtime} {str_}\n')
    file.close()
    print(f'{wtime} ({str_})')


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
"""start_time1 = time.time()
for filename in filenames:
    read_info(filename)
finish_time1 = time.time()
file_n(finish_time1 - start_time1, "линейный")"""

# Многопроцессный

if __name__ == '__main__':
    start_time2 = time.time()
    with Pool(len(filenames)) as pool:
        pool.map(read_info, filenames)
    finish_time2 = time.time()
    file_n(finish_time2 - start_time2, "многопроцессный")
