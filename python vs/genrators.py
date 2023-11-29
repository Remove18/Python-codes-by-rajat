import time

time.sleep(3)

def generate():
    for i in range (200):
        i = i + 1
        yield i
        
gen = generate()

for i in gen:
    print(i)

time.sleep(3)

for j in range(1,201):
    print(j)