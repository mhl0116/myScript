from subprocess import call
import time 

### z -> mumu
massZErr_rel_bins = [0.006, 0.008]
for i in range(10):
    massZErr_rel_bins.append(massZErr_rel_bins[-1]+(0.02-0.008)/10)
massZErr_rel_bins.append(0.05)

inputpath = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4/'
filename = 'DYJetsToLL_M-50_kalman_v4_m2mu.root'
plotpath = '/home/mhl/public_html/2016/20161020_mass/fitmassZ/'
outtxtName = 'sigma_m2mu.txt'

call('echo " " > ' + outtxtName, shell=True)

for i in range(len(massZErr_rel_bins)-1):

    cmd = 'python doClosure_mZ.py --min '+str(massZErr_rel_bins[i])+' --max '+str(massZErr_rel_bins[i+1]) \
        + ' --inpath ' + inputpath \
        + ' --filename ' + filename \
        + ' --plotpath ' + plotpath \
        + ' --outtxtName ' + outtxtName + ' --fs 2mu &'

    call(cmd, shell=True)


