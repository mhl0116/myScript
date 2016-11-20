paraConfigs = { }

mc2015_dy_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/inputRootFiles/'
mc2016_dy_path = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/inputRoot/forApproval/'
mc2015_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/'
mc2016_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/makeSlimTree/'

mc2015_dy_path_v4 = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4/"
mc2015_dy_path_v4_NoMZCut = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4_NOmassZCut/"

savePath = '/home/mhl/public_html/2016/20161120_mass/'

#make plots in different ptEta bins
skimmedDY_cut = 'massZ > 80 && massZ < 100 && massZErr > 0.2 && massZErr < 7.2 && Met < 30 && '
skimmedDY_cutOnGEN = 'GENmass2l > 80 && GENmass2l < 100 && '

mu_ptBins = [10, 40, 50, 100]
mu_etaBins = [0.0, 0.9, 1.2, 2.4]

for i in range(len(mu_ptBins)-1):
 for j in range(len(mu_etaBins)-1):

  cut_mu1_pt_eta = 'pT1 > '+str(mu_ptBins[i])+' && pT1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) 
  cut_mu2_pt_eta = 'pT2 > '+str(mu_ptBins[i])+' && pT2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1])
  saveName_mu_ptErr = 'mu_ptErr_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) 
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  #make ptErr distribution between 2015DY MC and 2016DY MC

  paraConfigs['mc_DY15_16_muPtErr_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [1000, 0, 0.1],
  'vars1': ['pterr1/pT1', 'pterr2/pT2'],
  'vars2': ['pterr1/pT1', 'pterr2/pT2'],
  'cuts1': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'cuts2': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1'],
  'xTitle': '#sigma_{p_{T}/p_{T}}',
  'yTitle': 'Rate/'+str(0.1/1000),
  'legend1': '2015MC, DY',
  'legend2': '2016MC, DY',
  'savePath': savePath,
  'saveName': saveName_mu_ptErr, #
  'latexNote1': latexNote_mu_pt_eta, #
  'latexNote2': ''
  }

  saveName_mu_ptErr_15mc_v4 = 'mu_ptErr_15mc_v4_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
