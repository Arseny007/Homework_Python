import matplotlib.pyplot as plt
import psutil

class Queue:

    def __init__(self, queue=[], size=None):
        self.queue = queue[:size] if size else queue

        if size:
            if len(self.queue) < size:
                add = [0] * (size - len(self.queue))
                self.queue = add + self.queue
                print(self.queue)
        self.size = size

    def push(self, item):
        self.queue.append(item)
        if self.size:
            if len(self.queue) >= self.size:
                self.pop()

    def pop(self):
        return self.queue.pop(0)

timings = [i for i in range(100)]
cpu_load = Queue([0 for _ in range(100)], 100)
mem_load = Queue([0 for _ in range(100)], 100)

plt.ion() # interactive on

fig, axs = plt.subplots(2)
cpu_line, = axs[0].plot(timings, cpu_load.queue, color='blue')
mem_line, = axs[1].plot(timings, cpu_load.queue, color='green')

axs[0].set_title("CPU",fontsize=18)
axs[1].set_title("MEM",fontsize=18)
axs[0].set_ylim([0, 100])
axs[1].set_ylim([0, 100])

def update_plots(cpu_load, mem_load):
    cpu_line.set_ydata(cpu_load.queue)
    mem_line.set_ydata(mem_load.queue)
    return cpu_line, mem_line

plt.show()

def actual_percent(mem = False):
    if mem:
        vir_mem = psutil.virtual_memory()
        return (vir_mem.total - vir_mem.available) / vir_mem.total * 100
    else:
        return psutil.cpu_percent(interval = 0.2, percpu=False)

try:
    while True:
        cpu_load.push(actual_percent())
        mem_load.push(actual_percent(mem=True))
        update_plots(cpu_load, mem_load)
        fig.canvas.draw()
        fig.canvas.flush_events()

except KeyboardInterrupt:
    print('\nshutdown')