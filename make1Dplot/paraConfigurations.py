paraConfigs = { }

mc2015_H_path = "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/"
mc2016_H_path = '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_20160716_MuCalib/'

savePath = '/home/mhl/public_html/2016/20161118_mass/'

Hsample_baseCut = 'passedFullSelection && mass4l > 105 && mass4l < 140 '

saveName = 'H15_MC_mass4lErr_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootPath2': mc2015_H_path,
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 5],
'vars1': ['mass4lErr'],
'vars2': ['mass4lErr'],
'cuts1': [Hsample_baseCut + ' && finalState == 1' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1' ],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'mass4lErr',
'yTitle': '',
'legend1': '',
'legend2': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}

saveName = 'H15_MC_mass4lErr_4e'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootPath2': mc2015_H_path,
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 5],
'vars1': ['mass4lErr'],
'vars2': ['mass4lErr'],
'cuts1': [Hsample_baseCut + ' && finalState == 2' ],
'cuts2': [Hsample_baseCut + ' && finalState == 2' ],
'weight1': ['1', '1'], 
'weight2': ['1', '1'],
'xTitle': 'mass4lErr',
'yTitle': '',
'legend1': '',
'legend2': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}

saveName = 'H15_MC_mass4lErr_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootPath2': mc2015_H_path,
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 5],
'vars1': ['mass4lErr'],
'vars2': ['mass4lErr'],
'cuts1': [Hsample_baseCut + ' && finalState > 2' ],
'cuts2': [Hsample_baseCut + ' && finalState > 2' ],
'weight1': ['1', '1'], 
'weight2': ['1', '1'],
'xTitle': 'mass4lErr',
'yTitle': '',
'legend1': '',
'legend2': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'H15_MC_relmass4lErr_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootPath2': mc2015_H_path,
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 0.05],
'vars1': ['mass4lErr/mass4l'],
'vars2': ['mass4lErr/mass4l'],
'cuts1': [Hsample_baseCut + ' && finalState == 1' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1' ],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'mass4lErr/mass4l',
'yTitle': '',
'legend1': '',
'legend2': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ', #latexNote1_mu_pt_eta, #
'latexNote2': ' ' #latexNote2_mu_pt_eta
}