#  mc2015_dy_path_v4 = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4/"

  paraConfigs['mc_DY15_v4_16_muPtErr_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_v4,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [1000, 0, 0.1],
  'vars1': ['pterr1/pT1', 'pterr2/pT2'],
  'vars2': ['pterr1/pT1', 'pterr2/pT2'],
  'cuts1': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'cuts2': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1'],
  'xTitle': '#sigma_{p_{T}/p_{T}}',
  'yTitle': 'Rate/'+str(0.1/1000),
  'legend1': '2015MC_v4, DY',
  'legend2': '2016MC, DY',
  'savePath': savePath,
  'saveName': saveName_mu_ptErr_15mc_v4, #
  'latexNote1': latexNote_mu_pt_eta, #
  'latexNote2': ''
  }



  cut_fixlep1 = ' ( abs(genzm-massZ) > 3 && \
                    pT1 > 40 && pT1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9 &&  \
                    pT2 > ' + str(mu_ptBins[i])+' && pT2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1]) + ')'

  cut_fixlep2 = ' ( abs(genzm-massZ) > 3 && \
                    pT2 > 40 && pT2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9 &&  \
                    pT1 > ' + str(mu_ptBins[i])+' && pT1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) + ')'

  latexNote1_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T}^{lep1} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta|^{lep1} < '+str(mu_etaBins[j+1])
  latexNote2_mu_pt_eta = '40GeV < p_{T}^{lep2} < 50GeV, 0.0 < |#eta|^{lep2} < 0.9'

  saveName_mu_pt_leg2 = 'mu_pt_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_leg2'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_DY15_16_muPt_leg2_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, mu_ptBins[i], mu_ptBins[i+1]],
  'vars1': ['pT2', 'pT1'],
  'vars2': ['pT2', 'pT1'],
  'cuts1': [skimmedDY_cut + cut_fixlep1, skimmedDY_cut + cut_fixlep2], #
  'cuts2': [skimmedDY_cut + cut_fixlep1, skimmedDY_cut + cut_fixlep2], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1'],
  'xTitle': 'p_{T}',
  'yTitle': 'Rate/'+str(mu_ptBins[i+1]-mu_ptBins[i]/100),
  'legend1': '2015MC, DY',
  'legend2': '2016MC, DY',
  'savePath': savePath,
  'saveName': saveName_mu_pt_leg2, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }


  saveName_mu_pt_leg1 = 'mu_pt_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_leg1'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_DY15_16_muPt_leg1_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 40, 50],
  'vars1': ['pT1', 'pT2'],
  'vars2': ['pT1', 'pT2'],
  'cuts1': [skimmedDY_cut + cut_fixlep1, skimmedDY_cut + cut_fixlep2], #
  'cuts2': [skimmedDY_cut + cut_fixlep1, skimmedDY_cut + cut_fixlep2], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1'],
  'xTitle': 'p_{T}',
  'yTitle': 'Rate/'+str(mu_ptBins[i+1]-mu_ptBins[i]/100),
  'legend1': '2015MC, DY',
  'legend2': '2016MC, DY',
  'savePath': savePath,
  'saveName': saveName_mu_pt_leg1, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }


  cut_fixOneMu = ' ( pT1 > 40 && pT1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9 &&  \
                     pT2 > ' + str(mu_ptBins[i])+' && pT2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1]) + ') || '\
                +' ( pT2 > 40 && pT2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9 &&  \
                     pT1 > ' + str(mu_ptBins[i])+' && pT1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) + ')'
  latexNote1_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T}^{lep1} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta|^{lep1} < '+str(mu_etaBins[j+1])
  latexNote2_mu_pt_eta = '40GeV < p_{T}^{lep2} < 50GeV, 0.0 < |#eta|^{lep2} < 0.9'

  #compare genMZ and recoMZ for 2015MC in different pt-eta bin
  saveName_genZ_recoZ_2015MC = 'genZ_recoZ_2015MC_'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
  paraConfigs['mc_DY15_genZ_recoZ_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path,
  'rootPath2': mc2015_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 80, 100],
  'vars1': ['genzm'],
  'vars2': ['massZ'],
  'cuts1': [skimmedDY_cut + cut_fixOneMu], #
  'cuts2': [skimmedDY_cut + cut_fixOneMu], #
  'weight1': ['1'],
  'weight2': ['1'],
  'xTitle': 'massZ(GeV)',
  'yTitle': 'Rate/'+str(20/100)+' GeV',
  'legend1': '2015MC, m_{Z}^{GEN}',
  'legend2': '2015MC, m_{Z}^{RECO}',
  'savePath': savePath,
  'saveName': saveName_genZ_recoZ_2015MC, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }

  #compare genm2l and recoMZ for 2015MC in different pt-eta bin
  saveName_genm2l_recoZ_2015MC = 'genm2l_recoZ_2015MC_'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
  paraConfigs['mc_DY15_genm2l_recoZ_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_v4,
  'rootPath2': mc2015_dy_path_v4,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 80, 100],
  'vars1': ['GENmass2l'],
  'vars2': ['massZ'],
  'cuts1': [skimmedDY_cut + cut_fixOneMu + ' && genLep_pt1 > 0 && genLep_pt2 > 0'], #
  'cuts2': [skimmedDY_cut + cut_fixOneMu + ' && genLep_pt1 > 0 && genLep_pt2 > 0'], #
  'weight1': ['1'],
  'weight2': ['1'],
  'xTitle': 'massZ(GeV)',
  'yTitle': 'Rate/'+str(20/100)+' GeV',
  'legend1': '2015MC, GENmass2l',
  'legend2': '2015MC, m_{Z}^{RECO}',
  'savePath': savePath,
  'saveName': saveName_genm2l_recoZ_2015MC, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }
  
  #compare genm2l and GENMZ for 2015MC in different pt-eta bin
  saveName_genm2l_GENMZ_2015MC = 'genm2l_GENMZ_2015MC_'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
  paraConfigs['mc_DY15_genm2l_GENMZ_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_v4,
  'rootPath2': mc2015_dy_path_v4,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 80, 100],
  'vars1': ['GENmass2l'],
  'vars2': ['genzm'],
  'cuts1': [skimmedDY_cut + cut_fixOneMu + ' && genLep_pt1 > 0 && genLep_pt2 > 0'], #
  'cuts2': [skimmedDY_cut + cut_fixOneMu + ' && genLep_pt1 > 0 && genLep_pt2 > 0'], #
  'weight1': ['1'],
  'weight2': ['1'],
  'xTitle': 'massZ(GeV)',
  'yTitle': 'Rate/'+str(20/100)+' GeV',
  'legend1': '2015MC, GENmass2l',
  'legend2': '2015MC, GENMZ',
  'savePath': savePath,
  'saveName': saveName_genm2l_GENMZ_2015MC, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }

  cut_fixOneMu_cutOnGEN = ' ( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9 &&  \
                     genLep_pt2 > ' + str(mu_ptBins[i])+' && genLep_pt2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1]) + ') || '\
                +' ( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9 &&  \
                     genLep_pt1 > ' + str(mu_ptBins[i])+' && genLep_pt1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) + ')'


  #CUT ON GEN, compare genm2l and massZ for 2015MC in different pt-eta bin
  saveName = 'genm2l_massZ_2015MC_cutOnGEN_'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
  paraConfigs['mc_DY15_genm2l_GENMZ_cutOnGEN_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_v4,
  'rootPath2': mc2015_dy_path_v4,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 80, 100],
  'vars1': ['GENmass2l'],
  'vars2': ['massZ'],
  'cuts1': [skimmedDY_cutOnGEN + cut_fixOneMu_cutOnGEN + ' && genLep_pt1 > 0 && genLep_pt2 > 0'], #
  'cuts2': [skimmedDY_cutOnGEN + cut_fixOneMu_cutOnGEN + ' && genLep_pt1 > 0 && genLep_pt2 > 0'], #
  'weight1': ['1'],
  'weight2': ['1'],
  'xTitle': 'massZ(GeV)',
  'yTitle': 'Rate/'+str(20/100)+' GeV',
  'legend1': '2015MC, GENmass2l',
  'legend2': '2015MC, massZ',
  'savePath': savePath,
  'saveName': saveName, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }

