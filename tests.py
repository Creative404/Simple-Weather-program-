import time

a=0
checkamte = True
while checkamte:
    a += 1
    print(a)
    if a == 5:
        checkamte = False
        print("test")
time.sleep(0.5)
print("done")
time.sleep(0)
print("done2")
