paraConfigs = { }

mc2015_dy_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/inputRootFiles/'
mc2016_dy_path = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/inputRoot/forApproval/'
mc2015_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/'
mc2016_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/makeSlimTree/'
mc2015_H_path = '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_Run1Fid_20160222/'
mc2016_H_path = '/cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/'

mc2015_dy_path_v4_NoMZCut = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4_NOmassZCut/"

mc2015_dy_path_kalmanv4_hasGENm2l = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4/'

savePath = '/home/mhl/public_html/2017/20170118_test/'

skimmedDY_cut = 'massZ > 80 && massZ < 100 && massZErr > 0.2 && massZErr < 7.2 && Met < 30 && ' 
skimmedDY_cutOnGEN = 'GENmass2l > 80 && GENmass2l < 100 && '
H_MC_cut = 'passedFullSelection && mass4l > 105 && mass4l < 140 && '

mu_ptBins = [10, 40, 50, 100]
mu_etaBins = [0.0, 0.9, 1.2, 2.4]

for i in range(len(mu_ptBins)-1):
 for j in range(len(mu_etaBins)-1):

  cut_mu1_pt_eta = ' (pT1 > '+str(mu_ptBins[i])+' && pT1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) + ')'
  cut_mu2_pt_eta = ' (pT2 > '+str(mu_ptBins[i])+' && pT2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1]) + ')'

  cut_mu1 = '(abs(pT1-genLep_pt1) <  abs(pT2-genLep_pt1) ? ' + cut_mu1_pt_eta + ' : ' + cut_mu2_pt_eta + ')'
  cut_mu2 = '(abs(pT2-genLep_pt2) <  abs(pT1-genLep_pt2) ? ' + cut_mu2_pt_eta + ' : ' + cut_mu1_pt_eta + ')'

  saveName_mu_pt_gen_reco_15MC = 'mu_pt_gen_reco_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_15mc' 
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_15_DY_pt_gen_reco_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_withgenpt,
  'rootfile1': 'DYJetsToLL_M-50_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [100, 10, 100],
  'binInfo_y': [100, 10, 100],
  'vars1_x': ['genLep_pt1', 'genLep_pt2'],
  'vars1_y': ['(abs(pT1-genLep_pt1) <  abs(pT2-genLep_pt1) ? pT1 : pT2)', '(abs(pT2-genLep_pt2) <  abs(pT1-genLep_pt2) ? pT2 : pT1)'],
  'cuts1': [skimmedDY_cut + cut_mu1, skimmedDY_cut + cut_mu2], # 
  'weight1': ['1', '1'],
  'xTitle': 'p_{T}^{GEN}(GeV)',
  'yTitle': 'p_{T}^{RECO}(GeV)',
  'savePath': savePath,
  'saveName': saveName_mu_pt_gen_reco_15MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  }
#  print paraConfigs['mc_15_DY_pt_gen_reco_'+str(i*(len(mu_ptBins)-2)+i+j)]['cuts1']

for i in range(len(mu_ptBins)-1):
 for j in range(len(mu_etaBins)-1):

  cut_mu1_pt_eta = ' (pT1 > '+str(mu_ptBins[i])+' && pT1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) + ')'
  cut_mu2_pt_eta = ' (pT2 > '+str(mu_ptBins[i])+' && pT2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1]) + ')'

  cut_mu1 = '(abs(pT1-genLep_pt1) <  abs(pT2-genLep_pt1) ? ' + cut_mu1_pt_eta + ' : ' + cut_mu2_pt_eta + ')'
  cut_mu2 = '(abs(pT2-genLep_pt2) <  abs(pT1-genLep_pt2) ? ' + cut_mu2_pt_eta + ' : ' + cut_mu1_pt_eta + ')'

  saveName_mu_pt_gen_reco_16MC = 'mu_pt_gen_reco_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_16mc' 
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_16_DY_pt_gen_reco_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2016_dy_path_withgenpt,
  'rootfile1': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [100, 10, 100],
  'binInfo_y': [100, 10, 100],
  'vars1_x': ['genLep_pt1', 'genLep_pt2'],
  'vars1_y': ['(abs(pT1-genLep_pt1) <  abs(pT2-genLep_pt1) ? pT1 : pT2)', '(abs(pT2-genLep_pt2) <  abs(pT1-genLep_pt2) ? pT2 : pT1)'],
  'cuts1': [skimmedDY_cut + cut_mu1, skimmedDY_cut + cut_mu2], # 
  'weight1': ['1', '1'],
  'xTitle': 'p_{T}^{GEN}(GeV)',
  'yTitle': 'p_{T}^{RECO}(GeV)',
  'savePath': savePath,
  'saveName': saveName_mu_pt_gen_reco_16MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  }


#gen z reco z
for i in range(len(mu_ptBins)-1):
 for j in range(len(mu_etaBins)-1):

  cut_mu1_pt_eta = ' (pT1 > '+str(mu_ptBins[i])+' && pT1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) + \
                 ' && pT2 > 40 && pT2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9 )'
  cut_mu2_pt_eta = ' (pT2 > '+str(mu_ptBins[i])+' && pT2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1]) + \
                 ' && pT1 > 40 && pT1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9 )'

  saveName_mz_gen_reco_16MC = 'mz_gen_reco_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_16mc'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_16_DY_mz_gen_reco_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2016_dy_path_withgenpt,
  'rootfile1': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [100, 80, 100],
  'binInfo_y': [100, 80, 100],
  'vars1_x': ['genzm'],
  'vars1_y': ['massZ'],
  'cuts1': [skimmedDY_cut + '(' + cut_mu1_pt_eta + '||' + cut_mu2_pt_eta + ')', skimmedDY_cut + '(' + cut_mu2_pt_eta + '||' + cut_mu1_pt_eta + ')'], # 
  'weight1': ['1', '1'],
  'xTitle': 'm_{Z}^{GEN}(GeV)',
  'yTitle': 'm_{Z}^{RECO}(GeV)',
  'savePath': savePath,
  'saveName': saveName_mz_gen_reco_16MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  }


#GENmass2l reco z
  hasOnlyTwoGENLeps = ' && genLep_pt1 > 0 && genLep_pt2 > 0'

  saveName_genm2l_recomz_15MC = 'genm2l_recomz_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_15mc'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_15_DY_genm2l_recomz_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [50, 80, 100],
  'binInfo_y': [50, 80, 100],
  'vars1_x': ['GENmass2l'],
  'vars1_y': ['massZ'],
  'cuts1': [skimmedDY_cut + '(' + cut_mu1_pt_eta + '||' + cut_mu2_pt_eta + ')'+ hasOnlyTwoGENLeps, \
            skimmedDY_cut + '(' + cut_mu2_pt_eta + '||' + cut_mu1_pt_eta + ')'+ hasOnlyTwoGENLeps], # 
  'weight1': ['1', '1'],
  'xTitle': 'GENmass2l(GeV)',
  'yTitle': 'massZ(GeV)',
  'savePath': savePath,
  'saveName': saveName_genm2l_recomz_15MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  }


#GENmass2l GENMZ
  saveName_genm2l_GENMZ_15MC = 'genm2l_GENMZ_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_15mc'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_15_DY_genm2l_GENMZ_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [50, 80, 100],
  'binInfo_y': [50, 80, 100],
  'vars1_x': ['genzm'],
  'vars1_y': ['GENmass2l'],
  'cuts1': [skimmedDY_cut + '(' + cut_mu1_pt_eta + '||' + cut_mu2_pt_eta + ')'+ hasOnlyTwoGENLeps, \
            skimmedDY_cut + '(' + cut_mu2_pt_eta + '||' + cut_mu1_pt_eta + ')'+ hasOnlyTwoGENLeps], # 
  'weight1': ['1', '1'],
  'xTitle': 'GENMZ(GeV)',
  'yTitle': 'GENmass2l(GeV)',
  'savePath': savePath,
  'saveName': saveName_genm2l_GENMZ_15MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  }


#massZ GENMZ 15MC
  saveName_massZ_GENMZ_15MC = 'massZ_GENMZ_pt'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_15mc'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_15_DY_massZ_GENMZ_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [50, 80, 100],
  'binInfo_y': [50, 80, 100],
  'vars1_x': ['genzm'],
  'vars1_y': ['massZ'],
  'cuts1': [skimmedDY_cut + '(' + cut_mu1_pt_eta + '||' + cut_mu2_pt_eta + ')'+ hasOnlyTwoGENLeps, \
            skimmedDY_cut + '(' + cut_mu2_pt_eta + '||' + cut_mu1_pt_eta + ')'+ hasOnlyTwoGENLeps], # 
  'weight1': ['1', '1'],
  'xTitle': 'GENMZ(GeV)',
  'yTitle': 'massZ(GeV)',
  'savePath': savePath,
  'saveName': saveName_massZ_GENMZ_15MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  }


# |massZ-GENmass2l| > 3, pt-eta

  saveName_massZ_GENmass2l_diffBig_ptEta_15MC = 'massZ_GENmass2l_diffBig_ptEta_'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_15mc'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_15_DY_massZ_GENmass2l_diffBig_ptEta_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [50, mu_etaBins[j], mu_etaBins[j+1]],
  'binInfo_y': [50, mu_ptBins[i], mu_ptBins[i+1]],
  'vars1_x': ['abs(eta1)', 'abs(eta2)'],
  'vars1_y': ['pT1', 'pT2'],
  'cuts1': [skimmedDY_cut + '(' + cut_mu1_pt_eta + ')'+ hasOnlyTwoGENLeps, \
            skimmedDY_cut + '(' + cut_mu2_pt_eta + ')'+ hasOnlyTwoGENLeps], # 
  'weight1': ['1', '1'],
  'xTitle': 'eta',
  'yTitle': 'pT(GeV)',
  'savePath': savePath,
  'saveName': saveName_massZ_GENmass2l_diffBig_ptEta_15MC, #
  'latexNote1': latexNote_mu_pt_eta, #
  }

  saveName = 'pT_GENpT_'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_15mc'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])

  paraConfigs['mc_15_DY_pT_GENpT_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [90, 10, 100],
  'binInfo_y': [90, 10, 100],
  'vars1_x': ['genLep_pt1', 'genLep_pt2'],
  'vars1_y': ['pT1', 'pT2'],
  'cuts1': [skimmedDY_cut + '(' + cut_mu1_pt_eta + '||' + cut_mu2_pt_eta + ')'+ hasOnlyTwoGENLeps, \
            skimmedDY_cut + '(' + cut_mu2_pt_eta + '||' + cut_mu2_pt_eta + ')'+ hasOnlyTwoGENLeps], # 
  'weight1': ['1', '1'],
  'xTitle': 'GENpT(GeV)',
  'yTitle': 'pT(GeV)',
  'savePath': savePath,
  'saveName': saveName, #
  'latexNote1': latexNote_mu_pt_eta, #
  }


  cutOnGEN_mu1_pt_eta = ' (genLep_pt1 > '+str(mu_ptBins[i])+' && genLep_pt1 < '+str(mu_ptBins[i+1])+' && abs(eta1) > '+str(mu_etaBins[j])+' && abs(eta1) < '+str(mu_etaBins[j+1]) + \
                 ' && genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9 )'
  cutOnGEN_mu2_pt_eta = ' (genLep_pt2 > '+str(mu_ptBins[i])+' && genLep_pt2 < '+str(mu_ptBins[i+1])+' && abs(eta2) > '+str(mu_etaBins[j])+' && abs(eta2) < '+str(mu_etaBins[j+1]) + \
                 ' && genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9 )'

  saveName = 'pT_GENpT_'+str(mu_ptBins[i])+'_'+str(mu_ptBins[i+1])+'_eta'+str(mu_etaBins[j])+'_'+str(mu_etaBins[j+1]) + '_2D_15mc_cutOnGEN'
  latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])
  paraConfigs['mc_15_DY_pT_GENpT_cutOnGEN_'+str(i*(len(mu_ptBins)-2)+i+j)] = \
  {\
  'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
  'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
  'tree1': 'passedEvents',
  'binInfo_x': [90, 10, 100],
  'binInfo_y': [90, 10, 100],
  'vars1_x': ['genLep_pt1', 'genLep_pt2'],
  'vars1_y': ['pT1', 'pT2'],
  'cuts1': [skimmedDY_cutOnGEN + '(' + cutOnGEN_mu1_pt_eta + '||' + cutOnGEN_mu2_pt_eta + ') && genLep_pt1 > 0 && genLep_pt2 > 0', \
            skimmedDY_cutOnGEN + '(' + cutOnGEN_mu2_pt_eta + '||' + cutOnGEN_mu2_pt_eta + ') && genLep_pt1 > 0 && genLep_pt2 > 0'], # 
  'weight1': ['1', '1'],
  'xTitle': 'GENpT(GeV)',
  'yTitle': 'pT(GeV)',
  'savePath': savePath,
  'saveName': saveName, #
  'latexNote1': latexNote_mu_pt_eta, #
  }