#compare genMZ and recoMZ for 2016MC in different pt-eta bin
  saveName_genZ_recoZ_2016MC = 'genZ_recoZ_2016MC_'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
  paraConfigs['mc_DY16_genZ_recoZ_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2016_dy_path,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 80, 100],
  'vars1': ['genzm'],
  'vars2': ['massZ'],
  'cuts1': [skimmedDY_cut + cut_fixOneMu], #
  'cuts2': [skimmedDY_cut + cut_fixOneMu], #
  'weight1': ['1'],
  'weight2': ['1'],
  'xTitle': 'massZ(GeV)',
  'yTitle': 'Rate/'+str(20/100)+' GeV',
  'legend1': '2016MC, m_{Z}^{GEN}',
  'legend2': '2016MC, m_{Z}^{RECO}',
  'savePath': savePath,
  'saveName': saveName_genZ_recoZ_2016MC, #
  'latexNote1': latexNote1_mu_pt_eta,
  'latexNote2': latexNote2_mu_pt_eta
  }


  #compare genzm between 2015 and 2016
  saveName_genZ_2015MC_2016MC = 'genZ_2015MC_2016MC'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
  paraConfigs['mc_DY15_DY16_genz_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_v4,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [50, 80, 100],
  'vars1': ['genzm'],
  'vars2': ['genzm'],
  'cuts1': [skimmedDY_cut + cut_fixOneMu], #
  'cuts2': [skimmedDY_cut + cut_fixOneMu], #
  'weight1': ['1'],
  'weight2': ['1'],
  'xTitle': 'massZ(GeV)',
  'yTitle': 'Rate/'+str(20/50)+' GeV',
  'legend1': '2015MC, m_{Z}^{GEN}',
  'legend2': '2016MC, m_{Z}^{GEN}',
  'savePath': savePath,
  'saveName': saveName_genZ_2015MC_2016MC, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }
  #compare reco between 2015 and 2016
  saveName_recoZ_2015MC_2016MC = 'recoZ_2015MC_2016MC'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
  paraConfigs['mc_DY15_DY16_recoz_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_v4,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [50, 80, 100],
  'vars1': ['massZ'],
  'vars2': ['massZ'],
  'cuts1': [skimmedDY_cut + cut_fixOneMu], #
  'cuts2': [skimmedDY_cut + cut_fixOneMu], #
  'weight1': ['1'],
  'weight2': ['1'],
  'xTitle': 'massZ(GeV)',
  'yTitle': 'Rate/'+str(20/50)+' GeV',
  'legend1': '2015MC, m_{Z}^{RECO}',
  'legend2': '2016MC, m_{Z}^{RECO}',
  'savePath': savePath,
  'saveName': saveName_recoZ_2015MC_2016MC, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }

  #compare pull of mZ between 2015 and 2016 MC
  saveName_pullZ_2015MC_2016MC = 'pullZ_2015MC_2016MC'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1])
  paraConfigs['mc_DY15_DY16_pullz_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_v4,
  'rootPath2': mc2016_dy_path,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, -3, 3],
  'vars1': ['(massZ-GENmass2l)/massZErr'],
  'vars2': ['(massZ-genzm)/massZErr'],
  'cuts1': [skimmedDY_cut + cut_fixOneMu + ' && GENmass2l'], #
  'cuts2': [skimmedDY_cut + cut_fixOneMu], #
  'weight1': ['1'],
  'weight2': ['1'],
  'xTitle': '(massZ_{reco}-GENmass2l)/massZErr',
  'yTitle': '',
  'legend1': '2015MC',
  'legend2': '2016MC',
  'savePath': savePath,
  'saveName': saveName_pullZ_2015MC_2016MC, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }


 
  #compare mu pt at gen and reco level
  skimmedDY_cut_gen = 'genzm > 80 && genzm < 100 && Met < 30 && genLep_pt1 > 0 && genLep_pt2 > 0 && '

  cut_mu1_pt_eta_gen = 'genLep_pt1 > '+str(mu_ptBins[i])+' && genLep_pt1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1])
  cut_mu2_pt_eta_gen = 'genLep_pt2 > '+str(mu_ptBins[i])+' && genLep_pt2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1])

  saveName_mu_pt_gen_reco = 'mu_pt_gen_reco_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2015MC'
  latexNote1_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T}^{reco} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])
  latexNote2_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T}^{gen} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

