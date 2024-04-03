
from queue import Queue
import threading
import time

# Function to process numbers from the queue
def process_numbers(queue):
    while True:
        number = queue.get()
        if number is None:  # None is used as a signal to stop the thread
            queue.task_done()
            break
        print(f"{threading.current_thread().name} removed {number} from the queue. Even: {number % 2 == 0}")
        queue.task_done()

def main():
    number_queue = Queue()

    # Creating three threads that will process the numbers
    threads = [threading.Thread(target=process_numbers, args=(number_queue,), name=f"Thread-{i+1}") for i in range(3)]

    # Starting the threads
    for thread in threads:
        thread.start()

    # Filling the queue with numbers
    for number in range(1, 11):
        number_queue.put(number)

    # Allowing some time for the queue to empty before sending stop signals
    time.sleep(1)

    # Sending a stop signal (None) to each thread
    for _ in range(len(threads)):
        number_queue.put(None)

    # Joining the threads
    for thread in threads:
        thread.join()

    print("All tasks are done.")

if __name__ == "__main__":
    main()