#### for all pT-eta bins ####
saveName = 'massZ_GENmass2l_diffBig_genpT1_genpT2_2015MC'
paraConfigs['mc_15_DY_massZ_GENmass2l_diffBig_genpT1_genpT2'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [45, 10, 55],
'binInfo_y': [45, 10, 55],
'vars1_x': ['genLep_pt1 > genLep_pt2 ? genLep_pt1 : genLep_pt2'],
'vars1_y': ['genLep_pt1 > genLep_pt2 ? genLep_pt2 : genLep_pt1'],
'cuts1': [skimmedDY_cut + 'GENmass2l > 0 && abs(massZ-GENmass2l) > 5'],
'weight1': ['1'],
'xTitle': 'pT1(GeV)',
'yTitle': 'pT2(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #latexNote_mu_pt_eta, #
}

saveName = 'massZ_GENmass2l_diffSmall_genpT1_genpT2_2015MC'
paraConfigs['mc_15_DY_massZ_GENmass2l_diffSmall_genpT1_genpT2'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [45, 10, 55],
'binInfo_y': [45, 10, 55],
'vars1_x': ['genLep_pt1 > genLep_pt2 ? genLep_pt1 : genLep_pt2'],
'vars1_y': ['genLep_pt1 > genLep_pt2 ? genLep_pt2 : genLep_pt1'],
'cuts1': [skimmedDY_cut + 'GENmass2l > 0 && abs(massZ-GENmass2l) < 2'],
'weight1': ['1'],
'xTitle': 'pT1(GeV)',
'yTitle': 'pT2(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #latexNote_mu_pt_eta, #
}


saveName = 'massZ_GENmass2l_diffBig_pT1_pT2_2015MC'
paraConfigs['mc_15_DY_massZ_GENmass2l_diffBig_pT1_pT2'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [45, 10, 55],
'binInfo_y': [45, 10, 55],
'vars1_x': ['pT1 > pT2 ? pT1 : pT2'],
'vars1_y': ['pT1 > pT2 ? pT2 : pT1'],
'cuts1': [skimmedDY_cut + 'GENmass2l > 0 && abs(massZ-GENmass2l) > 5'],
'weight1': ['1'],
'xTitle': 'pT1(GeV)',
'yTitle': 'pT2(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #latexNote_mu_pt_eta, #
}

saveName = 'massZ_GENmass2l_diffSmall_pT1_pT2_2015MC'
paraConfigs['mc_15_DY_massZ_GENmass2l_diffSmall_pT1_pT2'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [45, 10, 55],
'binInfo_y': [45, 10, 55],
'vars1_x': ['pT1 > pT2 ? pT1 : pT2'],
'vars1_y': ['pT1 > pT2 ? pT2 : pT1'],
'cuts1': [skimmedDY_cut + 'GENmass2l > 0 && abs(massZ-GENmass2l) < 2'],
'weight1': ['1'],
'xTitle': 'pT1(GeV)',
'yTitle': 'pT2(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #latexNote_mu_pt_eta, #
}


saveName = 'massZ_GENmass2l_diffBig_eta1_eta2_2015MC'
paraConfigs['mc_15_DY_massZ_GENmass2l_diffBig_eta1_eta2'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.4],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['genLep_pt1 > genLep_pt2 ? abs(eta1) : abs(eta2)'],
'vars1_y': ['genLep_pt1 > genLep_pt2 ? abs(eta2) : abs(eta1)'],
'cuts1': [skimmedDY_cut + 'GENmass2l > 0 && abs(massZ-GENmass2l) > 5'],
'weight1': ['1'],
'xTitle': '|#eta_{1}|',
'yTitle': '|#eta_{2}|',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #latexNote_mu_pt_eta, #
}

saveName = 'massZ_GENmass2l_diffSmall_eta1_eta2_2015MC'
paraConfigs['mc_15_DY_massZ_GENmass2l_diffSmall_eta1_eta2'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.4],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['genLep_pt1 > genLep_pt2 ? abs(eta1) : abs(eta2)'],
'vars1_y': ['genLep_pt1 > genLep_pt2 ? abs(eta2) : abs(eta1)'],
'cuts1': [skimmedDY_cut + 'GENmass2l > 0 && abs(massZ-GENmass2l) < 2'],
'weight1': ['1'],
'xTitle': '|#eta_{1}|',
'yTitle': '|#eta_{2}|',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #latexNote_mu_pt_eta, #
}


cut_hasLeg1 = ' ((pT2 > 40 && pT2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) || (pT1 > 40 && pT1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9))'
saveName = 'pT_GENpT_2D_15mc_hasLeg1'
#latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])
paraConfigs['mc_15_DY_pT_GENpT_hasLeg1'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [90, 10, 100],
'binInfo_y': [90, 10, 100],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pT1', 'pT2'],
'cuts1': [skimmedDY_cut + cut_hasLeg1 + ' && genLep_pt1 > 0 && genLep_pt2 > 0', \
          skimmedDY_cut + cut_hasLeg1 + ' && genLep_pt1 > 0 && genLep_pt2 > 0'], # 
'weight1': ['1', '1'],
'xTitle': 'GENpT(GeV)',
'yTitle': 'pT(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'pT_GENpT_2D_15mc'
#latexNote_mu_pt_eta = str(mu_ptBins[i])+'GeV < p_{T} < '+str(mu_ptBins[i+1])+'GeV, '+str(mu_etaBins[j])+' < |#eta| < '+str(mu_etaBins[j+1])
paraConfigs['mc_15_DY_pT_GENpT'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [90, 10, 100],
'binInfo_y': [90, 10, 100],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pT1', 'pT2'],
'cuts1': [skimmedDY_cut + ' genLep_pt1 > 0 && genLep_pt2 > 0', \
          skimmedDY_cut + ' genLep_pt1 > 0 && genLep_pt2 > 0'], # 
'weight1': ['1', '1'],
'xTitle': 'GENpT(GeV)',
'yTitle': 'pT(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ''#
}

saveName = 'pT_GENpT_leg2_2D_15mc_hasLeg1_cutOnGEN'
paraConfigs['mc_15_DY_pT_GENpT_leg2_hasLeg1_cutOnGEN'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [90, 10, 100],
'binInfo_y': [90, 10, 100],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pT1', 'pT2'],
'cuts1': [skimmedDY_cutOnGEN + ' (genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) && genLep_pt1 > 0 && genLep_pt2 > 0', \
          skimmedDY_cutOnGEN + ' (genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) && genLep_pt1 > 0 && genLep_pt2 > 0'], # 
'weight1': ['1', '1'],
'xTitle': 'GENpT(GeV)',
'yTitle': 'pT(GeV)',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'pT_GENpT_leg2_2D_15mc_oneLeg_in_pt10_40_eta0p0_0p9'
paraConfigs['mc_15_DY_pT_GENpT_leg2_oneLeg_in_pt10_40_eta0p0_0p9'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [90, 10, 100],
'binInfo_y': [90, 10, 100],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pT1', 'pT2'],
'cuts1': [skimmedDY_cut + ' (pT2 > 10 && pT2 < 40 && abs(eta2) > 0 && abs(eta2) < 0.9) && genLep_pt1 > 0 && genLep_pt2 > 0', \
          skimmedDY_cut + ' (pT1 > 10 && pT1 < 40 && abs(eta1) > 0 && abs(eta1) < 0.9) && genLep_pt1 > 0 && genLep_pt2 > 0'], # 
'weight1': ['1', '1'],
'xTitle': 'GENpT(GeV)',
'yTitle': 'pT(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'pT_etaT_leg2_2D_15mc_oneLeg_in_pt10_40_eta0p0_0p9'
paraConfigs['mc_15_DY_pT_eta_leg2_oneLeg_in_pt10_40_eta0p0_0p9'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.4],
'binInfo_y': [90, 10, 100],
'vars1_x': ['abs(eta1)', 'abs(eta2)'],
'vars1_y': ['pT1', 'pT2'],
'cuts1': [skimmedDY_cut + ' (pT2 > 10 && pT2 < 40 && abs(eta2) > 0 && abs(eta2) < 0.9) && genLep_pt1 > 0 && genLep_pt2 > 0', \
          skimmedDY_cut + ' (pT1 > 10 && pT1 < 40 && abs(eta1) > 0 && abs(eta1) < 0.9) && genLep_pt1 > 0 && genLep_pt2 > 0'], # 
'weight1': ['1', '1'],
'xTitle': 'GENpT(GeV)',
'yTitle': 'pT(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'pull_vs_massZ_15MC'
paraConfigs['pull_vs_massZ_15MC'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [50, -3, 3],
'vars1_x': ['massZ'],
'vars1_y': ['(massZ-GENmass2l)/massZErr'],
'cuts1': [skimmedDY_cut + 'genLep_pt1 > 0 && genLep_pt2 > 0'],
'weight1': ['1'],
'xTitle': 'massZ_{reco}(GeV)',
'yTitle': '(massZ-GENmass2l)/massZErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'pull_vs_GENmass2l_15MC'
paraConfigs['pull_vs_GENmass2l_15MC'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [50, -3, 3],
'vars1_x': ['GENmass2l'],
'vars1_y': ['(massZ-GENmass2l)/massZErr'],
'cuts1': [skimmedDY_cut + 'genLep_pt1 > 0 && genLep_pt2 > 0'],
'weight1': ['1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': '(massZ-GENmass2l)/massZErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


lep1Pt_40_50_eta_0_0p9 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) )'
lep2Pt_40_50_eta_0_0p9 = ' (( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [50, 10, 100],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['genLep_pt1','genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9, \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 ],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'pT_{GEN}(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

lep1Pt_40_50_eta_0_0p9 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) )'
lep2Pt_40_50_eta_0_0p9 = ' (( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l_otherGENMu_eta_0_0p1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [50, 10, 100],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['genLep_pt1','genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && abs(eta1) > 0 && abs(eta1) < 0.1', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && abs(eta2) > 0 && abs(eta2) < 0.1'],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'pT_{GEN}(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

