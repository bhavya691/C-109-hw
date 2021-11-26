import statistics
import pandas as pd
df = pd.read_csv('data.csv')
score = df['reading score']
mean = statistics.mean(score)
median = statistics.median(score)
mode = statistics.mode(score)
stdev = statistics.stdev(score)
stdev_1_start, stdev_1_end = mean-stdev, mean+stdev
stdev_2_start, stdev_2_end = mean-2*stdev, mean+2*stdev

stdev_3_start, stdev_3_end = mean-3*stdev, mean+3*stdev

stdev_1_limit = [result for result in score if result > stdev_1_start and result < stdev_1_end]

stdev_2_limit = [result for result in score if result > stdev_2_start and result < stdev_2_end]

stdev_3_limit = [result for result in score if result > stdev_3_start and result < stdev_3_end]

print(f'Mean: {mean}')
print(f'Median: {median}')
print(f'Mode: {mode}')
print(f'Standard Deviation: {stdev}')   

print('{} % is present in stdev 1'.format(len(stdev_1_limit) * 100 / len(score)))

print('{} % is present in stdev 2'.format(len(stdev_2_limit) * 100 / len(score)))

print('{} % is present in stdev 3'.format(len(stdev_3_limit) * 100 / len(score)))