import time
a, b = 1,1

def recursive(n, a, b):
    if(n <= 1):
        return 1
    else:
        return a + recursive(n-1, b, a+b)

start_time = time.time()
for i in range(999):
    recursive(i, a, b)

print("--- %s seconds ---" % (time.time() - start_time))