lep1Pt_40_50_eta_0_0p9 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) )'
lep2Pt_40_50_eta_0_0p9 = ' (( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l_otherGENMu_eta_0p9_1p1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [50, 10, 100],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['genLep_pt1','genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && abs(eta1) > 0.9 && abs(eta1) < 1.1', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && abs(eta2) > 0.9 && abs(eta2) < 1.1'],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'pT_{GEN}(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

lep1Pt_40_50_eta_0_0p9 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) )'
lep2Pt_40_50_eta_0_0p9 = ' (( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l_otherGENMu_eta_2p1_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [50, 10, 100],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['genLep_pt1','genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && abs(eta1) > 2.1 && abs(eta1) < 2.4', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && abs(eta2) > 2.1 && abs(eta2) < 2.4'],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'pT_{GEN}(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


lep1Pt_40_50_eta_0_0p9 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) )'
lep2Pt_40_50_eta_0_0p9 = ' (( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_eta_vs_GENmass2l'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['abs(eta1)','abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9, \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 ],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_eta_vs_GENmass2l_otherGENMu_pT_44_46'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['abs(eta1)','abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && genLep_pt1 > 44 && genLep_pt1 < 46', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && genLep_pt2 > 44 && genLep_pt2 < 46'],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_eta_vs_GENmass2l_otherGENMu_pT_40_42'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['abs(eta1)','abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && genLep_pt1 > 40 && genLep_pt1 < 42', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && genLep_pt2 > 40 && genLep_pt2 < 42'],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_eta_vs_GENmass2l_otherGENMu_pT_50_52'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['abs(eta1)','abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && genLep_pt1 > 50 && genLep_pt1 < 52', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && genLep_pt2 > 50 && genLep_pt2 < 52'],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'fixOneGENMu_pT_40_50_0_0p9_GENmass2l_90_92_plotOtherGENMu_pT_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 10, 100],
'binInfo_y': [50, 0, 2.4],
'vars1_x': ['genLep_pt1','genLep_pt2'],
'vars1_y': ['abs(eta1)','abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && GENmass2l > 90 && GENmass2l < 92', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && GENmass2l > 90 && GENmass2l < 92'],
'weight1': ['1','1'],
'xTitle': 'pT_{GEN}',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'fixOneGENMu_pT_40_50_0_0p9_GENmass2l_80_87_plotOtherGENMu_pT_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 10, 100],
'binInfo_y': [50, 0, 2.4],
'vars1_x': ['genLep_pt1','genLep_pt2'],
'vars1_y': ['abs(eta1)','abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && GENmass2l > 80 && GENmass2l < 87', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && GENmass2l > 80 && GENmass2l < 87'],
'weight1': ['1','1'],
'xTitle': 'pT_{GEN}',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'fixOneGENMu_pT_40_50_0_0p9_GENmass2l_95_100_plotOtherGENMu_pT_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 10, 100],
'binInfo_y': [50, 0, 2.4],
'vars1_x': ['genLep_pt1','genLep_pt2'],
'vars1_y': ['abs(eta1)','abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && GENmass2l > 95 && GENmass2l < 100', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && GENmass2l > 95 && GENmass2l < 100'],
'weight1': ['1','1'],
'xTitle': 'pT_{GEN}',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}










lep1Pt_40_50_eta_0_0p9 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) )'
lep2Pt_40_50_eta_0_0p9 = ' (( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l_genzm_88_94'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [50, 10, 100],
'vars1_x': ['GENmass2l','GENmass2l'],
'vars1_y': ['genLep_pt1','genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && genzm > 88 && genzm < 94', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && genzm > 88 && genzm < 94'],
'weight1': ['1','1'],
'xTitle': 'GENmass2l(GeV)',
'yTitle': 'pT_{GEN}(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


lep1Pt_40_50_eta_0_0p9 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) )'
lep2Pt_40_50_eta_0_0p9 = ' (( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENMZ_genzm_88_94'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 80, 100],
'binInfo_y': [50, 10, 100],
'vars1_x': ['genzm','genzm'],
'vars1_y': ['genLep_pt1','genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep2Pt_40_50_eta_0_0p9 + ' && genzm > 88 && genzm < 94', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && ' + lep1Pt_40_50_eta_0_0p9 + ' && genzm > 88 && genzm < 94'],
'weight1': ['1','1'],
'xTitle': 'GENMZ(GeV)',
'yTitle': 'pT_{GEN}(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_leadGENpT_subGENpT'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 10, 100],
'binInfo_y': [100, 10, 100],
'vars1_x': ['genLep_pt1 > genLep_pt2 ? genLep_pt1 : genLep_pt2'],
'vars1_y': ['genLep_pt1 < genLep_pt2 ? genLep_pt1 : genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1'],
'xTitle': 'leading_pt(GeV)',
'yTitle': 'subleading_pt(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_GENpT1_GENpT2'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 10, 100],
'binInfo_y': [100, 10, 100],
'vars1_x': ['eta1 > eta2 ? genLep_pt1 : genLep_pt2'],
'vars1_y': ['eta1 < eta2 ? genLep_pt1 : genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1'],
'xTitle': 'biggerEta_pt(GeV)',
'yTitle': 'smallerEta_pt(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_GENpT1_GENpT2_eta_0'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 10, 100],
'binInfo_y': [100, 10, 100],
'vars1_x': ['phi1 > phi2 ? genLep_pt1 : genLep_pt2'],
'vars1_y': ['phi1 < phi2 ? genLep_pt1 : genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && (abs(eta1)-0 < 0.05) && (abs(eta2) - 0 < 0.05)'],
'weight1': ['1'],
'xTitle': 'biggerPhi_pt(GeV)',
'yTitle': 'smallerPhi_pt(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_phi1_phi2_eta_0'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.15, 3.15],
'binInfo_y': [100, -3.15, 3.15],
'vars1_x': ['phi1'],
'vars1_y': ['phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && (abs(eta1)-0 < 0.05) && (abs(eta2) - 0 < 0.05)'],
'weight1': ['1'],
'xTitle': 'phi1(GeV)',
'yTitle': 'phi2(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_leadGENpT_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 10, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['genLep_pt1 > genLep_pt2 ? genLep_pt1 : genLep_pt2'],
'vars1_y': ['genLep_pt1 > genLep_pt2 ? abs(eta1) : abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1'],
'xTitle': 'leading_pt(GeV)',
'yTitle': 'leadingpT_eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_subleadGENpT_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 10, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['genLep_pt1 < genLep_pt2 ? genLep_pt1 : genLep_pt2'],
'vars1_y': ['genLep_pt1 < genLep_pt2 ? abs(eta1) : abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1'],
'xTitle': 'subleading_pt(GeV)',
'yTitle': 'subleadingpT_eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_pTErr_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 2],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 ', skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_pTErr_phi'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents', 
'binInfo_x': [100, -3.14, 3.14],
'binInfo_y': [100, 0, 2],
'vars1_x': ['phi1', 'phi2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 ', skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_pTErr_RECOpT'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents', 
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 ', skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{RECO}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_pTErr_GENpT'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 ', skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_pTErr_GENpT_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 7, 100],
'binInfo_y': [100, 0, 2],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 ', skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErr_GENpT_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && abs(genLep_eta1) < 0.9', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && abs(genLep_eta2) < 0.9'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErr_GENpT_eta_0p9_1p8'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && abs(genLep_eta1) < 1.8 && abs(genLep_eta1) > 0.9', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && abs(genLep_eta2) < 1.8 && abs(genLep_eta2) > 0.9'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErr_GENpT_eta_1p8_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && abs(genLep_eta1) < 2.4 && abs(genLep_eta1) > 1.8', \
          skimmedDY_cutOnGEN + 'genLep_pt2 >5 && genLep_pt2 < 100 && abs(genLep_eta2) < 2.4 && abs(genLep_eta2) > 1.8'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrRECO_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents', 
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 ', skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY16_MC_relpTErrRECO_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2016_dy_path_withgenpt,
'rootfile1': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': [skimmedDY_cut+'1', skimmedDY_cut+'1'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY16_data_relpTErrRECO_eta'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/inputRootFiles/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': [skimmedDY_cut+'1', skimmedDY_cut+'1'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrRECO_phi'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.14, 3.14],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['phi1', 'phi2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 ', skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '',
'doLogZ':True #
}


saveName = 'DY15_MC_relpTErrGEN_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_relpTErrGEN_eta_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.5, 2.5],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt1 < 100',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 7 && genLep_pt2 < 100'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrGEN_eta_phiBiggerThan0'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents', 
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && genLep_phi1 > 0.5',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && genLep_phi2 > 0.5'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_relpTErrGEN_eta_phi_minus_0p8_minus_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents', 
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && (genLep_phi1 > -0.9 && genLep_phi1 < -0.8)',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && (genLep_phi2 > -0.9 && genLep_phi2 < -0.8)'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrGEN_eta_residual_0_0p01'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents', 
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && abs((pT1-genLep_pt1)/genLep_pt1)<0.01', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && abs((pT2-genLep_pt2)/genLep_pt2)<0.01'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrGEN_eta_residual_0_0p01_pull_0_1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents', 
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt1 < 100 && abs((pT1-genLep_pt1)/genLep_pt1)<0.01 && abs((pT1-genLep_pt1)/pterr1) < 1', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 5 && genLep_pt2 < 100 && abs((pT2-genLep_pt2)/genLep_pt2)<0.01 && abs((pT2-genLep_pt2)/pterr2) < 1'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrGEN_eta_pTSmallerThan50'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [500, -2.4, 2.4],
'binInfo_y': [500, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && genLep_pt1 < 50',\
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && genLep_pt2 < 50'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrGEN_phi'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.14, 3.14],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_phi1', 'genLep_phi2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 ', skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 '],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '',
'doLogZ':True #
}

saveName = 'DY15_MC_relpTErrGEN_phi_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.14, 3.14],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_phi1', 'genLep_phi2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt1 < 100 && abs(genLep_eta1) < 0.9',\
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 < 100 && abs(genLep_eta2) < 0.9 '],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '',
'doLogZ':True #
}

saveName = 'DY15_MC_relpTErrGEN_phi_eta_0p9_1p8'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.14, 3.14],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_phi1', 'genLep_phi2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt1 < 100 && abs(genLep_eta1) < 1.8 && abs(genLep_eta1) > 0.9',\
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 < 100 && abs(genLep_eta2) < 1.8 && abs(genLep_eta2) > 0.9'],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '',
'doLogZ':True #
}

saveName = 'DY15_MC_relpTErrGEN_phi_eta_1p8_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.14, 3.14],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_phi1', 'genLep_phi2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt1 < 100 && abs(genLep_eta1) < 2.4 && abs(genLep_eta1) > 1.8',\
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 < 100 && abs(genLep_eta2) < 2.4 && abs(genLep_eta2) > 1.8'],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '',
'doLogZ':True #
}


