from zro import Proxy
import os
import json
import mpeconfig

if __name__ == '__main__':
	config = mpeconfig.source_configuration('neuropixels')
	stim_agent_params = config['components']['Stim']
	camstim_host = stim_agent_params['host']
	camstim_port = str(stim_agent_params['port'])
	host_port = camstim_host+':' +camstim_port
	camstim = Proxy(host_port, serialization='json')


	params_path = r"C:\Users\svc_neuropix\Documents\python_scripts\opto_test\opto_test.json"
	with open(params_path, 'r') as f:
		params = json.load(f)

		
	camstim.start_session('366122', 'greggh', override_params = params)