import time
hours = 24
mints = 60
secs = 60

for hour in range(hours):
    for mint in range(mints):
        for sec in range(secs):
            print(f"{hour}:{mint}:{sec}")
            time.sleep(1)
        print()
