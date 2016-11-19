paraConfigs = { }

mc2015_dy_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/inputRootFiles/'
mc2016_dy_path = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/inputRoot/forApproval/'
mc2015_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/'
mc2016_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/makeSlimTree/'

mc2015_dy_path_v4 = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4/"
mc2015_dy_path_v4_NoMZCut = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4_NOmassZCut/"

savePath = '/home/mhl/public_html/2016/20161116_mass/'

#make plots in different ptEta bins
skimmedDY_cut = 'massZ > 80 && massZ < 100 && massZErr > 0.2 && massZErr < 7.2 && Met < 30 && '
skimmedDY_cutOnGEN = 'GENmass2l > 80 && GENmass2l < 100 && '

saveName = 'pullZ_2015MC'
paraConfigs['mc_DY15_pullz'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(massZ-GENmass2l)/massZErr'],
'cuts1': [skimmedDY_cut + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'weight1': ['1'],
'xTitle': '(massZ_{reco}-GENmass2l)/massZErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'GENmass2l_2015MC'
paraConfigs['mc_DY15_GENmass2l'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


oneGENMuPt_40_50 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 ) || (genLep_pt2 > 40 && genLep_pt2 < 50) ) '
saveName = 'GENmass2l_2015MC_oneGENMuPt_40_50'
paraConfigs['mc_DY15_GENmass2l_oneGENMuPt_40_50'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + oneGENMuPt_40_50], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


oneGENMuPt_40_50_eta_0_0p9 = ' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9) || \
                                ( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'GENmass2l_2015MC_oneGENMuPt_40_50_eta_0_0p9'
paraConfigs['mc_DY15_GENmass2l_oneGENMuPt_40_50_eta_0_0p9'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + oneGENMuPt_40_50_eta_0_0p9], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


oneGENMuPt_10_40_eta_0_0p9 = ' (( genLep_pt1 > 10 && genLep_pt1 < 40 && abs(eta1) > 0 && abs(eta1) < 0.9) || \
                                ( genLep_pt2 > 10 && genLep_pt2 < 40 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'GENmass2l_2015MC_oneGENMuPt_10_40_eta_0_0p9'
paraConfigs['mc_DY15_GENmass2l_oneGENMuPt_10_40_eta_0_0p9'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + oneGENMuPt_10_40_eta_0_0p9], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


oneGENMuPt_50_100_eta_0_0p9 = ' (( genLep_pt1 > 50 && genLep_pt1 < 100 && abs(eta1) > 0 && abs(eta1) < 0.9) || \
                                ( genLep_pt2 > 50 && genLep_pt2 < 100 && abs(eta2) > 0 && abs(eta2) < 0.9) ) '
saveName = 'GENmass2l_2015MC_oneGENMuPt_50_100_eta_0_0p9'
paraConfigs['mc_DY15_GENmass2l_oneGENMuPt_50_100_eta_0_0p9'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + oneGENMuPt_50_100_eta_0_0p9], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


oneGENMuPt_40_50_eta_0_0p9_otherGENmuPt_10_40 = \
' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9 && genLep_pt2 > 10 && genLep_pt2 < 40 ) || \
   ( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9 && genLep_pt1 > 10 && genLep_pt1 < 40 ) ) '
saveName = 'GENmass2l_2015MC_oneGENMuPt_40_50_eta_0_0p9_otherGENMuPt_10_40'
paraConfigs['mc_DY15_GENmass2l_oneGENMuPt_40_50_eta_0_0p9_otherGENMuPt_10_40'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + oneGENMuPt_40_50_eta_0_0p9_otherGENmuPt_10_40], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


oneGENMuPt_40_50_eta_0_0p9_otherGENmuPt_10_40_eta_0_0p9 = \
' (( genLep_pt1 > 40 && genLep_pt1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9 && genLep_pt2 > 10 && genLep_pt2 < 40 && abs(eta2) > 0 && abs(eta2) < 0.9) || \
   ( genLep_pt2 > 40 && genLep_pt2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9 && genLep_pt1 > 10 && genLep_pt1 < 40 && abs(eta1) > 0 && abs(eta1) < 0.9) ) '
saveName = 'GENmass2l_2015MC_oneGENMuPt_40_50_eta_0_0p9_otherGENMuPt_10_40_eta_0_0p9'
paraConfigs['mc_DY15_GENmass2l_oneGENMuPt_40_50_eta_0_0p9_otherGENMuPt_10_40_eta_0_0p9'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + oneGENMuPt_40_50_eta_0_0p9_otherGENmuPt_10_40_eta_0_0p9], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


saveName = 'DY15_MC_pTResidual'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -0.1, 0.1],
'vars1': ['(pT1-genLep_pt1)/genLep_pt1', '(pT2-genLep_pt2)/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0', skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pT_{gen}',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'DY15_MC_pTResidual_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -0.1, 0.1],
'vars1': ['(pT1-genLep_pt1)/genLep_pt1', '(pT2-genLep_pt2)/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta1) < 0.9 ', \
          skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta2) < 0.9 '], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pT_{gen}',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'DY15_MC_pTResidual_0p9_1p8'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -0.1, 0.1],
