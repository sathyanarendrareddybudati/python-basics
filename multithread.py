import time
import threading
start = time.perf_counter()
def satya(seconds):
    print(f'sleeping 1 second...')
    time.sleep(seconds)
    print(f'sleeping finished...')

threads = []
for _ in range(10):
    t = threading.Thread(target=satya, args=[1.5])
    t.start()
    threads.append(t)
# t1 = threading.Thread(target=satya)
# t2 = threading.Thread(target=satya)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
end = time.perf_counter()
print(f'finished in {round(end-start)} seconds..')