import subprocess
import glob
import os
from datetime import datetime as dt
import time
import shutil

stim_computer = 'W10DTSM112721'
sync_computer = r'\\W10DTSM112719'

log_location = r'\\'+stim_computer+r'\c\ProgramData\AIBS_MPE\camstim\logs\*'

filename = '*_out.log'

sorted_list = sorted(glob.iglob(log_location), key=os.path.getctime)
recent_dir = sorted_list[-1]
stim_log_fullpath = glob.glob(os.path.join(recent_dir, filename))[0]

tail_path = r"C:\Program Files\cmder\vendor\git-for-windows\usr\bin\tail.exe"

command_str = f'{tail_path} {stim_log_fullpath} -f'
subprocess.Popen(command_str)

# make temporary name for file
timestamp = dt.now().strftime('%Y%m%d%H%M%S')
filename = 'analog_lick_'+timestamp+'.log'

data_path = r'C:\Program Files\python_scripts\analog_lick_data'

file_path = os.path.join(data_path, filename)

print('attempting to record from arduino to '+filename+ ' in '+data_path)
command_str = 'type com3:>> '+filename

os.chdir(data_path)
analog_lick_logging = subprocess.Popen(command_str, shell=True)

#read the text file periodically for a certain string
kill_str = "Task reached max duration" #- also add timeout feature, if nothing logs for 5 minutes kill and move
#when you find the string kill the process


wait_time_s = 3800
start_time = dt.now()
count = 0
end_count = 10
log_size = 0
sleep_time = 30
while((dt.now() - start_time).total_seconds()< wait_time_s):
	time.sleep(sleep_time)
	with open(stim_log_fullpath, 'r') as f:
		log_txt = f.read()
	if os.path.getsize(stim_log_fullpath) == log_size:
		count +=1
	else:
		count = 0
	log_size = os.path.getsize(stim_log_fullpath)
	not_writing = count >= end_count
	if kill_str in log_txt:
		print('killing Arduino logging, string"'+kill_str+'" was found in stim log')
	if not_writing:
		no_log_time = sleep_time*end_count
		print('killing Arduino logging, no logging detected for '+no_log_time+' seconds' )
	if (kill_str in log_txt) or not_writing:
		analog_lick_logging.kill()
		break
else:
	print('killing Arduino logging, reached max time of '+wait_time_s+'seconds' )
	analog_lick_logging.kill()


data_location = os.path.join(sync_computer, r'c\ProgramData\AIBS_MPE\neuropixels_data\*_*_*')
session_dir = sorted(glob.iglob(data_location), key=os.path.getctime)[-1]
session_name = os.path.split(session_dir)[1]
new_path = os.path.join(session_dir, session_name+'.analog_lick_'+timestamp+'.log')

shutil.copyfile(file_path, new_path)