'vars1': ['(pT1-genLep_pt1)/genLep_pt1', '(pT2-genLep_pt2)/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta1) < 1.8 && abs(genLep_eta1) > 0.9 ', \
          skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta2) < 1.8 && abs(genLep_eta2) > 0.9'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pT_{gen}',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'DY15_MC_pTResidual_1p8_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -0.1, 0.1],
'vars1': ['(pT1-genLep_pt1)/genLep_pt1', '(pT2-genLep_pt2)/genLep_pt2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta1) < 2.4 && abs(genLep_eta1) > 1.8', \
          skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && abs(genLep_eta2) < 2.4 && abs(genLep_eta2) > 1.8'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pT_{gen}',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'DY15_MC_pTPull'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(pT1-genLep_pt1)/pterr1', '(pT2-genLep_pt2)/pterr2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0', skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


twoGENMu_eta_0_0p9 = ' ( abs(genLep_eta1) < 0.9 && abs(genLep_eta2) < 0.9) '
saveName = 'GENmass2l_2015MC_twoGENMu_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 5 && genLep_pt2 > 5 && genLep_pt1 < 100 && genLep_pt2 < 100 && ' + twoGENMu_eta_0_0p9], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}

saveName = 'GENZM_2015MC'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN+ ' genLep_pt1 > 5 && genLep_pt2 > 5 && genLep_pt1 < 100 && genLep_pt2 < 100'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}

saveName = 'GENZM_2015MC_genzm_80_100'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': ['genzm > 80 && genzm < 100'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}
saveName = 'GENZM_2015MC_genzm_70_110'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 110],
'vars1': ['genzm'],
'cuts1': ['genzm > 70 && genzm < 110'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}

#twoGENMu_eta_0_0p9 = ' ( abs(eta1) < 0.9 && abs(eta2) < 0.9) '
saveName = 'massZ_2015MC_twoGENMu_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + twoGENMu_eta_0_0p9], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}

saveName = 'massZ_2015MC'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cut + ' 1 '], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
#'pdfName': 'BWxCB'
}

saveName = 'massZ_2016MC'
paraConfigs[saveName] = \
{\
'rootPath1': mc2016_dy_path_withgenpt,
'rootfile1': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cut + ' 1 '], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
#'pdfName': 'BWxCB'
}

saveName = 'GENZM_2016MC'
paraConfigs[saveName] = \
{\
'rootPath1': mc2016_dy_path_withgenpt,
'rootfile1': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': ['genzm > 80 && genzm < 100'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}

twoGENMu_eta_0p9_1p8 = ' ( abs(genLep_eta1) < 1.8 && abs(genLep_eta1) > 0.9 && abs(genLep_eta2) < 1.8 && abs(genLep_eta2) > 0.9) '
saveName = 'GENmass2l_2015MC_twoGENMu_eta_0p9_1p8'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 5 && genLep_pt2 > 5 && genLep_pt1 < 100 && genLep_pt2 < 100 && ' + twoGENMu_eta_0p9_1p8], #
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


saveName = 'massZ_2015MC_twoGENMu_eta_0p9_1p8'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + twoGENMu_eta_0p9_1p8], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


