from subprocess import call
import os.path
import glob

#nSetups = len(glob.glob('setup*py'))
#tmpsetup = 'setup_' + str(nSetups+1) + '.py'

call('ls setups', shell=True) 
config =  raw_input('choose input: ')

tmpsetup = config

call('cp setups/' + config + ' ' + tmpsetup, shell=True)

call('python ' + tmpsetup, shell=True)

call('cp -r setups backup', shell=True)
call('rm -i ' + tmpsetup, shell=True)