#  mc2015_dy_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/'
#  mc2016_dy_path = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/makeSlimTree/'
  paraConfigs['mc_DY15_muPt_gen_reco_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_withgenpt,
  'rootPath2': mc2015_dy_path_withgenpt,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 10, 100],
  'vars1': ['pT1', 'pT2'],
  'vars2': ['genLep_pt1', 'genLep_pt2'],
  'cuts1': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'cuts2': [skimmedDY_cut_gen + cut_mu1_pt_eta_gen, skimmedDY_cut_gen + cut_mu2_pt_eta_gen], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1'],
  'xTitle': 'muon p_{T} error(GeV)',
  'yTitle': 'Rate/'+str(90/100)+' GeV',
  'legend1': '2015MC, DY, RECO',
  'legend2': '2015MC, DY, GEN',
  'savePath': savePath,
  'saveName': saveName_mu_pt_gen_reco, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }
 
  saveName_mu_pt_gen_reco = 'mu_pt_gen_reco_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2016MC'

  paraConfigs['mc_DY16_muPt_gen_reco_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2016_dy_path_withgenpt,
  'rootPath2': mc2016_dy_path_withgenpt,
  'rootfile1': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2_m2mu.root',
  'rootfile2': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2_m2mu.root',
  'tree1': 'passedEvents',
  'tree2': 'passedEvents',
  'binInfo': [100, 10, 100],
  'vars1': ['pT1', 'pT2'],
  'vars2': ['genLep_pt1', 'genLep_pt2'],
  'cuts1': [skimmedDY_cut + cut_mu1_pt_eta, skimmedDY_cut + cut_mu2_pt_eta], #
  'cuts2': [skimmedDY_cut_gen + cut_mu1_pt_eta_gen, skimmedDY_cut_gen + cut_mu2_pt_eta_gen], #
  'weight1': ['1', '1'],
  'weight2': ['1', '1'],
  'xTitle': 'muon p_{T} error(GeV)',
  'yTitle': 'Rate/'+str(90/100)+' GeV',
  'legend1': '2016MC, DY, RECO',
  'legend2': '2016MC, DY, GEN',
  'savePath': savePath,
  'saveName': saveName_mu_pt_gen_reco, #
  'latexNote1': latexNote1_mu_pt_eta, #
  'latexNote2': latexNote2_mu_pt_eta
  }


