import time

for n in range(1, 20, 1):
    if n%3 == 0:
        print("박수")
    else:
        print(n)
    
    time.sleep(0.5)