twoGENMu_eta_1p8_2p4 = ' ( abs(genLep_eta1) < 2.4 && abs(genLep_eta1) > 1.8 && abs(genLep_eta2) < 2.4 && abs(genLep_eta2) > 1.8) '
saveName = 'GENmass2l_2015MC_twoGENMu_eta_1p8_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 5 && genLep_pt2 > 5 && genLep_pt1 < 100 && genLep_pt2 < 100 && ' + twoGENMu_eta_1p8_2p4], #
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


saveName = 'massZ_2015MC_twoGENMu_eta_1p8_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 0 && genLep_pt2 > 0 && ' + twoGENMu_eta_1p8_2p4], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_massZErrSmallThan1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cut + ' massZErr < 1 '], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_massZErrSmallThan0p9'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cut + ' massZErr < 0.9 '], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_massZErr_0p6_0p7'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cut + ' massZErr < 0.7 && massZErr > 0.6'], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_relmassZErr_0p01_0p012'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cut + ' massZErr/massZ < 0.012 && massZErr/massZ > 0.01'], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_relmassZErr_0_0p01'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cut + ' massZErr/massZ < 0.01 && massZErr/massZ > 0'], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


twoGENe_eta_0_0p7 = ' ( abs(genLep_eta1) < 0.7 && abs(genLep_eta2) < 0.7) '
saveName = 'GENmass2l_2015MC_twoGENe_eta_0_0p7'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 7 && genLep_pt2 > 7 && ' + twoGENe_eta_0_0p7], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


twoGENe_eta_0p7_1 = ' ( abs(genLep_eta1) > 0.7 && abs(genLep_eta2) > 0.7 && abs(genLep_eta1) < 1 && abs(genLep_eta2) < 1) '
saveName = 'GENmass2l_2015MC_twoGENe_eta_0p7_1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 7 && genLep_pt2 > 7 && ' + twoGENe_eta_0p7_1], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}

twoGENe_eta_1_1p5 = ' ( abs(genLep_eta1) > 1 && abs(genLep_eta2) > 1 && abs(genLep_eta1) < 1.5 && abs(genLep_eta2) < 1.5) '
saveName = 'GENmass2l_2015MC_twoGENe_eta_1_1p5'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 7 && genLep_pt2 > 7 && ' + twoGENe_eta_1_1p5], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


twoGENe_eta_1p5_2p5 = ' ( abs(genLep_eta1) > 1.5 && abs(genLep_eta2) > 1.5 && abs(genLep_eta1) < 2.5 && abs(genLep_eta2) < 2.5) '
saveName = 'GENmass2l_2015MC_twoGENe_eta_1p5_2p5'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENmass2l'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 7 && genLep_pt2 > 7 && ' + twoGENe_eta_1p5_2p5], #
'weight1': ['1'],
'xTitle': 'GENmass2l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


twoGENe_eta_0_0p7 = ' ( abs(genLep_eta1) < 0.7 && abs(genLep_eta2) < 0.7) '
saveName = 'massZ_2015MC_twoGENe_eta_0_0p7'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 7 && genLep_pt2 > 7 && ' + twoGENe_eta_0_0p7], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


twoGENe_eta_0p7_1 = ' ( abs(genLep_eta1) > 0.7 && abs(genLep_eta2) > 0.7 && abs(genLep_eta1) < 1 && abs(genLep_eta2) < 1) '
saveName = 'massZ_2015MC_twoGENe_eta_0p7_1'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 7 && genLep_pt2 > 7 && ' + twoGENe_eta_0p7_1], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


twoGENe_eta_1_1p5 = ' ( abs(genLep_eta1) > 1 && abs(genLep_eta2) > 1 && abs(genLep_eta1) < 1.5 && abs(genLep_eta2) < 1.5) '
saveName = 'massZ_2015MC_twoGENe_eta_1_1p5'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 7 && genLep_pt2 > 7 && ' + twoGENe_eta_1_1p5], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


