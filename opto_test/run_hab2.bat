ECHO off
title Opto Calibration Script
call conda activate day2

ECHO Running opto test script
call python C:\Users\svc_neuropix\Documents\python_scripts\opto_test\run_hab2.py

cmd \k