saveName = 'DY15_MC_pTErr_GENpT_eta_0.0_0.9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2], 
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta1) < 0.9', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta2) < 0.9'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_pTErr_GENpT_eta_0.2_0.9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta1) < 0.9 && abs(genLep_eta1) > 0.5', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta2) < 0.9 && abs(genLep_eta2) > 0.5'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_pTErr_GENpT_eta_0.9_1.2'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(eta1) < 1.2 && abs(eta1) > 0.9', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(eta2) < 1.2 && abs(eta2) > 0.9'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'DY15_MC_pTErr_GENpT_eta_0.9_1.8'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta1) < 1.8 && abs(genLep_eta1) > 0.9', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta2) < 1.8 && abs(genLep_eta2) > 0.9'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_pTErr_GENpT_eta_1.2_1.8'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(eta1) < 1.8 && abs(eta1) > 1.2', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(eta2) < 1.8 && abs(eta2) > 1.2'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_pTErr_GENpT_eta_1.8_2.4'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta1) < 2.4 && abs(genLep_eta1) > 1.8', \
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta2) < 2.4 && abs(genLep_eta2) > 1.8'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'p_{T} error(GeV)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrGEN_phi_eta_0p0_0p9_relpTErrbiggerThan0.02'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, -3.14, 3.14],
'binInfo_y': [50, 0, 0.1],
'vars1_x': ['phi1', 'phi2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(eta1) < 0.9 && pterr1/genLep_pt1 > 0.02',\
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(eta2) < 0.9 && pterr2/genLep_pt2 > 0.02'],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErrGEN_phi_eta_0p0_0p1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [200, -3.14, 3.14],
'binInfo_y': [200, 0, 0.1],
'vars1_x': ['phi1', 'phi2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(eta1) < 0.1',\
          skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && abs(eta2) < 0.1'],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_eta_phi_relpTErrGENBiggerThan0.02_eta_0p0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.14, 3.14],
'binInfo_y': [100, 0, 1],
'vars1_x': ['phi1', 'phi2'],
'vars1_y': ['abs(eta1)', 'abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt1 < 50 && abs(eta1) < 0.9 && pterr1/genLep_pt1 > 0.02',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 < 50 && abs(eta2) < 0.9 && pterr2/genLep_pt2 > 0.02'],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'abs|#eta|',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_eta_phi_relpTErrGENBiggerThan0.02_eta_0p0_0p1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.14, 3.14],
'binInfo_y': [1, 0, 0.1],
'vars1_x': ['phi1', 'phi2'],
'vars1_y': ['abs(eta1)', 'abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt1 < 70 && abs(eta1) < 0.1 && pterr1/genLep_pt1 > 0.014',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 < 70 && abs(eta2) < 0.1 && pterr2/genLep_pt2 > 0.014'],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': 'abs|#eta|',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}


saveName = 'DY15_MC_eta1_eta2_relpTErrGENBiggerThan0.02_eta1_0p0_0p1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 1],
'binInfo_y': [100, 0, 1],
'vars1_x': ['abs(eta1)'],
'vars1_y': ['abs(eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt1 < 70 && abs(eta1) < 0.1 && pterr1/genLep_pt1 > 0.014'],#,\
#          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 < 70 && abs(eta1) < 0.1 && pterr2/genLep_pt1 > 0.014'],
'weight1': ['1','1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}

saveName = 'DY15_MC_pTResidual_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['(pT1-genLep_pt1)/genLep_pt1', '(pT2-genLep_pt2)/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 > 0'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': '(pT_{reco}-pT_{gen})/pT_{gen}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}


saveName = 'DY15_MC_pTResidual_phi'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.15, 3.15],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['genLep_phi1', 'genLep_phi2'],
'vars1_y': ['(pT1-genLep_pt1)/genLep_pt1', '(pT2-genLep_pt2)/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 > 0'],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': '(pT_{reco}-pT_{gen})/pT_{gen}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}


saveName = 'DY15_MC_pTPull_eta'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, -3, 3],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['(pT1-genLep_pt1)/pterr1', '(pT2-genLep_pt2)/pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 > 0'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': '(pT_{reco}-pT_{gen})/pTErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}


saveName = 'DY15_MC_pTPull_phi'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3.15, 3.15],
'binInfo_y': [100, -3, 3],
'vars1_x': ['genLep_phi1', 'genLep_phi2'],
'vars1_y': ['(pT1-genLep_pt1)/pterr1', '(pT2-genLep_pt2)/pterr2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 > 0'],
'weight1': ['1','1'],
'xTitle': 'phi',
'yTitle': '(pT_{reco}-pT_{gen})/pTErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}


saveName = 'DY15_MC_eta_phi_eta_0_0p9_relpTErr_big_0p02'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 0, 0.9],
'binInfo_y': [50, -4, 4],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt1 < 100 && abs(genLep_eta1) < 0.9 && pterr1/genLep_pt1 > 0.02',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 < 100 && abs(genLep_eta2) < 0.9 && pterr2/genLep_pt2 > 0.02'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'phi',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}



saveName = 'DY15_MC_eta_phi_eta_0p9_1p8_relpTErr_big_0p03'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 0.9, 1.8],
'binInfo_y': [50, -4, 4],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['genLep_phi1', 'genLep_phi2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt1 < 100 && abs(genLep_eta1) < 1.8 && abs(genLep_eta1) > 0.9 && pterr1/genLep_pt1 > 0.03',\
          skimmedDY_cutOnGEN + 'genLep_pt2 > 0 && genLep_pt2 < 100 && abs(genLep_eta2) < 1.8 && abs(genLep_eta2) > 0.9 && pterr2/genLep_pt2 > 0.03'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'phi',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}


