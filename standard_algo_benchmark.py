import numpy as np
import pandas as pd
import utils.new_standard_algo as standard_algo
import utils.benchmark as benchmark
import argparse

parser = argparse.ArgumentParser(description='HTMLPhish')
parser.add_argument('--p', type=str, default=None,
                    help='path to dir containing the csv files')
args = parser.parse_args()
p = args.p

scores = [benchmark.get_hit_rate_across_datasets('LRU',50, p),
          benchmark.get_hit_rate_across_datasets('LFU',50, p),
          benchmark.get_hit_rate_across_datasets('FIFO',50, p),
          benchmark.get_hit_rate_across_datasets('LIFO',50, p),
          benchmark.get_hit_rate_across_datasets('Belady',50, p),
          benchmark.get_hit_rate_across_datasets('ARC',50, p),
          benchmark.get_hit_rate_across_datasets('LECAR',50, p)]


table = pd.DataFrame(scores, columns = ['Mean Miss Scores',
                                         'Mean Non Miss Scores',
                                         'Mean Overall Scores'])
table['ALGOs'] = ['LRU', 'LFU', 'FIFO', 'LIFO', 'BELADY', 'ARC', 'LECAR']

table.set_index(['ALGOs'], inplace = True)
print(table)

