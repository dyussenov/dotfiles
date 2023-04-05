import time

current_time = time.time()

i = 1
s =1000000000
while i <= 10000000:
    s /= i
    i += 1

print(s)


print(time.time() - current_time)