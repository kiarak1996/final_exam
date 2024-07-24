from queue import PriorityQueue

# Create a PriorityQueue object
my_queue = PriorityQueue()

my_queue.put((1, "Hello, PriorityQueue!"))

element = my_queue.get()

# Show the output
print(element)
