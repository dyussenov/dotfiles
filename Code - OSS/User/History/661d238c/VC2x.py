import time

current_time = time.time()

i = 0
s =0
while i < 1000:
    s += i
    i += 1

print(s)

print(time.time() - current_time)