twoGENe_eta_1p5_2p5 = ' ( abs(genLep_eta1) > 1.5 && abs(genLep_eta2) > 1.5 && abs(genLep_eta1) < 2.5 && abs(genLep_eta2) < 2.5) '
saveName = 'massZ_2015MC_twoGENe_eta_1p5_2p5'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 7 && genLep_pt2 > 7 && ' + twoGENe_eta_1p5_2p5], #
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
}


HMC_2015_liteMarco = "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/"

saveName = 'm4l_4mu.root'
paraConfigs[saveName] = \
{\
'rootPath1': HMC_2015_liteMarco,
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lrefit_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': HMC_2015_liteMarco,
#'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile1': 'test_tripleGauss_asyErrMinos.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4lREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lrefit_4mu_beforeCorrErr.root'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4lREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

H_genIndexCut_4mu='passedFullSelection&&finalState==1&& lep_genindex[lep_Hindex[0]]>=0&& lep_genindex[lep_Hindex[1]]>=0&& lep_genindex[lep_Hindex[2]]>=0&& lep_genindex[lep_Hindex[3]]>=0'
saveName = 'pTPull_genpT_5_10_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(lep_pt[lep_Hindex[0]]-GENlep_pt[lep_genindex[lep_Hindex[0]]])/lep_pterr[lep_Hindex[0]]', \
          '(lep_pt[lep_Hindex[1]]-GENlep_pt[lep_genindex[lep_Hindex[1]]])/lep_pterr[lep_Hindex[1]]', \
          '(lep_pt[lep_Hindex[2]]-GENlep_pt[lep_genindex[lep_Hindex[2]]])/lep_pterr[lep_Hindex[2]]', \
          '(lep_pt[lep_Hindex[3]]-GENlep_pt[lep_genindex[lep_Hindex[3]]])/lep_pterr[lep_Hindex[3]]'],
