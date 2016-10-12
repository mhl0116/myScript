paraConfigs = { }

mc2015_dy_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4/'
mc2016_dy_path = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/inputRoot/forApproval/'
mc2015_H_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/CMSSW_7_6_4/src/'
mc2016_H_path = '/cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/'
savePath = '/home/mhl/public_html/2016/20161004_mass/'

#make plots in different ptEta bins
skimmedDY_cut = 'massZ > 80 && massZ < 100 && massZErr > 0.2 && massZErr < 7.2 && Met < 30 && '
H_MC_cut = 'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && '

mu_ptBins = [10, 40, 50, 100]
mu_etaBins = [0.0, 0.9, 1.2, 2.4]

for i in range(len(mu_ptBins)-1):
 for j in range(len(mu_etaBins)-1):

  cut_mu1_pt_eta = 'pT1 > '+str(mu_ptBins[i])+' && pT1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) 
  cut_mu2_pt_eta = 'pT2 > '+str(mu_ptBins[i])+' && pT2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1])

  cut_mu_pt_eta_H = []
  for k in range(4):
      tmpCut = 'lep_pt[lep_Hindex['+str(k)+']] > ' + str(mu_ptBins[i]) + \
           ' && lep_pt[lep_Hindex['+str(k)+']] < ' + str(mu_ptBins[i+1]) + \
           ' && abs(lep_eta[lep_Hindex['+str(k)+']]) > ' + str(mu_etaBins[j]) + \
           ' && abs(lep_eta[lep_Hindex['+str(k)+']]) < ' +str(mu_etaBins[j+1]) 
      cut_mu_pt_eta_H.append(tmpCut)

  saveName_mu_ptErr_15MC = 'mu_ptErr_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_compare_DY_H_2015MC' 
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  #compare pTErr betwen 2015MC DY and H

  paraConfigs['mc_15_DY_H_muPtErr_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path,
  'rootPath2': mc2015_H_path,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'rootfile2': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIIFall15MiniAODv2.root',
  'tree1': 'passedEvents',
  'tree2': 'Ana/passedEvents',
  'binInfo': [200, 0, 0.1],
  'vars1': ['pterr1/pT1', 'pterr2/pT2'],
  'vars2': ['lep_pterr[lep_Hindex[0]]/lep_pt[lep_Hindex[0]]', 'lep_pterr[lep_Hindex[1]]/lep_pt[lep_Hindex[1]]', 'lep_pterr[lep_Hindex[2]]/lep_pt[lep_Hindex[2]]', 'lep_pterr[lep_Hindex[3]]/lep_pt[lep_Hindex[3]]'],
  'cuts1': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'cuts2': [H_MC_cut + cut_mu_pt_eta_H[0], H_MC_cut + cut_mu_pt_eta_H[1], H_MC_cut + cut_mu_pt_eta_H[2], H_MC_cut + cut_mu_pt_eta_H[3]], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1', '1', '1'],
  'xTitle': '#sigma_{p_{T}/p_{T}}',
  'yTitle': 'Rate/'+str(0.1/200),
  'legend1': '2015MC, DY',
  'legend2': '2015MC, H',
  'savePath': savePath,
  'saveName': saveName_mu_ptErr_15MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  'latexNote2': ''
  }

  saveName_mu_ptErr_16MC = 'mu_ptErr_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_compare_DY_H_2016MC'
  paraConfigs['mc_16_DY_H_muPtErr_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2016_dy_path,
  'rootPath2': mc2016_H_path,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'rootfile2': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISpring16MiniAODv2.root',
  'tree1': 'passedEvents',
  'tree2': 'Ana/passedEvents',
  'binInfo': [200, 0, 0.1],
  'vars1': ['pterr1/pT1', 'pterr2/pT2'],
  'vars2': ['lep_pterr[lep_Hindex[0]]/lep_pt[lep_Hindex[0]]', 'lep_pterr[lep_Hindex[1]]/lep_pt[lep_Hindex[1]]', 'lep_pterr[lep_Hindex[2]]/lep_pt[lep_Hindex[2]]', 'lep_pterr[lep_Hindex[3]]/lep_pt[lep_Hindex[3]]'],
  'cuts1': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'cuts2': [H_MC_cut + cut_mu_pt_eta_H[0], H_MC_cut + cut_mu_pt_eta_H[1], H_MC_cut + cut_mu_pt_eta_H[2], H_MC_cut + cut_mu_pt_eta_H[3]], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1', '1', '1'],
  'xTitle': '#sigma_{p_{T}/p_{T}}',
  'yTitle': 'Rate/'+str(0.1/200)+' GeV',
  'legend1': '2016MC, DY',
  'legend2': '2016MC, H',
  'savePath': savePath,
  'saveName': saveName_mu_ptErr_16MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  'latexNote2': ''
  }

