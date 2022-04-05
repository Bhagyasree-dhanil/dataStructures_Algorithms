# Queue

'''
fisrt in first out approch

Application

* Media playlist
* CPU task scheduling

operations associated with queues:

1. enqueue - add items to queue O(1)
2. Dequeue - remove last item O(1)
3. Front - get first item from queue O(1)
4. Rear - get last item from queue O(1)

'''

# using list

stock_price_queue = []

stock_price_queue.insert(0, 131.10)
stock_price_queue.insert(0, 133.4)
stock_price_queue.insert(0, 134.6)

print(stock_price_queue.pop())
print(stock_price_queue.pop())
print(stock_price_queue.pop())

# using collection.deque ( we can implement both stack and queue using collection.deque)

from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(18)
q.appendleft(4)

print(q.pop())
print(q.pop())
print(q.pop())


# class implementation of queue using deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return
        else:
            return self.buffer.pop()

    def isempty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


sp = Queue()

sp.enqueue({
    'company': 'walmart',
    'timestamp': '5 april 10.01 am',
    'price': 131.10
})

sp.enqueue({
    'company': 'walmart',
    'timestamp': '5 april 10.03 am',
    'price': 132.01
})

sp.enqueue({
    'company': 'walmart',
    'timestamp': '5 april 10.06 am',
    'price': 132.17
})

print(sp.buffer)
print("result", sp.dequeue())

# ================================= Exercise -1 =======================================================#
'''

For all exercises use Queue class implemented in main tutorial.

Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order
every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread 
is consuming the food orders. Use Queue class implemented in tutorial.

'''

food_order=Queue()
import time
import threading

def place_order(orders):
    for i in orders:
        print("placing order for :",i)
        food_order.enqueue(i)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while food_order.isempty()==False:
        order=food_order.dequeue()
        print("Now serving",order)
        time.sleep(2)

'''
order_list= ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
t1=threading.Thread(target=place_order, args=(order_list,))
t2=threading.Thread(target=serve_order)
t1.start()
t2.start()
'''

# ============================== Exercise -2=======================================================#

'''

Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial.
 Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number
 (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.
'''
bn=Queue()

def b_nos(n):
    bn.enqueue('1')
    for i in range(n):
        b_val=bn.front()
        print(b_val)
        bn.enqueue(b_val+'0')
        bn.enqueue(b_val+'1')
        bn.dequeue()

b_nos(10)