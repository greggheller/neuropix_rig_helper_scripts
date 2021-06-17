# neuropix_rig_helper_scripts
This repo contains scripts associated with Solenoid Test, Opto Test, tail stim logs, passive habituations and opening rig proxies

Many of these scripts use a szr.Proxy to trigger the camstim agent to run a script. Most of the python files have a paired bat file to make them easy to run. 

water test:
prupose: runs a dummy behavior session for mouse number 366122 with custom parameters to deliver many rewards in a short time (in order to weigh the volume delivered and verify that the solonoid is calibrated)

key script: water_cal.py



opto test:
prupose: runs a dummy behavior session for mouse number 366122 with custom parameters to loop through the levels for the opto so the brightness can be verified and documented
key script: opto_test.py



passive habituaiton:
runs a stimulus for the passive habituation sessions
run_hab1.py, run_hab2.py


tail_stim_logs:
purpose: tails the log for the behaivor session so that we can track the behavior, also records and moves the analog lock signal if the arduino is connected to the laptop
key script: tail_stim_log.py


Other helpers:
water_test/npx_helper.py
was written to run a behavior habitation session with sync and stop the streams afterwards. Good for testing, could be adapted to trigger MVR and be used for all habs

water_test/open_rig_proxies.py
was written to open proxies for all the experiment streams. Doesn't seem to be working right now. 
