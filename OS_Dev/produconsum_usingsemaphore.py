import threading
import time
import random

# Shared buffer (using list to simulate slots)
buffer = [None] * 5  # Buffer size is 10
MAX = 5

# Semaphores to manage full and empty slots
empty = threading.Semaphore(MAX)  # Starts with MAX empty slots
full = threading.Semaphore(0)     # Starts with 0 full slots
lock = threading.Lock()           # Mutex to protect the critical section

# Producer function
def producer(producer_id):
    global buffer
    for i in range(MAX):
        item = random.randint(1, 100)
        inserted = False

        while not inserted:
            empty.acquire()  # Wait for an empty slot
            with lock:  # Lock the critical section
                for slot in range(MAX):
                    if buffer[slot] is None:  # Find an empty slot
                        buffer[slot] = item
                        print(f"Producer {producer_id} inserting {item} in slot {slot+1}")
                        inserted = True
                        break

                if not inserted:
                    print(f"Producer {producer_id} blocked ...... buffer full")
            time.sleep(0.5)  # Wait before trying again
            full.release()  # Signal that an item has been produced

# Consumer function
def consumer(consumer_id):
    global buffer
    for i in range(MAX):
        consumed = False

        while not consumed:
            full.acquire()  # Wait for a full slot
            with lock:  # Lock the critical section
                for slot in range(MAX):
                    if buffer[slot] is not None:  # Find a filled slot
                        item = buffer[slot]
                        buffer[slot] = None  # Empty the slot
                        print(f"Consumer {consumer_id} consuming {item} from slot {slot+1}")
                        consumed = True
                        break

                if not consumed:
                    print(f"Consumer {consumer_id} blocked ...... buffer empty")
            time.sleep(0.5)  # Wait before trying again
            empty.release()  # Signal that an item has been consumed

if __name__ == "__main__":
    # Create producer and consumer threads
    producer_thread_1 = threading.Thread(target=producer, args=(1,))
    producer_thread_2 = threading.Thread(target=producer, args=(2,))
    consumer_thread_1 = threading.Thread(target=consumer, args=(1,))
    consumer_thread_2 = threading.Thread(target=consumer, args=(2,))

    # Start the threads
    producer_thread_1.start()
    producer_thread_2.start()
    consumer_thread_1.start()
    consumer_thread_2.start()

    # Wait for all threads to finish
    producer_thread_1.join()
    producer_thread_2.join()
    consumer_thread_1.join()
    consumer_thread_2.join()

    print("All items have been produced and consumed.")