saveName = 'DY15_eta1_eta2_relMassErr_smallerThan_0p009'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.4],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['abs(genLep_eta1)'],
'vars1_y': ['abs(genLep_eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && genLep_pt1 < 100 && genLep_pt2 < 100 && massZErr/massZ < 0.009'],
'weight1': ['1','1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}


saveName = 'DY15_eta1_eta2_relMassErr_biggerThan_0p009'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.4],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['abs(genLep_eta1)'],
'vars1_y': ['abs(genLep_eta2)'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 0 && genLep_pt2 > 0 && genLep_pt1 < 100 && genLep_pt2 < 100 && massZErr/massZ > 0.009'],
'weight1': ['1','1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}

saveName = 'DY15_massZErr_relmassZErr'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [10, 0.015, 0.026],
'binInfo_y': [10, 1, 3],
'vars1_x': ['massZErr/massZ'],
'vars1_y': ['massZErr'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 5 && genLep_pt2 > 5 && genLep_pt1 < 100 && genLep_pt2 < 100'],
'weight1': ['1','1'],
'xTitle': 'massZErr/massZ',
'yTitle': 'massZErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'doLogZ': False
}


saveName = 'DY15_MC_relpTErr_GENpT_eta_0_0p5_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt1 < 100 && abs(genLep_eta1) < 0.5', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 7 && genLep_pt2 < 100 && abs(genLep_eta2) < 0.5'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErr_GENpT_eta_0p7_1_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt1 < 100 && abs(genLep_eta1) < 1 && abs(genLep_eta1) > 0.7', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 7 && genLep_pt2 < 100 && abs(genLep_eta2) < 1 && abs(genLep_eta2) > 0.7'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_relpTErr_GENpT_eta_1_1p5_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt1 < 100 && abs(genLep_eta1) < 1.5 && abs(genLep_eta1) > 1', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 7 && genLep_pt2 < 100 && abs(genLep_eta2) < 1.5 && abs(genLep_eta2) > 1'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_relpTErr_GENpT_eta_1p5_2_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt1 < 100 && abs(genLep_eta1) < 2 && abs(genLep_eta1) > 1.5', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 7 && genLep_pt2 < 100 && abs(genLep_eta2) < 2 && abs(genLep_eta2) > 1.5'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY15_MC_relpTErr_GENpT_eta_2_2p5_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt1 < 100 && abs(genLep_eta1) < 2.5 && abs(genLep_eta1) > 2', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 7 && genLep_pt2 < 100 && abs(genLep_eta2) < 2.5 && abs(genLep_eta2) > 2'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_relpTErr_GENpT_eta_2_2p3_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt1 < 100 && abs(genLep_eta1) < 2.3 && abs(genLep_eta1) > 2 && lep1_ecalDriven', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 7 && genLep_pt2 < 100 && abs(genLep_eta2) < 2.3 && abs(genLep_eta2) > 2 && lep2_ecalDriven'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_relpTErr_GENpT_eta_2p3_2p5_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt1 < 100 && abs(genLep_eta1) < 2.5 && abs(genLep_eta1) > 2.3 && lep1_ecalDriven', \
          skimmedDY_cutOnGEN + 'genLep_pt2 > 7 && genLep_pt2 < 100 && abs(genLep_eta2) < 2.5 && abs(genLep_eta2) > 2.3 && lep2_ecalDriven'],
'weight1': ['1','1'],
'xTitle': 'p_{T}^{GEN}(GeV)',
'yTitle': 'pTErr/pT_{GEN}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'DY15_MC_eta1_eta2_relmasszErr_0p007_0p008'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['genLep_eta1'],
'vars1_y': ['genLep_eta2'],
'cuts1': [skimmedDY_cutOnGEN + 'genLep_pt1 > 7 && genLep_pt2 > 7 && massZErr/massZ > 0.007 && massZErr/massZ < 0.008'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


mc2015_H_path = "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/"

Hsample_baseCut = 'passedFullSelection && mass4l > 105 && mass4l < 140 '

saveName = 'H15_MC_eta1_eta2_mass4lErr_0p6_0p9_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.4],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['etaL1'],
'vars1_y': ['etaL2'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 0.6 && mass4lErr < 0.9 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_eta3_eta4_mass4lErr_0p6_0p9_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.4],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['etaL3'],
'vars1_y': ['etaL4'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 0.6 && mass4lErr < 0.9 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'eta3',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT1_pT2_mass4lErr_0p6_0p9_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['pTL1'],
'vars1_y': ['pTL2'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 0.6 && mass4lErr < 0.9 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pTL1',
'yTitle': 'pTL2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT3_pT4_mass4lErr_0p6_0p9_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['pTL3'],
'vars1_y': ['pTL4'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 0.6 && mass4lErr < 0.9 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pTL3',
'yTitle': 'pTL4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT1_eta1_m4muErr_0p74_0p88'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL1'],
'vars1_y': ['abs(etaL1)'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 0.74 && mass4lErr < 0.88 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'eta1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT2_eta2_m4muErr_0p74_0p88'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL2'],
'vars1_y': ['abs(etaL2)'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 0.74 && mass4lErr < 0.88 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT3_eta3_m4muErr_0p74_0p88'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL3'],
'vars1_y': ['abs(etaL3)'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 0.74 && mass4lErr < 0.88 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pT3',
'yTitle': 'eta3',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT4_eta4_m4muErr_0p74_0p88'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL4'],
'vars1_y': ['abs(etaL4)'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 0.74 && mass4lErr < 0.88 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT1_eta1_m4muErr_1p16_1p3'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL1'],
'vars1_y': ['abs(etaL1)'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 1.16 && mass4lErr < 1.3 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'eta1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT2_eta2_m4muErr_1p16_1p3'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL2'],
'vars1_y': ['abs(etaL2)'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 1.16 && mass4lErr < 1.3 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT3_eta3_m4muErr_1p16_1p3'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL3'],
'vars1_y': ['abs(etaL3)'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 1.16 && mass4lErr < 1.3 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pT3',
'yTitle': 'eta3',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT4_eta4_m4muErr_1p16_1p3'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL4'],
'vars1_y': ['abs(etaL4)'],
'cuts1': [Hsample_baseCut + ' && mass4lErr > 1.16 && mass4lErr < 1.3 && finalState == 1'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'massZ_genmz_CutmassZ_not_80_100'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 60, 120],
'binInfo_y': [100, 60, 120],
'vars1_x': ['genzm'],
'vars1_y': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + '  genzm > 80 && genzm < 100 && (massZ <= 80 || massZ >= 100)'],
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': 'massZ_{reco}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_relM4lErr_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.01],
'binInfo_y': [100, 0, 0.01],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'H15_MC_pT1_eta1_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL1'],
'vars1_y': ['abs(etaL1)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'eta1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT2_eta2_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL2'],
'vars1_y': ['abs(etaL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT3_eta3_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL3'],
'vars1_y': ['abs(etaL3)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT3',
'yTitle': 'eta3',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT4_eta4_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL4'],
'vars1_y': ['abs(etaL4)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'H15_MC_pT1_pTErr1_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 1],
'vars1_x': ['pTL1'],
'vars1_y': ['pTErrL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pTErr1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT1_relpTErr1_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTL1'],
'vars1_y': ['pTErrL1/pTL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pTErr1/pT1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT2_pTErr2_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 1],
'vars1_x': ['pTL2'],
'vars1_y': ['pTErrL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT2_relpTErr2_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTL2'],
'vars1_y': ['pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'pTErr2/pT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT3_pTErr3_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 1],
'vars1_x': ['pTL3'],
'vars1_y': ['pTErrL3'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT3',
'yTitle': 'pTErr3',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT3_relpTErr3_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTL3'],
'vars1_y': ['pTErrL3/pTL3'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT3',
'yTitle': 'pTErr3/pT3',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT4_pTErr4_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 1],
'vars1_x': ['pTL4'],
'vars1_y': ['pTErrL4'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'pTErr4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT4_relpTErr4_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTL4'],
'vars1_y': ['pTErrL4/pTL4'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'pTErr4/pT4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_m4l_m4lREFIT_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 105, 140],
'binInfo_y': [100, 105, 140],
'vars1_x': ['mass4l'],
'vars1_y': ['mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': 'mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_m4lErr_m4lErrREFIT_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 5],
'binInfo_y': [100, 0, 5],
'vars1_x': ['mass4lErr'],
'vars1_y': ['mass4lErrREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'mass4lErr',
'yTitle': 'mass4lErrREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_m4lErr_m4lErrREFIT_relM4lErrREFIT_biggerThan0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 5],
'binInfo_y': [100, 0, 5],
'vars1_x': ['mass4lErr'],
'vars1_y': ['mass4lErrREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT > 0.005'],
'weight1': ['1'],
'xTitle': 'mass4lErr',
'yTitle': 'mass4lErrREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_biggerThan0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.01],
'binInfo_y': [100, 0, 0.01],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT > 0.005'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mas4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_biggerThan0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.01],
'binInfo_y': [100, 0, 0.01],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT > 0.005'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.01],
'binInfo_y': [100, 0, 0.01],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
#'rootfile1': 'test.root',
'rootfile1': 'newPara.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_minosAsym_sqrtSum'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'test_tripleGauss_asyErrMinos_sqrtSum.root',
#'rootfile1': 'ggH_2015MC_mH125_39.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 '],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_test_3gauss'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'newPara_tripleGauss.root',
#'rootfile1': 'ggH_2015MC_mH125_39.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 '],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_m4lErr_m4lErrREFIT_fullRange_test'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'test_tripleGauss_symErrHESSE.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr',
'yTitle': 'mass4lErrREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_removeCorr'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation)/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_pT4_pT4subtract2timespT4Err_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 0, 10],
'binInfo_y': [50, 0, 10],
'vars1_x': ['pTL4'],
'vars1_y': ['pTL4-2*pTErrL4'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'pT4-2*pTErr4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_pT4_pT4subtract2timespT4Err_relM4lErrREFIT_biggerThan0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [50, 0, 10],
'binInfo_y': [50, 0, 10],
'vars1_x': ['pTL4'],
'vars1_y': ['pTL4-2*pTErrL4'],
'cuts1': [Hsample_baseCut + ' && finalState == 1  && mass4lErrREFIT/mass4lREFIT > 0.005'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'pT4-2*pTErr4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'H15_MC_pT1_eta1_lowBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.9],
'vars1_x': ['pTL1'],
'vars1_y': ['abs(etaL1)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<17/25 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'eta1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT2_eta2_lowBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.9],
'vars1_x': ['pTL2'],
'vars1_y': ['abs(etaL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<17/25 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT3_eta3_lowBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.9],
'vars1_x': ['pTL3'],
'vars1_y': ['abs(etaL3)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<17/25 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT3',
'yTitle': 'eta3',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT4_eta4_lowBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.9],
'vars1_x': ['pTL4'],
'vars1_y': ['abs(etaL4)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<17/25 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT3_eta3_middleBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.9],
'vars1_x': ['pTL3'],
'vars1_y': ['abs(etaL3)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) >17/25 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) < 25/20&& abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT3',
'yTitle': 'eta3',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT4_eta4_middleBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.9],
'vars1_x': ['pTL4'],
'vars1_y': ['abs(etaL4)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)>17/25 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) < 25/20 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT1_eta1_middleBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.9],
'vars1_x': ['pTL1'],
'vars1_y': ['abs(etaL1)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)>17/25 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) < 25/20 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'eta1',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_MC_pT2_eta2_middleBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.9],
'vars1_x': ['pTL2'],
'vars1_y': ['abs(etaL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)>17/25 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) < 25/20&& abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'eta2',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'H15_MC_pT1_relpTErr1_middleBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.02],
'vars1_x': ['pTL1'],
'vars1_y': ['pTErrL1/pTL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)>17/25 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) < 25/20 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pTErr1/pT1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT2_relpTErr2_middleBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.02],
'vars1_x': ['pTL2'],
'vars1_y': ['pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)>17/25 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) < 25/20 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'pTErr2/pT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_MC_pT3_relpTErr3_middleBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.02],
'vars1_x': ['pTL3'],
'vars1_y': ['pTErrL3/pTL3'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)>17/25 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) < 25/20 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT3',
'yTitle': 'pTErr3/pT3',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_MC_pT4_relpTErr4_middleBlock_alleta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.02],
'vars1_x': ['pTL4'],
'vars1_y': ['pTErrL4/pTL4'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)>17/25 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l) < 25/20 && abs(etaL1) < 0.9 && abs(etaL2) < 0.9 && abs(etaL3) < 0.9 && abs(etaL4) < 0.9'],
'weight1': ['1'],
'xTitle': 'pT4',
'yTitle': 'pTErr4/pT4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_pT1_pT2_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5, 100],
'binInfo_y': [100, 5, 100],
'vars1_x': ['pTL1'],
'vars1_y': ['pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_eta1_eta2_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.4],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'diffrelM4lErr_correlation'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -0.01,0.01],
'binInfo_y': [100, -0.5,0.5],
'vars1_x': ['mass4lErrREFIT/mass4lREFIT-mass4lErr/mass4l'],
'vars1_y': ['correlation'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErrREFIT/mass4lREFIT-mass4lErr/mass4l',
'yTitle': 'correlation contribution in mass4lErrREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'mz1_m4lREFIT_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 60,120],
'binInfo_y': [100, 105,140],
'vars1_x': ['massZ1'],
'vars1_y': ['mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'massZ1',
'yTitle': 'mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'pTErr1_pTErr2_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,3],
'binInfo_y': [100, 0,3],
'vars1_x': ['pTErrL1'],
'vars1_y': ['pTErrL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'pTErrREFIT1_pTErrREFIT2_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,3],
'binInfo_y': [100, 0,3],
'vars1_x': ['pTErrREFITL1'],
'vars1_y': ['pTErrREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'pTErrREFIT1',
'yTitle': 'pTErrREFIT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'pTErr1_pTErr2_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,3],
'binInfo_y': [100, 0,3],
'vars1_x': ['pTErrL1'],
'vars1_y': ['pTErrL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 < 0'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'pTErrREFIT1_pTErrREFIT2_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,3],
'binInfo_y': [100, 0,3],
'vars1_x': ['pTErrREFITL1'],
'vars1_y': ['pTErrREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 < 0'],
'weight1': ['1'],
'xTitle': 'pTErrREFIT1',
'yTitle': 'pTErrREFIT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'pTErr1_pTErrREFIT1_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,3],
'binInfo_y': [100, 0,3],
'vars1_x': ['pTErrL1'],
'vars1_y': ['pTErrREFITL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErrREFIT1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'pTErr2_pTErrREFIT2_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,3],
'binInfo_y': [100, 0,3],
'vars1_x': ['pTErrL2'],
'vars1_y': ['pTErrREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'pTErr2',
'yTitle': 'pTErrREFIT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'pTErr1_pTErrREFIT1_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,3],
'binInfo_y': [100, 0,3],
'vars1_x': ['pTErrL1'],
'vars1_y': ['pTErrREFITL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 < 0'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErrREFIT1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'pTErr2_pTErrREFIT2_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,3],
'binInfo_y': [100, 0,3],
'vars1_x': ['pTErrL2'],
'vars1_y': ['pTErrREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 < 0'],
'weight1': ['1'],
'xTitle': 'pTErr2',
'yTitle': 'pTErrREFIT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'GENmassZ1_massZ1'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
#'rootfile1': 'test.root',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo_x': [100, 40, 120],
'binInfo_y': [100, 40, 120],
'vars1_x': ['GENmassZ1'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'massZ1_{gen}',
'yTitle': 'massZ1_{reco}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'massZ1_massZ1REFIT_test'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'test_tripleGauss_symErrHESSE.root',
#'rootfile1': 'newPara_tripleGauss.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 80, 110],
'binInfo_y': [100, 80, 110],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'massZ1_{reco}',
'yTitle': 'massZ1_{refit}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'massZ1_massZ1REFIT_test_3gauss_full'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
#'rootfile1': 'newPara.root',
'rootfile1': 'newPara_tripleGauss.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 40, 110],
'binInfo_y': [100, 40, 110],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'massZ1_{reco}',
'yTitle': 'massZ1_{refit}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'massZ1_massZ1REFIT_pdfKinZFitter'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
#'rootfile1': 'test.root',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 40, 110],
'binInfo_y': [100, 40, 110],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'massZ1_{reco}',
'yTitle': 'massZ1_{refit}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'massZ1_massZ1REFIT_pdfKinZFitter_ichepNtuple'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/',
#'rootfile1': 'test.root',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISpring16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo_x': [100, 88, 94],
'binInfo_y': [100, 88, 94],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'massZ1_{reco}',
'yTitle': 'massZ1_{refit}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'massZ1_massZ1REFIT_bw'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
#'rootfile1': 'test.root',
'rootfile1': 'useBW.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 40, 110],
'binInfo_y': [100, 40, 110],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'massZ1_{reco}',
'yTitle': 'massZ1_{refit}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'massZ1_massZ1REFIT_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 80, 100],
'binInfo_y': [100, 80, 100],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'massZ1_{reco}',
'yTitle': 'massZ1_{refit}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'massZ1_massZ1REFIT_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 80, 100],
'binInfo_y': [100, 80, 100],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/17'],
'weight1': ['1'],
'xTitle': 'massZ1_{reco}',
'yTitle': 'massZ1_{refit}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'massZ1_massZ1REFIT_upRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 80, 100],
'binInfo_y': [100, 80, 100],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1  && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)>25/17'],
'weight1': ['1'],
'xTitle': 'massZ1_{reco}',
'yTitle': 'massZ1_{refit}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_norefittedMZ191p2'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (massZ1REFIT > 91.24 || massZ1REFIT < 91.14)'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_norecoMZ191p2'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (massZ1 > 91.24 || massZ1 < 91.14)'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'pT1_pT2_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5,100],
'binInfo_y': [100, 5,100],
'vars1_x': ['pTL1'],
'vars1_y': ['pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'pT1_pT2_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5,100],
'binInfo_y': [100, 5,100],
'vars1_x': ['pTL1'],
'vars1_y': ['pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/17'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'eta1_eta2_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4,2.4],
'binInfo_y': [100, -2.4,2.4],
'vars1_x': ['etaL1'],
'vars1_y': ['etaL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'pT1REFIT_pT2REFIT_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5,100],
'binInfo_y': [100, 5,100],
'vars1_x': ['pTREFITL1'],
'vars1_y': ['pTREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'pT1REFIT_pT2REFIT_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5,100],
'binInfo_y': [100, 5,100],
'vars1_x': ['pTREFITL1'],
'vars1_y': ['pTREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/17'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'pT1_pT1REFIT_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5,100],
'binInfo_y': [100, 5,100],
'vars1_x': ['pTL1'],
'vars1_y': ['pTREFITL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pT1REFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'pT1_pT1REFIT_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5,100],
'binInfo_y': [100, 5,100],
'vars1_x': ['pTL1'],
'vars1_y': ['pTREFITL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/17'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pTREFIT1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'pT2_pT2REFIT_lowRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5,100],
'binInfo_y': [100, 5,100],
'vars1_x': ['pTL2'],
'vars1_y': ['pTREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 > 0'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'pT2REFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'pT2_pT2REFIT_middleRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 5,100],
'binInfo_y': [100, 5,100],
'vars1_x': ['pTL2'],
'vars1_y': ['pTREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.4 - (sqrt(mass4lErrREFIT*mass4lErrREFIT-correlation))/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/17'],
'weight1': ['1'],
'xTitle': 'pT2',
'yTitle': 'pTREFIT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_onlyrefittedMZ191p2'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.025],
'binInfo_y': [100, 0, 0.025],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && (massZ1REFIT < 91.24 && massZ1REFIT > 91.14)'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_diffM4lErr_MZ1_test'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'test_tripleGauss_symErrHESSE.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_MZ1_bw'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'useBW.root',
#'rootfile1': 'ggH_2015MC_mH125_39.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_MZ1_newPara_3gauss'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'test_tripleGauss_asyErrMinos_addGENpT.root',
#'rootfile1': 'ggH_2015MC_mH125_39.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_MZ1_newPara_3gauss_minos_sqrtSum'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootfile1': 'test_tripleGauss_asyErrMinos_sqrtSum.root',
#'rootfile1': 'ggH_2015MC_mH125_39.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_diffM4lErr_MZ1_newPara_test'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'H15_errUpDnDiff_mZ1_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'testDiffAsmErr.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -0.03, 0.03],
'binInfo_y': [100, 50, 100],
'vars1_x': ['pTErrREFITL1/pTREFITL1', 'pTErrREFITL2/pTREFITL2'],
'vars1_y': ['massZ1', 'massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1', Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'xTitle': '(pTErr_Hi + pTErr_Lo)/pTErr',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'H15_genPt_refitpT_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'testDiffAsmErr.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['pTGENL1', 'pTGENL2'],
'vars1_y': ['pTREFITL1', 'pTREFITL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1', Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'xTitle': 'pT_{GEN}',
'yTitle': 'pT_{REFIT}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_genPt_recopT_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'testDiffAsmErr.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['pTGENL1', 'pTGENL2'],
'vars1_y': ['pTL1', 'pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1', Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'xTitle': 'pT_{GEN}',
'yTitle': 'pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_recoPt_refitpT_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'testDiffAsmErr.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['pTREFITL1', 'pTREFITL2'],
'vars1_y': ['pTL1', 'pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1', Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'xTitle': 'pT_{REFIT}',
'yTitle': 'pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_GENZ_mass_0_1'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'ggH_2015MC_mH125.root',
#'rootfile1': 'mH_125.root',
'tree1': 'Ana/passedEvents',
'binInfo_x': [100, 4, 110],
'binInfo_y': [100, 4, 110],
'vars1_x': ['GENZ_mass[0]'],
'vars1_y': ['GENZ_mass[1]'],
'cuts1': [Hsample_baseCut],
'weight1': ['1'],
'xTitle': 'GENZ_mass[0]',
'yTitle': 'GENZ_mass[1]',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}



saveName = 'DY_2015_relpTErr_eta_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100'], #
'weight1': ['1', '1'],
'xTitle': 'eta',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_pT_eta_0_0p8_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8 && lep1_ecalDriven', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8 && lep2_ecalDriven'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_0_1_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverSqrtpT_eta_0_1_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.4],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['1/sqrt(genLep_pt1)', '1/sqrt(genLep_pt2)'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1'], #
'weight1': ['1', '1'],
'xTitle': '1/sqrt(pT)',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverpT_eta_0_1_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.2],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['1/genLep_pt1', '1/genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1'], #
'weight1': ['1', '1'],
'xTitle': '1/pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverSqrtpT_eta_1_1.47_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.4],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['1/sqrt(genLep_pt1)', '1/sqrt(genLep_pt2)'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1.47 && abs(genLep_eta1) > 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1.47 && abs(genLep_eta2) > 1'], #
'weight1': ['1', '1'],
'xTitle': '1/sqrt(pT)',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverpT_eta_1_1.47_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.2],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['1/genLep_pt1', '1/genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1.47 && abs(genLep_eta1) > 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1.47 && abs(genLep_eta2) > 1'], #
'weight1': ['1', '1'],
'xTitle': '1/pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverSqrtpT_eta_1.5_2_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.4],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['1/sqrt(genLep_pt1)', '1/sqrt(genLep_pt2)'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2 && abs(genLep_eta1) > 1.5', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2 && abs(genLep_eta2) > 1.5'], #
'weight1': ['1', '1'],
'xTitle': '1/sqrt(pT)',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverpT_eta_1.5_2_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.2],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['1/genLep_pt1', '1/genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2 && abs(genLep_eta1) > 1.5', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2 && abs(genLep_eta2) > 1.5'], #
'weight1': ['1', '1'],
'xTitle': '1/pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverSqrtpT_eta_2_2.5_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.4],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['1/sqrt(genLep_pt1)', '1/sqrt(genLep_pt2)'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2.5', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2.5'], #
'weight1': ['1', '1'],
'xTitle': '1/sqrt(pT)',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverpT_eta_2_2.5_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.2],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['1/genLep_pt1', '1/genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2.5', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2.5'], #
'weight1': ['1', '1'],
'xTitle': '1/pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_1_2_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2 && abs(genLep_eta1) > 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2 && abs(genLep_eta2) > 1'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': True,
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_0p8_1p44_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1.44 && abs(genLep_eta1) > 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1.44 && abs(genLep_eta2) > 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_0p8_1p44_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1.44 && abs(genLep_eta1) > 0.8 && lep1_ecalDriven', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1.44 && abs(genLep_eta2) > 0.8 && lep2_ecalDriven'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_1p1_1p44_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1.44 && abs(genLep_eta1) > 1.1 && lep1_ecalDriven == 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1.44 && abs(genLep_eta2) > 1.1 && lep2_ecalDriven == 1'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_0p8_1_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1 && abs(genLep_eta1) > 0.8 && lep1_ecalDriven == 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1 && abs(genLep_eta2) > 0.8 && lep2_ecalDriven == 1'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_pT_eta_1p44_1p57_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1.57 && abs(genLep_eta1) > 1.44 && lep1_ecalDriven == 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1.57 && abs(genLep_eta2) > 1.44 && lep2_ecalDriven == 1'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_pT_eta_1p57_2_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2 && abs(genLep_eta1) > 1.57 && lep1_ecalDriven == 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2 && abs(genLep_eta2) > 1.57 && lep2_ecalDriven == 1'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_1OverSqrtpT_eta_1p57_2_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['1/sqrt(genLep_pt1)', '1/sqrt(genLep_pt2)'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2 && abs(genLep_eta1) > 1.57 && lep1_ecalDriven == 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2 && abs(genLep_eta2) > 1.57 && lep2_ecalDriven == 1'], #
'weight1': ['1', '1'],
'xTitle': '1/Sqrt(pT)',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}
saveName = 'DY_2015_relpTErr_1OverSqrtpT_eta_0_0p8_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['1/sqrt(genLep_pt1)', '1/sqrt(genLep_pt2)'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8 && lep1_ecalDriven == 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8 && lep2_ecalDriven == 1'], #
'weight1': ['1', '1'],
'xTitle': '1/Sqrt(pT)',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_pT_eta_1p2_1p44_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 1.44 && abs(genLep_eta1) > 1.2 && lep1_ecalDriven == 1', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 1.44 && abs(genLep_eta2) > 1.2 && lep2_ecalDriven == 1'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_pT_eta_1p57_2p5_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2.5 && abs(genLep_eta1) > 1.57', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2.5 && abs(genLep_eta2) > 1.57'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_1p57_2p5_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2.5 && abs(genLep_eta1) > 1.57 && lep1_ecalDriven', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2.5 && abs(genLep_eta2) > 1.57 && lep2_ecalDriven'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_pT_eta_2_2p5_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2.5 && abs(genLep_eta1) > 2', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2.5 && abs(genLep_eta2) > 2'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_pT_eta_2_2p5_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 2.5 && abs(genLep_eta1) > 2 && lep1_ecalDriven', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 2.5 && abs(genLep_eta2) > 2 && lep2_ecalDriven'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}




saveName = 'DY_2015_relpTErr_sqrt1OverpT_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.4],
'binInfo_y': [100, 0, 0.04],
'vars1_x': ['sqrt(1/genLep_pt1)', 'sqrt(1/genLep_pt2)'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && lep1_ecalDriven == 1 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && lep2_ecalDriven == 1 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': '1/sqrt(pT)',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_pTErr2_pT_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1*pterr1', 'pterr2*pterr2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && lep1_ecalDriven == 1 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && lep2_ecalDriven == 1 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr^{2}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr2_1OverpT_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.15],
'binInfo_y': [100, 0, 0.001],
'vars1_x': ['1/genLep_pt1', '1/genLep_pt2'],
'vars1_y': ['pterr1*pterr1/genLep_pt1/genLep_pt1', 'pterr2*pterr2/genLep_pt2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && lep1_ecalDriven == 1 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && lep2_ecalDriven == 1 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': '1/pT',
'yTitle': '(ptErr/pt)^{2}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_1OverpT_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.15],
'binInfo_y': [100, 0, 0.04],
'vars1_x': ['1/genLep_pt1', '1/genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && lep1_ecalDriven == 1 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && lep2_ecalDriven == 1 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': '1/sqrt(pT)',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_pT_eta_0_0p8_pT_0_50_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 50],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_pT_eta_0_0p8_pT_50_100_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 50, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_pTErr_pT_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 10],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_sqrtpTErr_pT_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 10],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['sqrt(pterr1)', 'sqrt(pterr2)'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'sqrt(ptErr)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_pTErr_sqrtpT_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 10],
'binInfo_y': [100, 0, 10],
'vars1_x': ['sqrt(genLep_pt1)', 'sqrt(genLep_pt2)'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'sqrt(pT)',
'yTitle': 'ptErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'DY_2015_pTErrOverSqrtPt_pT_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 1],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pterr1/sqrt(genLep_pt1)', 'pterr2/sqrt(genLep_pt2)'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pT',
'yTitle': 'ptErr/sqrt(pT)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_pTErr_phi_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -3, 3],
'binInfo_y': [100, 0, 10],
'vars1_x': ['genLep_phi1', 'genLep_phi2'],
'vars1_y': ['pterr1', 'pterr2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'phi',
'yTitle': 'ptErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_relPtErr2_paraPt_eta_0_0p8_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['(0.3*0.3/100/100)*genLep_pt1*genLep_pt1+(2.8*2.8/100/100)*genLep_pt1+0.128*0.128', \
            '(0.3*0.3/100/100)*genLep_pt2*genLep_pt2+(2.8*2.8/100/100)*genLep_pt2+0.128*0.128'],
'vars1_y': ['pterr1*pterr1', 'pterr2*pterr2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta1) < 0.8', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && abs(genLep_eta2) < 0.8'], #
'weight1': ['1', '1'],
'xTitle': 'pTPara',
'yTitle': 'ptErr*ptErr',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_genPt1_genPt2_relMZErr_0.012_0.014_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['genLep_pt1'],
'vars1_y': ['genLep_pt2'],
'cuts1': ['massZ > 60 && massZ < 120 && massZErr/massZ > 0.012 && massZErr/massZ < 0.014'], #
'weight1': ['1', '1'],
'xTitle': 'genLep_pt1',
'yTitle': 'genLep_pt2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_genEta1_genEta2_relMZErr_0.012_0.014_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['abs(genLep_eta1)'],
'vars1_y': ['abs(genLep_eta2)'],
'cuts1': ['massZ > 60 && massZ < 120 && massZErr/massZ > 0.012 && massZErr/massZ < 0.014'], #
'weight1': ['1', '1'],
'xTitle': 'genLep_eta1',
'yTitle': 'genLep_eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_genPt1_genPt2_relMZErr_bigger_0.02_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['genLep_pt1'],
'vars1_y': ['genLep_pt2'],
'cuts1': ['massZ > 60 && massZ < 120 && massZErr/massZ > 0.02'], #
'weight1': ['1', '1'],
'xTitle': 'genLep_pt1',
'yTitle': 'genLep_pt2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}


saveName = 'DY_2015_genEta1_genEta2_relMZErr_bigger_0.458_0.05_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(genLep_eta1)'],
'vars1_y': ['abs(genLep_eta2)'],
'cuts1': ['massZ > 60 && massZ < 120 && massZErr/massZ < 0.05 && massZErr/massZ > 0.0458'], #
'weight1': ['1', '1'],
'xTitle': 'genLep_eta1',
'yTitle': 'genLep_eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}



saveName = 'DY_2015_genEta1_genEta2_relMZErr_bigger_0.05_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(genLep_eta1)'],
'vars1_y': ['abs(genLep_eta2)'],
'cuts1': ['massZ > 60 && massZ < 120 && massZErr/massZ > 0.05'], #
'weight1': ['1', '1'],
'xTitle': 'genLep_eta1',
'yTitle': 'genLep_eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}

saveName = 'H_2015_eta1_eta2_relM4lErr_bigger_0.03_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['mass4l > 105 && mass4l < 140 && passedFullSelection && mass4lErr/mass4l > 0.03 && finalState == 3'], #
'weight1': ['1', '1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' '
}



saveName = 'H_2015_eta1_eta2_relM4lErr_bigger_0.03_smaller_0.05_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['mass4l > 105 && mass4l < 140 && passedFullSelection && mass4lErr/mass4l > 0.03 && mass4lErr/mass4l < 0.05 && finalState == 2'], #
'weight1': ['1', '1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'doLogZ':True
}

saveName = 'H_2015_eta1_eta2_relM4lErr_bigger_0.03_smaller_0.05_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['mass4l > 105 && mass4l < 140 && passedFullSelection && mass4lErr/mass4l > 0.03 && mass4lErr/mass4l < 0.05 && finalState == 3'], #
'weight1': ['1', '1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'doLogZ':True
}

saveName = 'H_2015_eta1_eta2_relM4lErr_bigger_0.05_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['mass4l > 105 && mass4l < 140 && passedFullSelection && mass4lErr/mass4l > 0.05 && finalState == 3'], #
'weight1': ['1', '1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
}



saveName = 'H15_relm4lErr_relm4lErrREFIT_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140  && finalState > 2'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mas4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140  && finalState == 2'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mas4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relm4lErr_relm4lErrREFIT_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140  && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr/mas4l',
'yTitle': 'mass4lErrREFIT/mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta1_eta2_tailM4l_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['passedFullSelection && mass4l > 128 && mass4l < 130  && finalState == 3'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta1_eta2_tailM4lREFIT_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 128 && mass4lREFIT < 130  && finalState == 3'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta1_eta2_bigM4lErr_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['passedFullSelection && mass4l > 125 && mass4lErr > 2.5  && finalState == 3'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_eta1_eta2_bigM4lErrREFIT_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 125 && mass4lErrREFIT > 2.5  && finalState == 3'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_eta3_eta4_bigM4lErrREFIT_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL3)'],
'vars1_y': ['abs(etaL4)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 125 && mass4lErrREFIT > 2.5  && finalState == 3'],
'weight1': ['1'],
'xTitle': 'eta3',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta1_eta2_bigM4lErrREFIT_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 125 && mass4lErrREFIT > 2.5  && mass4lErrREFIT < 5 && finalState == 4'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta3_eta4_bigM4lErrREFIT_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL3)'],
'vars1_y': ['abs(etaL4)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 125 && mass4lErrREFIT > 2.5  && mass4lErrREFIT< 5 && finalState == 4'],
'weight1': ['1'],
'xTitle': 'eta3',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta1_eta2_smallM4lErrREFIT_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 125 && mass4lErrREFIT < 2 && finalState == 4'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta3_eta4_smallM4lErrREFIT_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL3)'],
'vars1_y': ['abs(etaL4)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 125 && mass4lErrREFIT < 2 && finalState == 4'],
'weight1': ['1'],
'xTitle': 'eta3',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta3_eta4_bigM4lErrREFIT_125_127_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL3)'],
'vars1_y': ['abs(etaL4)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 125 && mass4lREFIT < 127 && mass4lErrREFIT > 3 && finalState == 4'],
'weight1': ['1'],
'xTitle': 'eta3',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, 
'latexNote1': '' #
}


saveName = 'H15_eta1_eta2_bigM4lErrREFIT_125_127_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
'tree1': 'passedEvents',
'binInfo_x': [25, 0, 2.5],
'binInfo_y': [25, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': ['passedFullSelection && mass4lREFIT > 125 && mass4lREFIT < 127 && mass4lErrREFIT > 3 && finalState == 4'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, 
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_MZ1_test_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'debug.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_MZ1_test_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'debug.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 4'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_m4lREFIT_test_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_refitOnlyBelow_m4lErrREFIT_0p02.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -0.5, 0.5],
'binInfo_y': [100, 105, 140],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_m4lREFIT_test_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_refitOnlyBelow_m4lErrREFIT_0p02.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -0.5, 0.5],
'binInfo_y': [100, 105, 140],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 4'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'mass4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_MZ1_test_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -0.5, 0.5],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 2'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4lErr_MZ1_test_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -0.5, 0.5],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_diffM4l_MZ1_test_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -0.5, 0.5],
'binInfo_y': [100, 50, 100],
'vars1_x': ['abs(mass4l-GENmass4l)-abs(mass4lREFIT-GENmass4l)'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1'],
'xTitle': 'abs(mass4l-GENmass4l)-abs(mass4lREFIT-GENmass4l)',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4l_MZ1_test_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -0.5, 0.5],
'binInfo_y': [100, 50, 100],
'vars1_x': ['abs(mass4l-GENmass4l)-abs(mass4lREFIT-GENmass4l)'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 4'],
'weight1': ['1'],
'xTitle': 'abs(mass4l-GENmass4l)-abs(mass4lREFIT-GENmass4l)',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_diffM4l_MZ1_test_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -5, 5],
'binInfo_y': [100, 50, 100],
'vars1_x': ['abs(mass4l-GENmass4l)-abs(mass4lREFIT-GENmass4l)'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'abs(mass4l-GENmass4l)-abs(mass4lREFIT-GENmass4l)',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffM4l_MZ1_test_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 50, 100],
'vars1_x': ['abs(mass4l-GENmass4l)-abs(mass4lREFIT-GENmass4l)'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 2'],
'weight1': ['1'],
'xTitle': 'abs(mass4l-GENmass4l)-abs(mass4lREFIT-GENmass4l)',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_m4lErr_m4lErrREFIT_relM4lErrREFITBigger0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 5],
'binInfo_y': [100, 0, 5],
'vars1_x': ['mass4lErr'],
'vars1_y': ['mass4lErrREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState > 2 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'mass4lErr',
'yTitle': 'mass4lErrREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_diffm4lErr_relM4lErrREFITBigger0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -5, 5],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState > 2 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_diffm4lErr_relM4lErrREFITSmall0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -5, 5],
'binInfo_y': [100, 50, 100],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState > 2 && mass4lErrREFIT/mass4lREFIT < 0.02'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_pT1_pT2_relM4lErrREFITSmall0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['pTL1'],
'vars1_y': ['pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT < 0.02'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pT2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_pT1_pT2_relM4lErrREFITBig0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 100],
'vars1_x': ['pTL1'],
'vars1_y': ['pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'pT1',
'yTitle': 'pT2',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_eta1_eta2_relM4lErrREFITSmall0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['abs(etaL1)'],
'vars1_y': ['abs(etaL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT < 0.02'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_eta1_eta2_relM4lErrREFITBig0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['etaL1'],
'vars1_y': ['etaL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_pTErr1_pTErr2_relM4lErrREFITSmall0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 3],
'binInfo_y': [100, 0, 3],
'vars1_x': ['pTErrL1'],
'vars1_y': ['pTErrL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT < 0.02'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_pTErr1_pTErr2_relM4lErrREFITBig0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 3],
'binInfo_y': [100, 0, 3],
'vars1_x': ['pTErrL1'],
'vars1_y': ['pTErrL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_pTErr1_pTErr2_relM4lErrREFITSmall0p02_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 3],
'binInfo_y': [100, 0, 3],
'vars1_x': ['pTErrL1'],
'vars1_y': ['pTErrL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 4 && mass4lErrREFIT/mass4lREFIT < 0.02'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_pTErr1_pTErr2_relM4lErrREFITBig0p02_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 3],
'binInfo_y': [100, 0, 3],
'vars1_x': ['pTErrL1'],
'vars1_y': ['pTErrL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 4 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_relpTErr1_relpTErr2_relM4lErrREFITSmall0p02_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTErrL1/pTL1'],
'vars1_y': ['pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 4 && mass4lErrREFIT/mass4lREFIT < 0.02'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_relpTErr1_relpTErr2_relM4lErrREFITBig0p02_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTErrL1/pTL1'],
'vars1_y': ['pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 4 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_relpTErr1_relpTErr2_relM4lErrREFITSmall0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTErrL1/pTL1'],
'vars1_y': ['pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT < 0.02'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}
saveName = 'H15_relpTErr1_relpTErr2_relM4lErrREFITBig0p02_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTErrL1/pTL1'],
'vars1_y': ['pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'pTErr1',
'yTitle': 'pTErr2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_mass4lREFIT_mass4lErrREFIT_2e2mu_big0p02'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 105, 140],
'binInfo_y': [100, 2, 5],
'vars1_x': ['mass4lREFIT'],
'vars1_y': ['mass4lErrREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 3 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'm4lREFIT',
'yTitle': 'm4lErrREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_mass4lREFIT_mass4lErrREFIT_2mu2e_big0p02'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 105, 140],
'binInfo_y': [100, 2, 5],
'vars1_x': ['mass4lREFIT'],
'vars1_y': ['mass4lErrREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 4 && mass4lErrREFIT/mass4lREFIT > 0.02'],
'weight1': ['1'],
'xTitle': 'm4lREFIT',
'yTitle': 'm4lErrREFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_mz1_mz1refit_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 50, 100],
'binInfo_y': [100, 50, 100],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': 'mz1',
'yTitle': 'mz1REFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_mz1_mz1refit_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 50, 100],
'binInfo_y': [100, 50, 100],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 2'],
'weight1': ['1'],
'xTitle': 'mz1',
'yTitle': 'mz1REFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_mz1_mz1refit_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 50, 100],
'binInfo_y': [100, 50, 100],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1'],
'xTitle': 'mz1',
'yTitle': 'mz1REFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_mz1_mz1refit_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test_fixFitRangeWhenDeriveEBE_moreEtaBins.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 50, 100],
'binInfo_y': [100, 50, 100],
'vars1_x': ['massZ1'],
'vars1_y': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 4'],
'weight1': ['1'],
'xTitle': 'mz1',
'yTitle': 'mz1REFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relmz1Err_diffM4lErr_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'debug.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1Err/massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 4'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1Err/massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relmz1Err_diffM4lErr_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1Err/massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1Err/massZ1',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_maxrelLepErr_diffM4lErr_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['max(pTErrL1/pTL1, pTErrL2/pTL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'max(pTErrL1/pTL1, pTErrL2/pTL2)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_maxrelLepErr_diffM4lErr_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'debug.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['max(pTErrL1/pTL1, pTErrL2/pTL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 4'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'max(pTErrL1/pTL1, pTErrL2/pTL2)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_maxLepErr_diffM4lErr_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'debug.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 0, 10],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['max(pTErrL1, pTErrL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'max(pTErrL1, pTErrL2)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_maxLepErr_diffM4lErr_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'debug.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 0, 10],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['max(pTErrL1, pTErrL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 4'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'max(pTErrL1, pTErrL2)',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_mz1Err_diffM4lErr_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'debug.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 0, 10],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1Err'],
'cuts1': [Hsample_baseCut + ' && finalState == 4'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1Err',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_mz1Err_diffM4lErr_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'debug.root',
#'rootfile1': 'ggH_2015MC_mH125_31.root',
#'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2, 2],
'binInfo_y': [100, 0, 10],
'vars1_x': ['mass4lErr-mass4lErrREFIT'],
'vars1_y': ['massZ1Err'],
'cuts1': [Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1'],
'xTitle': 'mass4lErr-mass4lErrREFIT',
'yTitle': 'massZ1Err',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relpTErr_diff_genPt_refitpT_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'test.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -50, 50],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTREFITL1-pTGENL1', 'pTREFITL2-pTGENL2'],
'vars1_y': ['pTErrL1/pTL1', 'pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3', Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1', '1'],
'xTitle': 'pT_{refit} - pT_{gen}',
'yTitle': 'pTErr/pT_{reco}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_relpTErr_diff_genPt_refitpT_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'test.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -50, 50],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTREFITL1-pTGENL1', 'pTREFITL2-pTGENL2'],
'vars1_y': ['pTErrL1/pTL1', 'pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 4', Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1', '1'],
'xTitle': 'pT_{refit} - pT_{gen}',
'yTitle': 'pTErr/pT_{reco}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'H15_relpTErr_diff_recoPt_refitpT_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'test.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -50,50],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTREFITL1-pTL1', 'pTREFITL2-pTL2'],
'vars1_y': ['pTErrL1/pTL1', 'pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 3', Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1', '1'],
'xTitle': 'pT_{refit} - pT_{reco}',
'yTitle': 'pTErr/pT_{reco}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'H15_relpTErr_diff_recoPt_refitpT_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'test.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -50,50],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pTREFITL1-pTL1', 'pTREFITL2-pTL2'],
'vars1_y': ['pTErrL1/pTL1', 'pTErrL2/pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 4', Hsample_baseCut + ' && finalState == 3'],
'weight1': ['1', '1'],
'xTitle': 'pT_{refit} - pT_{reco}',
'yTitle': 'pTErr/pT_{reco}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'DY_2015_relpTErr_eta_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.5, 2.5],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && lep1_ecalDriven ', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && lep2_ecalDriven '], #
'weight1': ['1', '1'],
'xTitle': 'eta',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'DY_2015_relpTErr_eta_ecalDriven_relMassZErrBig0p03_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.5, 2.5],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && lep1_ecalDriven && massZErr/massZ > 0.03', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && lep2_ecalDriven && massZErr/massZ > 0.03'], #
'weight1': ['1', '1'],
'xTitle': 'eta',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_eta_ecalDriven_relPtErrBig0p05_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.5, 2.5],
'binInfo_y': [100, 0, 0.2],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && lep1_ecalDriven && pterr1/genLep_pt1 > 0.05', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && lep2_ecalDriven && pterr2/genLep_pt2 > 0.05'], #
'weight1': ['1', '1'],
'xTitle': 'eta',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'DY_2015_relpTErr_eta_nonecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && !lep1_ecalDriven ', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && !lep2_ecalDriven '], #
'weight1': ['1', '1'],
'xTitle': 'eta',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'DY_2015_massZErr_massZ_ifRelMassZErrBigger_0p03_2e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 60, 120],
'binInfo_y': [100, 0, 20],
'vars1_x': ['massZ'],
'vars1_y': ['massZErr'],
'cuts1': ['genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 60 && massZ < 120 && massZErr/massZ > 0.04'],
'weight1': ['1', '1'],
'xTitle': 'massZ',
'yTitle': 'massZErr',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'DY_2015_eta1_eta2_ifRelMassZErrBigger_0p04_2e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0,2.5],
'binInfo_y': [100, 0,2.5],
'vars1_x': ['abs(eta1)'],
'vars1_y': ['abs(eta2)'],
'cuts1': ['genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 60 && massZ < 120 && massZErr/massZ > 0.04'],
'weight1': ['1', '1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'DY_relMZErr_maxRelPtErr_2e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.12],
'binInfo_y': [100, 0, 0.4],
'vars1_x': ['massZErr/massZ'],
'vars1_y': ['max(pterr1/genLep_pt1, pterr2/genLep_pt2)'],
'cuts1': ['genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 60 && massZ < 120'],
'weight1': ['1', '1'],
'xTitle': 'massZErr/massZ',
'yTitle': 'max(ptErr/pT_{gen})',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'data15_2mu_relpTErrRECO_eta'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120',\
          'massZ > 60 && massZ < 120'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'mc15_2mu_relpTErrRECO_eta'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2015MC_kalman_v4_76X/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120',\
          'massZ > 60 && massZ < 120'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'data15_2mu_relpTErrRECO_eta_lowMet'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && Met < 5',\
          'massZ > 60 && massZ < 120 && Met < 5'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'data16_2mu_relpTErrRECO_eta'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/inputRoot/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.4, 2.4],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120', 'massZ > 60 && massZ < 120'],
'weight1': ['1','1'],
'xTitle': 'eta',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'data15_2mu_relpTErrRECO_pT_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 0.9', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 0.9'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'mc15_2mu_relpTErrRECO_pT_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2015MC_kalman_v4_76X/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 0.9', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 0.9'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'data15_2mu_relpTErrRECO_pT_eta_0p9_1p8'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 1.8 && abs(eta1) > 0.9', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 1.8 && abs(eta2) > 0.9'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'mc15_2mu_relpTErrRECO_pT_eta_0p9_1p8'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2015MC_kalman_v4_76X/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 1.8 && abs(eta1) > 0.9', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 1.8 && abs(eta2) > 0.9'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'data15_2mu_relpTErrRECO_pT_eta_1p8_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 2.4 && abs(eta1) > 1.8', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 2.4 && abs(eta2) > 1.8'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'data15_2mu_relpTErrRECO_pT_eta_1p8_2p2'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 2.2 && abs(eta1) > 1.8', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 2.2 && abs(eta2) > 1.8'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'data15_2mu_relpTErrRECO_pT_eta_2p2_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 2.4 && abs(eta1) > 2.2', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 2.4 && abs(eta2) > 2.2'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'mc15_2mu_relpTErrRECO_pT_eta_1p8_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2015MC_kalman_v4_76X/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 2.4 && abs(eta1) > 1.8', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 2.4 && abs(eta2) > 1.8'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'data15_2mu_pT_eta_relM2lErr_big_0p025'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 200],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['eta1', 'eta2'],
'cuts1': ['massZ > 60 && massZ < 120 && massZErr/massZ > 0.025', \
          'massZ > 60 && massZ < 120 && massZErr/massZ > 0.025'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'data15_2e_pT_eta_relM2lErr_0p02175_0p02725'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 200],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['eta1', 'eta2'],
'cuts1': ['massZ > 60 && massZ < 120 && massZErr/massZ > 0.02175 && massZErr/massZ < 0.02725 && lep1_ecalDriven && pterr1/pT1 < 0.07', \
          'massZ > 60 && massZ < 120 && massZErr/massZ > 0.02175 && massZErr/massZ < 0.02725 && lep2_ecalDriven && pterr2/pT2 < 0.07'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'eta',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}

saveName = 'data15_2mu_relM2lErr'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['pT1', 'pT2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && abs(eta1) < 2.4 && abs(eta1) > 1.8', \
          'massZ > 60 && massZ < 120 && abs(eta2) < 2.4 && abs(eta2) > 1.8'],
'weight1': ['1','1'],
'xTitle': 'pT',
'yTitle': 'pTErr/pT_{RECO}',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '' #
}


saveName = 'data_2015_relpTErr_eta_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.5, 2.5],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pterr2/pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && lep1_ecalDriven ', \
          'massZ > 60 && massZ < 120 && lep2_ecalDriven '], #
'weight1': ['1', '1'],
'xTitle': 'eta',
'yTitle': 'ptErr/pT',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'data_2015_relpTErr_eta_NoEcalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.5, 2.5],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['eta1', 'eta2'],
'vars1_y': ['pterr1/pT1', 'pT2'],
'cuts1': ['massZ > 60 && massZ < 120 && !lep1_ecalDriven ', \
          'massZ > 60 && massZ < 120 && !lep2_ecalDriven '], #
'weight1': ['1', '1'],
'xTitle': 'eta',
'yTitle': 'ptErr/pT',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'data_2015_m2lErr_avePtSquare'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/Data_2015D/',
'rootfile1': 'DoubleLepton_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 5],
'vars1_x': ['sqrt((pT1*pT1+pT2*pT2)/2)'],
'vars1_y': ['massZErr'],
'cuts1': ['massZ > 60 && massZ < 120 ', \
          'massZ > 60 && massZ < 120 '], #
'weight1': ['1'],
'xTitle': 'sqrt((pT1^{2}+pT2^{2})/2)',
'yTitle': 'massZErr',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

