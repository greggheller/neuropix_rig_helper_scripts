import os, glob
import argparse
import csv
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('requested_drop_size', type=int, )
parser.add_argument('number_of_drops', type=float,)
parser.add_argument('final_weight', type=float,)
parser.add_argument('reservoir_level', type=float,)
args, _ = parser.parse_known_args()

log_file = r"C:\Users\svc_neuropix\Documents\python_scripts\water_test\water_test_log.csv"

date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
requested_drop_size = args.requested_drop_size
num = args.number_of_drops
goal_weight = requested_drop_size*num/1000
actual_weight = args.final_weight
actual_drop_size = 1000*(actual_weight/num)
reservoir_level = args.reservoir_level

fields=[date, requested_drop_size, actual_weight, actual_drop_size, reservoir_level, num, ]
with open(log_file, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