saveName = 'pullZ_2015MC'
paraConfigs['mc_DY15_pullz'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2016_dy_path,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(massZ-GENmass2l)/massZErr'],
'vars2': ['(massZ-genzm)/massZErr'],
'cuts1': [skimmedDY_cut + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'cuts2': [skimmedDY_cut + cut_fixOneMu], #
'weight1': ['1'],
'weight2': ['1'],
'xTitle': '(massZ_{reco}-GENmass2l)/massZErr',
'yTitle': '',
'legend1': '2015MC',
'legend2': '2016MC',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}

cut_hasLeg1 = ' ((pT2 > 40 && pT2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) || (pT1 > 40 && pT1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9))'

saveName = 'pullZ_2015MC_hasLeg1'
paraConfigs['mc_DY15_pullz_hasLeg1'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2016_dy_path,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(massZ-GENmass2l)/massZErr'],
'vars2': ['(massZ-genzm)/massZErr'],
'cuts1': [skimmedDY_cut + cut_hasLeg1 + ' && genLep_pt1 > 0 && genLep_pt2 > 0'], #
'cuts2': [skimmedDY_cut + cut_fixOneMu], #
'weight1': ['1'],
'weight2': ['1'],
'xTitle': '(massZ_{reco}-GENmass2l)/massZErr',
'yTitle': '',
'legend1': '2015MC',
'legend2': '2016MC',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'pullZ_2015MC_noRECOfsr'
paraConfigs['mc_DY15_pullz_noRECOfsr'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2016_dy_path,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(massZ-GENmass2l)/massZErr'],
'vars2': ['(massZ-genzm)/massZErr'],
'cuts1': [skimmedDY_cut + ' genLep_pt1 > 0 && genLep_pt2 > 0 && nFSRPhotons == 0'], #
'cuts2': [skimmedDY_cut + cut_fixOneMu], #
'weight1': ['1'],
'weight2': ['1'],
'xTitle': '(massZ_{reco}-GENmass2l)/massZErr',
'yTitle': '',
'legend1': '2015MC',
'legend2': '2016MC',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY_MC_genPt1_genPt2'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [90, 10, 100],
'vars1': ['genLep_pt1 > genLep_pt2 ? genLep_pt1 : genLep_pt2'],
'vars2': ['genLep_pt1 <= genLep_pt2 ? genLep_pt1 : genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'cuts2': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'pT_{GEN}',
'yTitle': '',
'legend1': '2015MC-leading',
'legend2': '2015MC-subleading',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY_MC_eta1_eta2'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 2.4],
'vars1': ['genLep_pt1 > genLep_pt2 ? abs(eta1) : abs(eta2)'],
'vars2': ['genLep_pt1 <= genLep_pt2 ? abs(eta1) : abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'cuts2': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'eta',
'yTitle': '',
'legend1': '2015MC-leading',
'legend2': '2015MC-subleading',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY15_MC_genLepPhi_bigRelErr_smallRelErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -4, 4],
'vars1': ['genLep_phi1', 'genLep_phi2'],
'vars2': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.025', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.025'], #
'cuts2': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.015', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.015'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'phi',
'yTitle': '',
'legend1': 'pterr/pt > 0.025',
'legend2': 'pterr/pt < 0.015',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY15_MC_genLepPhi_ifEtaSmallerThan0p9_bigRelErr_smallRelErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -4, 4],
'vars1': ['genLep_phi1', 'genLep_phi2'],
'vars2': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.025 && abs(genLep_eta1) < 0.9', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.025 && abs(genLep_eta2) < 0.9'], #
'cuts2': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.015 && abs(genLep_eta1) < 0.9', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.015 && abs(genLep_eta2) < 0.9'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'phi',
'yTitle': '',
'legend1': 'pterr/pt > 0.025',
'legend2': 'pterr/pt < 0.015',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}

