import psutil, time
while True:
    time.sleep(10)
    mem_load = psutil.virtual_memory()