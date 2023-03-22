import os
from glob import glob
from pathlib import Path
import pandas as pd

PATH = "dataset/misses"
EXT = "*.csv"
all_csv_files1 = [file
                for path, subdir, files in os.walk(PATH)
                for file in glob(os.path.join(path, EXT))]

PATH = "dataset/address_pc_files"
EXT = "*.csv"
all_csv_files2 = [file
                for path, subdir, files in os.walk(PATH)
                for file in glob(os.path.join(path, EXT))]

files = all_csv_files1+all_csv_files2

for f in files:
    print(f)
    df = pd.read_csv(f)
    def ammma(s, base):
        p = int(s, base=16)
        if p > 0xffffffff:
            print(f, s, p)
        return p
    df['Address'] = df['Address'].apply(ammma, base=16)
    df['PC'] = df['PC'].apply(int, base=16)