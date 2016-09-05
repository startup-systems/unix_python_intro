import time

some_allocated_data = [1,3,4]
while True:
    some_allocated_data[-1] += 1
    print "Hello World"
    time.sleep(30)