paraConfigs = { }

mc2015_dy_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/inputRootFiles/'
mc2016_dy_path = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/inputRoot/forApproval/'
mc2015_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/'
mc2016_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/makeSlimTree/'
mc2015_H_path = '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_Run1Fid_20160222/'
mc2016_H_path = '/cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/'

mc2015_dy_path_kalmanv4_hasGENm2l = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4/'

savePath = '/home/mhl/public_html/2016/20161011_2015MCebeCorrection/'

skimmedDY_cut = 'massZ > 80 && massZ < 100 && massZErr > 0.2 && massZErr < 7.2 && Met < 30 && ' 
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

saveName = 'pT_GENpT_leg2_2D_15mc_hasLeg1'
paraConfigs['mc_15_DY_pT_GENpT_leg2_hasLeg1'] = \
{\
'rootPath1': mc2015_dy_path_kalmanv4_hasGENm2l,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [90, 10, 100],
'binInfo_y': [90, 10, 100],
'vars1_x': ['genLep_pt1', 'genLep_pt2'],
'vars1_y': ['pT1', 'pT2'],
'cuts1': [skimmedDY_cut + ' (pT2 > 40 && pT2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) && genLep_pt1 > 0 && genLep_pt2 > 0', \
          skimmedDY_cut + ' (pT1 > 40 && pT1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) && genLep_pt1 > 0 && genLep_pt2 > 0'], # 
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

