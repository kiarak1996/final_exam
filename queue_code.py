from queue import Queue

my_queue = Queue()

my_queue.put("Hello, Queue!")

element = my_queue.get()

print(element)