saveName = 'DY15_MC_genLepPhi_ifEta_1_1p6_bigRelErr_smallRelErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -4, 4],
'vars1': ['genLep_phi1', 'genLep_phi2'],
'vars2': ['genLep_phi1', 'genLep_phi2'], 
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.025 && abs(genLep_eta1) < 1.6 && abs(genLep_eta1) > 1', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.025 && abs(genLep_eta2) < 1.6 && abs(genLep_eta2) > 1'], #
'cuts2': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.015 && abs(genLep_eta1) < 1.6 && abs(genLep_eta1) > 1', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.015 && abs(genLep_eta2) < 1.6 && abs(genLep_eta2) > 1'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'phi',
'yTitle': '',
'legend1': 'pterr/pt > 0.025',
'legend2': 'pterr/pt < 0.015',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}

saveName = 'DY15_MC_genLepPhi_ifEtaSmallerThan0p5_bigRelErr_smallRelErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -4, 4],
'vars1': ['genLep_phi1', 'genLep_phi2'],
'vars2': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.025 && abs(genLep_eta1) < 0.5', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.025 && abs(genLep_eta2) < 0.5'], #
'cuts2': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.015 && abs(genLep_eta1) < 0.5', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.015 && abs(genLep_eta2) < 0.5'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'phi',
'yTitle': '',
'legend1': 'pterr/pt > 0.025',
'legend2': 'pterr/pt < 0.015',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY15_MC_genLepPhi_ifEtaSmallerThan0p2_bigRelErr_smallRelErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [50, -4, 4],
'vars1': ['genLep_phi1', 'genLep_phi2'],
'vars2': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.025 && abs(genLep_eta1) < 0.2', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.025 && abs(genLep_eta2) < 0.2'], #
'cuts2': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.015 && abs(genLep_eta1) < 0.2', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.015 && abs(genLep_eta2) < 0.2'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'phi',
'yTitle': '',
'legend1': 'pterr/pt > 0.025',
'legend2': 'pterr/pt < 0.015',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY15_MC_genLepPhi_ifEtaSmallerThan0p1_bigRelErr_smallRelErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [1000, -4, 4],
'vars1': ['genLep_phi1', 'genLep_phi2'],
'vars2': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.025 && abs(genLep_eta1) < 0.1', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.025 && abs(genLep_eta2) < 0.1'], #
'cuts2': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.015 && abs(genLep_eta1) < 0.1', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.015 && abs(genLep_eta2) < 0.1'], #
#'cuts1': ['genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.025 && abs(genLep_eta1) < 0.1', \
#          'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.025 && abs(genLep_eta2) < 0.1'], #
#'cuts2': ['genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.015 && abs(genLep_eta1) < 0.1', \
#          'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.015 && abs(genLep_eta2) < 0.1'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'phi',
'yTitle': '',
'legend1': 'pterr/pt > 0.025',
'legend2': 'pterr/pt < 0.015',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}



saveName = 'DY15_MC_genLepPhi_bigRelErr_smallRelErr_eta_0p1_0p8'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -4, 4],
'vars1': ['genLep_phi1', 'genLep_phi2'],
'vars2': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.02 && abs(genLep_eta1) < 0.8 && abs(genLep_eta1) > 0.1', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.02 && abs(genLep_eta2) < 0.8 && abs(genLep_eta2) > 0.1'], #
'cuts2': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.015 && abs(genLep_eta1) < 0.8 && abs(genLep_eta1) > 0.1', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.015 && abs(genLep_eta2) < 0.8 && abs(genLep_eta2) > 0.1'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'phi',
'yTitle': '',
'legend1': 'pterr/pt > 0.02',
'legend2': 'pterr/pt < 0.015',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY15_MC_genLepPhi_bigRelErr_smallRelErr_eta_1p3_1p5'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -4, 4],
'vars1': ['genLep_phi1', 'genLep_phi2'],
'vars2': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 > 0.025 && abs(genLep_eta1) < 1.5 && abs(genLep_eta1) > 1.3', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 > 0.025 && abs(genLep_eta2) < 1.5 && abs(genLep_eta2) > 1.3'], #
'cuts2': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && pterr1/genLep_pt1 < 0.02 && abs(genLep_eta1) < 1.5 && abs(genLep_eta1) > 1.3', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && pterr2/genLep_pt2 < 0.02 && abs(genLep_eta2) < 1.5 && abs(genLep_eta2) > 1.3'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'phi',
'yTitle': '',
'legend1': 'pterr/pt > 0.025',
'legend2': 'pterr/pt < 0.02',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}



