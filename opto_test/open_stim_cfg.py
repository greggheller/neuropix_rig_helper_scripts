import os
import subprocess
import mpeconfig

if __name__ == '__main__':
	config = mpeconfig.source_configuration('neuropixels')
	stim_agent_params = config['components']['Stim']
	camstim_host = stim_agent_params['host']


	stim_cfg_path = os.path.join(r'\\'+camstim_host, r"c\ProgramData\camstim\config\stim.cfg")
	sublime_path = r"C:\Program Files\Sublime Text 3\sublime_text.exe"

	command_str = sublime_path + ' ' + stim_cfg_path
	subprocess.Popen(command_str)