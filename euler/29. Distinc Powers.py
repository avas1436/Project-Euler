import time

start = time.process_time()
my_set = set()
for a in range(2, 101):
    for b in range(2, 101):
        my_set.add(a**b)
end = time.process_time() - start


print(f"Problem Solve in {end} Seconds")
print(f"The asnware is : {len(my_set)}")
