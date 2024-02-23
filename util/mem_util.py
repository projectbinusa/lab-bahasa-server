import os
import psutil

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}{}:consumed memory: {:,}".format(
            func.__name__, args[1].path, mem_after - mem_before))
        return result
    return wrapper