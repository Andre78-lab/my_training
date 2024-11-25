import time
import threading

def  write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}.")
current_time_start1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
current_time_finish1 = time.time()
working_time1 = round(current_time_finish1-current_time_start1)
print(f'Работа функций: {time.strftime("%H:%M:%S", time.gmtime(working_time1))}')

current_time_start2 = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
print(threading.enumerate())
thread1.join()
thread2.join()
thread3.join()
thread4.join()

current_time_finish2 = time.time()
working_time2 = round(current_time_finish2-current_time_start2)
print(f'Работа потоков: {time.strftime("%H:%M:%S", time.gmtime(working_time2))}')
