import dask.dataframe as dd
import psutil
import os
import time

file = r"D:/TP2/data/2019-Oct.csv"

process = psutil.Process(os.getpid())

start_memory = process.memory_info().rss / 1024**2
start_time = time.time()

df = dd.read_csv(file)

rows = df.shape[0].compute()

end_time = time.time()
end_memory = process.memory_info().rss / 1024**2

print("Method: Dask")
print("Rows:", rows)
print("Time:", round(end_time - start_time,2), "seconds")
print("Memory:", round(end_memory - start_memory,2), "MB")