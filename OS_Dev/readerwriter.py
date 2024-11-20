import threading
import time
import random

# Semaphores
read_count = 0
mutex = threading.Semaphore(1)  # Mutex to protect read_count
write_lock = threading.Semaphore(1)  # Write lock to allow exclusive access to writers

# Shared resource (database) - clock initialized to 23:59:55
database = {'hours': 23.0, 'minutes': 59.0, 'seconds': 55.0}

# Number of iterations (finite reads/writes)
iterations = 5

# Reader function
def reader(reader_id):
    global read_count
    for _ in range(iterations):
        # Entry section
        mutex.acquire()  # Lock to protect read_count variable
        read_count += 1
        if read_count == 1:
            write_lock.acquire()  # First reader locks the writers out
        mutex.release()  # Unlock mutex

        # Critical section (reading)
        print(f"Reader {reader_id} is reading clock: {database['hours']:02.0f}:{database['minutes']:02.0f}:{database['seconds']:02.0f}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulating reading time

        # Exit section
        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            write_lock.release()  # Last reader unlocks the writers
        mutex.release()
        print(f"Reader {reader_id} exiting critical section")
        time.sleep(random.uniform(0.1, 0.5))  # Simulating time between read operations

# Writer function
def writer(writer_id):
    global database
    for _ in range(iterations):
        # Entry section
        write_lock.acquire()  # Writer locks the resource

        # Critical section (writing)
        database['seconds'] += 1
        if database['seconds'] == 60:
            database['seconds'] = 0
            database['minutes'] += 1
        if database['minutes'] == 60:
            database['minutes'] = 0
            database['hours'] += 1
        if database['hours'] == 24:
            database['hours'] = 0

        print(f"Writer {writer_id} is writing clock: {database['hours']:02.0f}:{database['minutes']:02.0f}:{database['seconds']:02.0f}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulating writing time

        # Exit section
        write_lock.release()
        time.sleep(random.uniform(0.1, 0.5))  # Simulating time between write operations

if __name__ == "__main__":
    # Create reader and writer threads
    num_readers = 3
    num_writers = 2
    reader_threads = [threading.Thread(target=reader, args=(i+1,)) for i in range(num_readers)]
    writer_threads = [threading.Thread(target=writer, args=(i+1,)) for i in range(num_writers)]

    # Start all threads
    for thread in reader_threads + writer_threads:
        thread.start()

    # Wait for all threads to finish
    for thread in reader_threads + writer_threads:
        thread.join()

    print("All reading and writing operations have been completed.")
