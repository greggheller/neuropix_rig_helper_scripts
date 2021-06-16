ECHO off
title Water Test Script
call conda activate day2
set /p reward_vol=Desired water volume (in uL):
set /a reward_num=100
set /a expected_weight=%reward_vol%*10*%reward_num%/100
ECHO Running water test script with volume %reward_vol% %reward_num%
ECHO %reward_num% rewards should be dispensed, for final weight of 0.%expected_weight% grams
call python C:\Users\svc_neuropix\Documents\python_scripts\water_test\water_cal.py %reward_vol% %reward_num%
set /p final_weight=Delivered water weight (in mg):
set /p reservoir_level=Reservoir Level:
call python C:\Users\svc_neuropix\Documents\python_scripts\water_test\save_data.py %reward_vol% %reward_num% %final_weight% %reservoir_level%
cmd \k