saveName = 'DY15_H_mass4l_all_compare_relM4lBigger0p005'
paraConfigs[saveName] = \
{\
'rootPath1': mc2015_H_path,
'rootPath2': mc2015_H_path,
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4lREFIT'],
'vars2': ['mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErrREFIT/mass4lREFIT > 0.005'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'mass4lREFIT',
'yTitle': '',
'legend1': 'no cut on relM4lErr',
'legend2': 'relM4lErr > 0.005',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': True,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_mz1_mz1refit_bw'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'useBW.root',
'rootfile2': 'useBW.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['massZ1'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'reco',
'legend2': 'refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_mz1_mz1refit_newPara'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'newPara.root',
'rootfile2': 'newPara.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['massZ1'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'reco',
'legend2': 'refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_mz1_mz1refit_test'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'test.root',
'rootfile2': 'test.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['massZ1'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 ' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1 '],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'reco',
'legend2': 'refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}
saveName = 'DY15_H_mz1_mz1refit_bw'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'useBW.root',
'rootfile2': 'useBW.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['massZ1'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 ' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1 '],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'reco',
'legend2': 'refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'DY15_H_genmz1_mz1'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/mhl/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'ggH_2015MC_mH125.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['GENmassZ1'],
'vars2': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && passedFiducialSelection' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && passedFiducialSelection'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'gen',
'legend2': 'reco',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'DY15_H_genmz1_mz1refit_newPara'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/mhl/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'ggH_2015MC_mH125.root',
'rootfile2': 'newPara.root',
'tree1': 'Ana/passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['GENmassZ1'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && passedFiducialSelection' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && passedFiducialSelection'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'gen',
'legend2': 'refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'DY15_H_genmz1_mz1refit_bw'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/mhl/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'ggH_2015MC_mH125.root',
'rootfile2': 'useBW.root',
'tree1': 'Ana/passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['GENmassZ1'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && passedFiducialSelection' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && passedFiducialSelection'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'gen',
'legend2': 'refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_genmz1_mz1refit_kinZfiterPDF'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/mhl/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'ggH_2015MC_mH125.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'Ana/passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['GENmassZ1'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && passedFiducialSelection' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && passedFiducialSelection'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'gen',
'legend2': 'refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_mz1_mz1refit_ifmz1recoBigger91p2'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'useBW.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ1REFIT'],
'vars2': ['massZ1REFIT'], 
'cuts1': [Hsample_baseCut + ' && finalState == 1 && massZ1 > 91.2' ],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && massZ1 > 91.2'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1REFIT',
'yTitle': '',
'legend1': 'use bw',
'legend2': 'use pdf in kinZfitter',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}



saveName = 'DY15_H_mz1reco_mz1refit_pdfInPackage'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'useBW.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 40, 120],
'vars1': ['massZ1'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 '],
'cuts2': [Hsample_baseCut + ' && finalState == 1 '],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'RECO',
'legend2': 'REFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_m4lreco_m4lrefit_pdfInPackage'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'useBW.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [70, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 '],
'cuts2': [Hsample_baseCut + ' && finalState == 1 '],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'mass4l',
'yTitle': '',
'legend1': 'RECO',
'legend2': 'REFIT',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_pTL1_patch2_3'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 5, 105],
'vars1': ['pTL1'],
'vars2': ['pTL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'pTL1_{reco}',
'yTitle': '',
'legend1': 'patch3',
'legend2': 'patch2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}
saveName = 'DY15_H_pTL2_patch2_3'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 5, 105],
'vars1': ['pTL2'],
'vars2': ['pTL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'pTL2_{reco}',
'yTitle': '',
'legend1': 'patch3',
'legend2': 'patch2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'DY15_H_etaL1_patch2_3'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 2.4],
'vars1': ['abs(etaL1)'],
'vars2': ['abs(etaL1)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'etaL1',
'yTitle': '',
'legend1': 'patch3',
'legend2': 'patch2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_etaL2_patch2_3'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 2.4],
'vars1': ['abs(etaL2)'],
'vars2': ['abs(etaL2)'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'etaL2',
'yTitle': '',
'legend1': 'patch3',
'legend2': 'patch2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_pTErrL1_patch2_3'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 10],
'vars1': ['pTErrL1'],
'vars2': ['pTErrL1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'pTErrL1',
'yTitle': '',
'legend1': 'patch3',
'legend2': 'patch2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}
 
saveName = 'DY15_H_pTErrL2_patch2_3'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 10],
'vars1': ['pTErrL2'],
'vars2': ['pTErrL2'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'pTErrL2',
'yTitle': '',
'legend1': 'patch3',
'legend2': 'patch2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}



saveName = 'DY15_H_massZ1reco_patch2_3'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ1'],
'vars2': ['massZ1'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
#'cuts2': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1',
'yTitle': '',
'legend1': 'patch3',
'legend2': 'patch2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'DY15_H_massZ1refit_patch2_3'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'mH_125_addLepErrREFIT.root',
'rootfile2': 'mH_125_addLepErrREFIT.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 80, 100],
'vars1': ['massZ1REFIT'],
'vars2': ['massZ1REFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 > 0'],
'cuts2': [Hsample_baseCut + ' && finalState == 1 && mass4lErr/mass4l*0.48 - mass4lErrREFIT/mass4lREFIT + 0.002 < 0 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'massZ1REFIT',
'yTitle': '',
'legend1': 'patch3',
'legend2': 'patch2',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_m4lErr_reco_refit_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/Mass_2015MC/Fit_PereventMerr/",
'rootPath2': "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/Mass_2015MC/Fit_PereventMerr/",
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 0.03],
'vars1': ['mass4lErr/mass4l'],
'vars2': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
#'cuts2': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'cuts2': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'relM4lErr',
'yTitle': '',
'legend1': 'reco',
'legend2': 'refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_m4lErr_refit_4mu_minos_hesse'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'test_tripleGauss_asyErrMinos.root',
'rootfile2': 'test_tripleGauss_symErrHESSE.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 0.03],
'vars1': ['mass4lErrREFIT/mass4lREFIT'],
'vars2': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
#'cuts2': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'cuts2': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'relM4lErr',
'yTitle': '',
'legend1': 'minos',
'legend2': 'hesse',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_m4lErr_reco_refit_4mu_hesse'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'test_tripleGauss_symErrHESSE.root',
'rootfile2': 'test_tripleGauss_symErrHESSE.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 0.03],
'vars1': ['mass4lErr/mass4l'],
'vars2': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
#'cuts2': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'cuts2': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'relM4lErr',
'yTitle': '',
'legend1': 'reco',
'legend2': 'hesse',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_m4lErr_refit_4mu_minos_average_sqrtSum'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootPath2': "/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/",
'rootfile1': 'test_tripleGauss_asyErrMinos.root',
'rootfile2': 'test_tripleGauss_asyErrMinos_sqrtSum.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 0.03],
'vars1': ['mass4lErrREFIT/mass4lREFIT'],
'vars2': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': [Hsample_baseCut + ' && finalState == 1'],
#'cuts2': [Hsample_baseCut + ' && finalState == 1 && (mass4lErrREFIT/mass4lREFIT)/(mass4lErr/mass4l)<25/18'],
'cuts2': [Hsample_baseCut + ' && finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'relM4lErr',
'yTitle': '',
'legend1': 'minos average',
'legend2': 'minos sqrtSum',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}



saveName = 'H_GENmz1_8tev_13tev_2015_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run1/HZZ4l/SubmitArea_8TeV/Trees_HZZFiducialSamples_Jan8/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['GENmZ1'],
'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 1'],
'cuts2': ['finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '8tev',
'legend2': '13tev',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_GENmz1_8tev_13tev_2015_4e'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run1/HZZ4l/SubmitArea_8TeV/Trees_HZZFiducialSamples_Jan8/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['GENmZ1'],
'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 2'],
'cuts2': ['finalState == 2'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '8tev',
'legend2': '13tev',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'H_GENmz1_8tev_13tev_2015_2e2mu_useGENZ_mass'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run1/HZZ4l/SubmitArea_8TeV/Trees_HZZFiducialSamples_Jan8/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['max(GENmZ1,GENmZ2)'],
'vars2': ['max(GENZ_mass[0],GENZ_mass[1])'], #'GENmassZ1'],
#'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 3'],
'cuts2': ['finalState == 3'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '8tev',
'legend2': '13tev',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_GENmz1_8tev_13tev_2015_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run1/HZZ4l/SubmitArea_8TeV/Trees_HZZFiducialSamples_Jan8/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['GENmZ1'],
'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 4'],
'cuts2': ['finalState == 4'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '8tev',
'legend2': '13tev',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_GENmz1_13tev_2015_2016_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_20160716_MuCalib/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISpring16MiniAODv2.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['GENmassZ1'],
'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 1'],
'cuts2': ['finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '2015',
'legend2': '2016',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_GENmz1_13tev_2015_2016_4e'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_20160716_MuCalib/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISpring16MiniAODv2.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['GENmassZ1'],
'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 2'],
'cuts2': ['finalState == 2'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '2015',
'legend2': '2016',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_GENmz1_13tev_2015_2016_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_20160716_MuCalib/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISpring16MiniAODv2.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['GENmassZ1'],
'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 3'],
'cuts2': ['finalState == 3'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '2015',
'legend2': '2016',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'H_GENmz1_13tev_2015_2016_2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_20160716_MuCalib/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISpring16MiniAODv2.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['GENmassZ1'],
'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 4'],
'cuts2': ['finalState == 4'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '2015',
'legend2': '2016',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}




saveName = 'H_GENmz1_8tev_13tev_2015_4e_useGENZ_mass'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run1/HZZ4l/SubmitArea_8TeV/Trees_HZZFiducialSamples_Jan8/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['max(GENmZ1,GENmZ2)'],
'vars2': ['max(GENZ_mass[0],GENZ_mass[1])'], #'GENmassZ1'],
#'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 2'],
'cuts2': ['finalState == 2'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '8tev',
'legend2': '13tev',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'H_GENmz1_8tev_13tev_2015_2mu2e_useGENZ_mass'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run1/HZZ4l/SubmitArea_8TeV/Trees_HZZFiducialSamples_Jan8/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['GENmZ1'],
'vars2': ['max(GENZ_mass[0],GENZ_mass[1])'], #'GENmassZ1'],
#'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 4'],
'cuts2': ['finalState == 4'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '8tev',
'legend2': '13tev',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'H_GENmz1_8tev_13tev_2015_4mu_useGENZ_mass'
paraConfigs[saveName] = \
{\
'rootPath1': "/cms/data/store/user/t2/users/dsperka/Run1/HZZ4l/SubmitArea_8TeV/Trees_HZZFiducialSamples_Jan8/",
'rootPath2': "/cms/data/store/user/t2/users/mhl/",
'rootfile1': 'SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6.root',
'rootfile2': 'ggH_2015MC_mH125.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 50, 110],
'vars1': ['max(GENmZ1,GENmZ2)'],
'vars2': ['max(GENZ_mass[0],GENZ_mass[1])'], #'GENmassZ1'],
#'vars2': ['GENmassZ1'],
'cuts1': ['finalState == 1'],
'cuts2': ['finalState == 1'],
'weight1': ['1', '1'],
'weight2': ['1', '1'],
'xTitle': 'GENmassZ1',
'yTitle': '',
'legend1': '8tev',
'legend2': '13tev',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #latexNote1_mu_pt_eta, #
'latexNote2': '', #latexNote2_mu_pt_eta
'doFit': False,
'pdfName': 'doubleCB'
}

