from ROOT import *
f = TFile("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_Run1Fid_20160222/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1.root")
#f = TFile('/cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2.root')
t = f.Get('Ana/passedEvents')
for i in range(t.GetEntries()):
    t.GetEntry(i)
    if len(t.lep_id) < 2: continue
    passedLepIndex = []
    for j in range(len(t.lep_pt)):
        if not t.lep_tightId[j]: continue
        if not ((t.lep_RelIso)[j]>0.35): continue
        passedLepIndex.append(j)
    if not len(passedLepIndex) == 2: continue
    if not ((t.lep_id)[passedLepIndex[0]]+(t.lep_id)[passedLepIndex[1]]==0): continue

    if len(t.GENlep_pt) == 2:


       print 'lep1: reco - ', t.lep_pt[0], ', gen - ', t.GENlep_pt[0]
       print 'lep2: reco - ', t.lep_pt[1], ', gen - ', t.GENlep_pt[1]
       print ''
