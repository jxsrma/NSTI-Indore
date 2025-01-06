import time

print("Printing without flush:")
for i in range(5):
    print(i, end=" ", flush=False)
    time.sleep(1)

print("\n\nPrinting with flush:")
for i in range(5):
    print(i, end=" ", flush=False)
    time.sleep(1)
