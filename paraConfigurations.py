paraConfigs = { }

mc2015_dy_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/inputRootFiles/'
mc2016_dy_path = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/inputRoot/forApproval/'
savePath = '/home/mhl/public_html/2016/20161003_mass/'

#make ptErr distribution between 2015DY MC and 2016DY MC
skimmedDY_cut = 'massZ > 80 && massZ < 100 && massZErr > 0.2 && massZErr < 7.2 && Met < 30 && '
mu_ptBins = [10, 40, 50, 100]
mu_etaBins = [0.0, 0.9, 1.2, 2.4]

for i in range(len(mu_ptBins)-1):
 for j in range(len(mu_etaBins)-1):

  cut_mu1_pt_eta = 'pT1 > '+str(mu_ptBins[i])+' && pT1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) 
  cut_mu2_pt_eta = 'pT2 > '+str(mu_ptBins[i])+' && pT2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1])
  saveName_mu_ptErr = 'mu_ptErr_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) 
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_DY15_16_muPtErr_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 0, 5],
  'vars1': ['pterr1', 'pterr2'],
  'vars2': ['pterr1', 'pterr2'],
  'cuts1': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'cuts2': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1'],
  'xTitle': 'muon p_{T} error(GeV)',
  'yTitle': 'Rate/'+str(5.0/100)+' GeV',
  'legend1': '2015MC, DY',
  'legend2': '2016MC, DY',
  'savePath': savePath,
  'saveName': saveName_mu_ptErr, #
  'latexNote': latexNote_mu_pt_eta #
  }
