from zro import Proxy
import os
import sys
import mpeconfig
import json

if __name__ == '__main__':
	config = mpeconfig.source_configuration('neuropixels')
	stim_agent_params = config['components']['Stim']
	camstim_host = stim_agent_params['host']
	camstim_port = str(stim_agent_params['port'])
	host_port = camstim_host+':' +camstim_port
	camstim = Proxy(host_port, serialization='json')
	drop_size = sys.argv[1]
	try:
		drop_num = sys.argv[2]
	except IndexError as E:
		drop_num = 100

	params_path = r"C:\Users\svc_neuropix\Documents\python_scripts\water_test\water_test.json"
	with open(params_path, 'r') as f:
		params = json.load(f)

	params["warm_up_trials"] = int(drop_num)
	params["auto_reward_volume"] = int(drop_size)/1000
	params['max_task_duration_min'] = int(drop_num)*2/60
	#print(params)
	camstim.start_session('366122', 'greggh', override_params=params)