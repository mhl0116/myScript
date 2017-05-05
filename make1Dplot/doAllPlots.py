from subprocess import call

call('cp  paraConfigurations_1D.py paraConfigurations.py', shell=True)
saveName_0 = 'PtResidual_Z4L_Z4Lext_'
etas = [0,2.4]#0.9,1.8,2.4]
#pts = [5,10,20,30,40,50,60,70,80,90,100]
pts = [5,100]#20,40,50,60,100]
for i in range(len(pts)-1):
    for j in range(len(etas)-1):
        saveName = saveName_0 + 'pT_' + str(pts[i]) + '_' + str(pts[i+1]) + '_eta_' + str(etas[j]) + '_' + str(etas[j+1])
        call('python makePlot_1D.py -t "'+saveName+'"', shell=True)
