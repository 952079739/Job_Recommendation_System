import psutil

memory_cu = psutil.virtual_memory()
memory = psutil.virtual_memory().percent
cpu = psutil.cpu_percent(3)
sent = psutil.net_io_counters().bytes_recv
print(sent)
print(cpu)
print(memory)