'cuts1': [H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[0]]] > 5 && GENlep_pt[lep_genindex[lep_Hindex[0]]] < 10 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[1]]] > 5 && GENlep_pt[lep_genindex[lep_Hindex[1]]] < 10 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[2]]] > 5 && GENlep_pt[lep_genindex[lep_Hindex[2]]] < 10 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[3]]] > 5 && GENlep_pt[lep_genindex[lep_Hindex[3]]] < 10 '], #
'weight1': ['1', '1', '1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'pTPull_genpT_10_20_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(lep_pt[lep_Hindex[0]]-GENlep_pt[lep_genindex[lep_Hindex[0]]])/lep_pterr[lep_Hindex[0]]', \
          '(lep_pt[lep_Hindex[1]]-GENlep_pt[lep_genindex[lep_Hindex[1]]])/lep_pterr[lep_Hindex[1]]', \
          '(lep_pt[lep_Hindex[2]]-GENlep_pt[lep_genindex[lep_Hindex[2]]])/lep_pterr[lep_Hindex[2]]', \
          '(lep_pt[lep_Hindex[3]]-GENlep_pt[lep_genindex[lep_Hindex[3]]])/lep_pterr[lep_Hindex[3]]'],
'cuts1': [H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[0]]] > 10 && GENlep_pt[lep_genindex[lep_Hindex[0]]] < 20 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[1]]] > 10 && GENlep_pt[lep_genindex[lep_Hindex[1]]] < 20 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[2]]] > 10 && GENlep_pt[lep_genindex[lep_Hindex[2]]] < 20 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[3]]] > 10 && GENlep_pt[lep_genindex[lep_Hindex[3]]] < 20 '], #
'weight1': ['1', '1', '1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'pTPull_genpT_20_30_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(lep_pt[lep_Hindex[0]]-GENlep_pt[lep_genindex[lep_Hindex[0]]])/lep_pterr[lep_Hindex[0]]', \
          '(lep_pt[lep_Hindex[1]]-GENlep_pt[lep_genindex[lep_Hindex[1]]])/lep_pterr[lep_Hindex[1]]', \
          '(lep_pt[lep_Hindex[2]]-GENlep_pt[lep_genindex[lep_Hindex[2]]])/lep_pterr[lep_Hindex[2]]', \
          '(lep_pt[lep_Hindex[3]]-GENlep_pt[lep_genindex[lep_Hindex[3]]])/lep_pterr[lep_Hindex[3]]'],
'cuts1': [H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[0]]] > 20 && GENlep_pt[lep_genindex[lep_Hindex[0]]] < 30 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[1]]] > 20 && GENlep_pt[lep_genindex[lep_Hindex[1]]] < 30 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[2]]] > 20 && GENlep_pt[lep_genindex[lep_Hindex[2]]] < 30 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[3]]] > 20 && GENlep_pt[lep_genindex[lep_Hindex[3]]] < 30 '], #
'weight1': ['1', '1', '1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'pTPull_genpT_30_40_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(lep_pt[lep_Hindex[0]]-GENlep_pt[lep_genindex[lep_Hindex[0]]])/lep_pterr[lep_Hindex[0]]', \
          '(lep_pt[lep_Hindex[1]]-GENlep_pt[lep_genindex[lep_Hindex[1]]])/lep_pterr[lep_Hindex[1]]', \
          '(lep_pt[lep_Hindex[2]]-GENlep_pt[lep_genindex[lep_Hindex[2]]])/lep_pterr[lep_Hindex[2]]', \
          '(lep_pt[lep_Hindex[3]]-GENlep_pt[lep_genindex[lep_Hindex[3]]])/lep_pterr[lep_Hindex[3]]'],
'cuts1': [H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[0]]] > 30 && GENlep_pt[lep_genindex[lep_Hindex[0]]] < 40 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[1]]] > 30 && GENlep_pt[lep_genindex[lep_Hindex[1]]] < 40 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[2]]] > 30 && GENlep_pt[lep_genindex[lep_Hindex[2]]] < 40 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[3]]] > 30 && GENlep_pt[lep_genindex[lep_Hindex[3]]] < 40 '], #
'weight1': ['1', '1', '1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'pTPull_genpT_40_50_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(lep_pt[lep_Hindex[0]]-GENlep_pt[lep_genindex[lep_Hindex[0]]])/lep_pterr[lep_Hindex[0]]', \
          '(lep_pt[lep_Hindex[1]]-GENlep_pt[lep_genindex[lep_Hindex[1]]])/lep_pterr[lep_Hindex[1]]', \
          '(lep_pt[lep_Hindex[2]]-GENlep_pt[lep_genindex[lep_Hindex[2]]])/lep_pterr[lep_Hindex[2]]', \
          '(lep_pt[lep_Hindex[3]]-GENlep_pt[lep_genindex[lep_Hindex[3]]])/lep_pterr[lep_Hindex[3]]'],
'cuts1': [H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[0]]] > 40 && GENlep_pt[lep_genindex[lep_Hindex[0]]] < 50 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[1]]] > 40 && GENlep_pt[lep_genindex[lep_Hindex[1]]] < 50 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[2]]] > 40 && GENlep_pt[lep_genindex[lep_Hindex[2]]] < 50 ', \
          H_genIndexCut_4mu+' && GENlep_pt[lep_genindex[lep_Hindex[3]]] > 40 && GENlep_pt[lep_genindex[lep_Hindex[3]]] < 50 '], #
