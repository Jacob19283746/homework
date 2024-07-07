import threading
import time
def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)
def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)


num_thread = threading.Thread(target=print_numbers)
let_thread = threading.Thread(target=print_letters)


num_thread.start()
let_thread.start()

num_thread.join()
let_thread.join()

print("Потоки завершены")


