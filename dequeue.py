import threading
from collections import deque
import time

class ThreadSafeDeque:
    def __init__(self):
        self.deque = deque()
        self.lock = threading.Lock()

    def append(self, item):
        with self.lock:
            self.deque.append(item)
            print(f"Appended {item}")

    def append_left(self, item):
        with self.lock:
            self.deque.appendleft(item)
            print(f"Appended left {item}")

    def pop(self):
        with self.lock:
            if len(self.deque) > 0:
                item = self.deque.pop()
                print(f"Popped {item}")
                return item
            else:
                print("Deque is empty")

    def pop_left(self):
        with self.lock:
            if len(self.deque) > 0:
                item = self.deque.popleft()
                print(f"Popped left {item}")
                return item
            else:
                print("Deque is empty")

    def size(self):
        with self.lock:
            return len(self.deque)

# Example usage with multiple threads
def worker(deque_obj, thread_id):
    for i in range(5):
        deque_obj.append(f"item {i} from thread {thread_id}")
        time.sleep(0.1)
        deque_obj.pop()

if __name__ == "__main__":
    thread_safe_deque = ThreadSafeDeque()

    # Create two threads
    thread1 = threading.Thread(target=worker, args=(thread_safe_deque, 1))
    thread2 = threading.Thread(target=worker, args=(thread_safe_deque, 2))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print(f"Final deque size: {thread_safe_deque.size()}")
