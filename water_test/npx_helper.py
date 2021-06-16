from zro import Proxy
import os
import sys
import mpeconfig
import json
from pprint import pprint
import time

config = mpeconfig.source_configuration('neuropixels')

def open_proxy(key_string):
	config = mpeconfig.source_configuration('neuropixels')
	agent_params = config['components'][key_string]
	host = agent_params['host']
	port = str(agent_params['port'])
	host_port = host+':' +port
	proxy = Proxy(host_port, serialization='json')
	return proxy

class npx_helper():
	def __init__(self):
		self.config = mpeconfig.source_configuration('neuropixels')

		self.camstim = open_proxy('Stim')
		self.sync = open_proxy('Sync')

	

	def print_config(self):
		pprint(self.config)

	def start_sync(self):
		#print(type(self.sync))
		#print(type(self.sync.start))
		self.sync.start()


	def stop_sync(self):
		self.sync.stop()

	def start_session(self, mouse_id):
		self.camstim.start_session(mouse_id, 'greggh')

	def timed_session(self, mouse_id, wait_time_min):
		wait_time = int(wait_time_min)*60
		print('Wait time in seconds: '+str(wait_time))
		#print(type(self.camstim))
		#print(type(self.sync))

		self.start_sync()
		time.sleep(1)
		self.start_session(mouse_id)
		
		time.sleep(wait_time)
		self.stop_sync()