saveName = 'DY15_MC_relMassZErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 0.05],
'vars1': ['massZErr/massZ'],
'vars2': ['massZErr/massZ'],
'cuts1': [skimmedDY_cut + '1' ],
'cuts2': [skimmedDY_cut + '1' ],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZErr/massZ',
'yTitle': '',
'legend1': '',
'legend2': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}

saveName = 'DY15_MC_massZErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootPath2': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 5],
'vars1': ['massZErr'],
'vars2': ['massZErr'],
'cuts1': [skimmedDY_cut + '1' ],
'cuts2': [skimmedDY_cut + '1' ],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZErr',
'yTitle': '',
'legend1': '',
'legend2': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY15_MC_GENZM_recoZcut_80_100'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootPath2': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'vars2': ['genzm'],
'cuts1': [' genzm > 80 && genzm < 100' ],
'cuts2': [' genzm > 80 && genzm < 100 && massZ > 80 && massZ < 100' ],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENZM',
'yTitle': '',
'legend1': 'no massZ_{reco} cut',
'legend2': '80 < massZ_{reco} < 100',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'bw'
}

saveName = 'DY15_MC_GENZM_recoZcut_70_110'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootPath2': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [120, 70, 110],
'vars1': ['genzm'],
'vars2': ['genzm'],
'cuts1': [' genzm > 70 && genzm < 110' ],
'cuts2': [' genzm > 70 && genzm < 110 && massZ > 70 && massZ < 110' ],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENZM',
'yTitle': '',
'legend1': 'no massZ_{reco} cut',
'legend2': '70 < massZ_{reco} < 110',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'bw'
}


saveName = 'DY15_MC_GENZM_recoZcut_60_120'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootPath2': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [140, 60, 120],
'vars1': ['genzm'],
'vars2': ['genzm'],
'cuts1': [' genzm > 60 && genzm < 120' ],
'cuts2': [' genzm > 60 && genzm < 120 && massZ > 60 && massZ < 120' ],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENZM',
'yTitle': '',
'legend1': 'no massZ_{reco} cut',
'legend2': '60 < massZ_{reco} < 120',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'bw'
}


saveName = 'DY_2015_pTErr_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'rootPath2': mc2015_dy_path_v4_NoMZCut,
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 10],
'vars1': ['pterr1', 'pterr2'],
'vars2': ['pterr1', 'pterr2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8',\
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'],
'cuts2': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8',\
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'latexNote2': ' ',
'legend1': '',
'legend2': '',
'doFit': False,
'pdfName': 'bw'
}

saveName = 'DY_2015_relpTErr_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'rootPath2': mc2015_dy_path_v4_NoMZCut,
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 0.1],
'vars1': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'vars2': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8',\
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'],
'cuts2': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8',\
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'latexNote2': ' ',
'legend1': '',
'legend2': '',
'doFit': False,
'pdfName': 'bw'
}


saveName = 'DY_2015_eta_eta_1p57_2p5_diffrelPtErr_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'rootPath2': mc2015_dy_path_v4_NoMZCut,
'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 1.5, 2.6],
'vars1': ['abs(genLep_eta1)', 'abs(genLep_eta2)'],
'vars2': ['abs(genLep_eta1)', 'abs(genLep_eta2)'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2.5 && abs(genLep_eta1) > 1.57 && pterr1/genLep_pt1 < 0.02',\
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2.5 && abs(genLep_eta2) > 1.57 && pterr2/genLep_pt2 < 0.02'],
'cuts2': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2.5 && abs(genLep_eta1) > 1.57 && pterr1/genLep_pt1 > 0.028 ',\
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2.5 && abs(genLep_eta2) > 1.57 && pterr2/genLep_pt2 > 0.028 '], #
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'eta',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'latexNote2': ' ',
'legend1': 'pterr/pt < 0.02',
'legend2': 'pterr/pt > 0.028',
'doFit': False,
'pdfName': 'bw'
}
 
