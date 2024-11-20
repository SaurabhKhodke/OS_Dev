import threading
import time
import random

# Shared buffer and slot status
buffer = [None] * 10  # Buffer size is 10
MAX = 10
lock = threading.Lock()  # Mutex

# Producer function
def producer(producer_id):
    global buffer
    for i in range(MAX):
        time.sleep(1)  # Simulate work being done before producing an item
        item = random.randint(1, 100)
        inserted = False

        while not inserted:
            with lock:  # Lock the critical section
                # Check for empty slot
                for slot in range(MAX):
                    if buffer[slot] is None:  # Find an empty slot
                        buffer[slot] = item
                        print(f"Producer {producer_id} inserting {item} in slot {slot+1}")
                        inserted = True
                        break
                if not inserted:
                    print(f"Producer {producer_id} blocked ...... buffer full")
            time.sleep(0.5)  # Wait before trying again

# Consumer function
def consumer(consumer_id):
    global buffer
    for i in range(MAX):
        time.sleep(1)  # Simulate work being done before consuming an item
        consumed = False

        while not consumed:
            with lock:  # Lock the critical section
                # Check for filled slot
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