'weight1': ['1', '1', '1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'DY15_MC_pTPull_genpT_5_10'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(pT1-genLep_pt1)/pterr1', '(pT2-genLep_pt2)/pterr2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 5 && genLep_pt1 < 10',\
          skimmedDY_cutOnGEN + ' genLep_pt2 > 5 && genLep_pt2 < 10'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'DY15_MC_pTPull_genpT_10_20'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(pT1-genLep_pt1)/pterr1', '(pT2-genLep_pt2)/pterr2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 10 && genLep_pt1 < 20', \
          skimmedDY_cutOnGEN + ' genLep_pt2 > 10 && genLep_pt2 < 20'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'DY15_MC_pTPull_genpT_20_30'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(pT1-genLep_pt1)/pterr1', '(pT2-genLep_pt2)/pterr2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 20 && genLep_pt1 < 30',\
          skimmedDY_cutOnGEN + ' genLep_pt2 > 20 && genLep_pt2 < 30'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'DY15_MC_pTPull_genpT_30_40'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(pT1-genLep_pt1)/pterr1', '(pT2-genLep_pt2)/pterr2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 30 && genLep_pt1 < 40',\
          skimmedDY_cutOnGEN + ' genLep_pt2 > 30 && genLep_pt2 < 40'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'DY15_MC_pTPull_genpT_40_50'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(pT1-genLep_pt1)/pterr1', '(pT2-genLep_pt2)/pterr2'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 40 && genLep_pt1 < 50',\
          skimmedDY_cutOnGEN + ' genLep_pt2 > 40 && genLep_pt2 < 50'], #
'weight1': ['1', '1'],
'xTitle': '(pT_{reco}-pT_{gen})/pTErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'DY15_MC_mass2lPull_inclusive'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80,100],
'vars1': ['massZ'],
'cuts1': [skimmedDY_cutOnGEN + ' genLep_pt1 > 5 && genLep_pt1 < 100 && genLep_pt2 > 5 && genLep_pt2 < 100'],
'weight1': ['1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxCB'
#'pdfName': 'model'
}


saveName = 'm4l_inclusive'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection&& finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4l_inclusive_16MC'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISpring16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection&& finalState == 1'],
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lREFIT_15MC_afterCorr'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/Mass_2015MC/Fit_PereventMerr/',
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4lREFIT'],
'cuts1': ['passedFullSelection&& finalState == 1 && mass4l > 105 && mass4l < 140'],
'weight1': ['1'],
'xTitle': 'mass4lREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4l_15MC_afterCorr'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/Mass_2015MC/Fit_PereventMerr/',
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection&& finalState == 1 && mass4l > 105 && mass4l < 140'],
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lREFIT_15MC_beforeCorr'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4lREFIT'],
'cuts1': ['passedFullSelection&& finalState == 1 && mass4l > 105 && mass4l < 140'],
'weight1': ['1'],
'xTitle': 'mass4lREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'DY_GENZM_noSlim'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/',
'rootfile1': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENZ_mass[0]'],
'cuts1': ['GENZ_mass[0] > 80 && GENZ_mass[0] < 100'],
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


saveName = 'DY_GENZM_massZ_80_100'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/',
'rootfile1': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['GENZ_mass[0]'],
'cuts1': ['GENZ_mass[0] > 80 && GENZ_mass[0] < 100 && massZ > 80 && massZ < 100'],
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


saveName = 'massZ_2015MC_testNoMzCutWhenSlim'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN + '  genzm > 80 && genzm < 100'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_testNoMzCutWhenSlim_massZ_80_100'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN + '  genzm > 80 && genzm < 100 && massZ > 80 && massZ < 100'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}

saveName = 'massZ_2015MC_testNoMzCutWhenSlim_nocutongen'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': ['1'],#'  genzm > 80 && genzm < 100'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}

saveName = 'massZ_2015MC_testNoMzCutWhenSlim_massZ_80_100_nocutongen'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': ['  genzm > 80 && genzm < 100 && massZ > 80 && massZ < 100'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}
saveName = 'massZ_2015MC_testNoMzCutWhenSlim_massZ_70_110_nocutongen'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [120, 70, 110],
'vars1': ['genzm'],
'cuts1': ['  genzm > 70 && genzm < 110 && massZ > 70 && massZ < 110'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}
saveName = 'massZ_2015MC_testNoMzCutWhenSlim_massZ_60_120_nocutongen'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [140, 60, 120],
'vars1': ['genzm'],
'cuts1': ['  genzm > 60 && genzm < 120 && massZ > 60 && massZ < 120'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_testNoMzCutWhenSlim_massZ_75_105'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN + '  genzm > 80 && genzm < 100 && massZ > 75 && massZ < 105'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_testNoMzCutWhenSlim_massZ_biggerthan80'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN + '  genzm > 80 && genzm < 100 && massZ > 80'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}


