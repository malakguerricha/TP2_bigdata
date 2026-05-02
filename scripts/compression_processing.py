import pandas as pd
import psutil
import os
import time

original = r"D:/TP2/data/2019-Oct.csv"
compressed = r"D:/TP2/data/2019-Oct.csv.gz"

print("Creating compressed file...")

df = pd.read_csv(original)

df.to_csv(compressed, compression="gzip")

process = psutil.Process(os.getpid())

start_memory = process.memory_info().rss / 1024**2
start_time = time.time()

df = pd.read_csv(compressed, compression="gzip")

rows = len(df)

end_time = time.time()
end_memory = process.memory_info().rss / 1024**2

print("Method: Compression")
print("Rows:", rows)
print("Time:", round(end_time - start_time,2), "seconds")
print("Memory:", round(end_memory - start_memory,2), "MB")