saveName = 'massZ_2015MC_testNoMzCutWhenSlim_massZ_smallerthan100'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_dy_path_v4_NoMZCut,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['genzm'],
'cuts1': [skimmedDY_cutOnGEN + '  genzm > 80 && genzm < 100 && massZ < 100'], #
'weight1': ['1'],
'xTitle': 'genzm',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
#'pdfName': 'BWxCB'
}


saveName = 'm4l_15MC_relM4lErr_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/Mass_2015MC/Fit_PereventMerr/',
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection&& finalState == 1 && mass4l > 105 && mass4l < 140 && mass4lErr/mass4l < 0.005'],
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4l_15MC_relM4lErrREFIT_0_0p005'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/Mass_2015MC/Fit_PereventMerr/',
'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection&& finalState == 1 && mass4l > 105 && mass4l < 140 && mass4lErrREFIT/mass4lREFIT < 0.005'],
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'GENmassZ1_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 50, 105],
'vars1': ['GENmassZ1'],
'cuts1': ['passedFullSelection && passedFiducialSelection && finalState == 1'],
'weight1': ['1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
#'pdfName': 'BWplusDCB'
'pdfName': 'pdfpdfgenmz1'
}

saveName = 'GENmassZ1_4mu_test_cb2gauss'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 50, 105],
'vars1': ['GENmassZ1'],
'cuts1': ['passedFullSelection && passedFiducialSelection && finalState == 1'],
'weight1': ['1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
#'pdfName': 'singleCB'
'pdfName': 'pdfgenmz1'
}

saveName = 'GENmassZ1_4mu_tail'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 50, 88],
'vars1': ['GENmassZ1'],
'cuts1': ['passedFullSelection && passedFiducialSelection && finalState == 1'],
'weight1': ['1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bernstein'
#'pdfName': 'genmz1'
}

saveName = 'GENmassZ1_4mu_old'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['GENmassZ1'],
'cuts1': ['passedFullSelection && passedFiducialSelection && finalState == 1'],
'weight1': ['1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
#'pdfName': 'singleCB'
'pdfName': 'RelBWxCBxgauss'
}

saveName = 'GENmassZ1_4mu_reParaOld'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 45, 105],
'vars1': ['GENmassZ1'],
'cuts1': ['passedFullSelection && passedFiducialSelection && finalState == 1'],
'weight1': ['1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
#'pdfName': 'bw'
'pdfName': 'BWplusCB'
}


saveName = 'pT_pull'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
#'rootfile1': 'newPara_tripleGauss.root',
'rootfile1': 'test_tripleGauss_asyErrMinos.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(pTL1-pTGENL1)/pTErrREFITL1', \
          '(pTL2-pTGENL2)/pTErrREFITL2', \
          '(pTL3-pTGENL3)/pTErrREFITL3', \
          '(pTL4-pTGENL4)/pTErrREFITL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140' + ' && finalState == 1',\
          'passedFullSelection && mass4l > 105 && mass4l < 140' + ' && finalState == 1', \
          'passedFullSelection && mass4l > 105 && mass4l < 140' + ' && finalState == 1',\
          'passedFullSelection && mass4l > 105 && mass4l < 140' + ' && finalState == 1'],
'weight1': ['1', '1', '1', '1'],
'xTitle': '(pT_{refit}-pT_{gen}/pTErrREFIT)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '',
'pdfName': 'doubleCB' #
}


saveName = 'm4l_pull'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/',
'rootfile1': 'test_tripleGauss_symErrHESSE.root',
#'rootfile1': 'test_tripleGauss_asyErrMinos.root',
#'rootfile1': 'mH_125.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(mass4lREFIT-GENmass4l)/mass4lErrREFIT'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140' + ' && finalState == 1'],
'weight1': ['1'],
'xTitle': '',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '',
'pdfName': 'doubleCB' #
}

