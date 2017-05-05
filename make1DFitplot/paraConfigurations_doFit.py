paraConfigs = { }

savePath = '/home/mhl/public_html/2017/20170503_testUnbinFitCode/'

saveName = 'GENMZ_2016MC_e_massZ'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v1_20170201/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo': [100, 60, 120],
'vars1': ['genzm'],
'cuts1': [' genLep_pt1 > 0 && genLep_pt2 > 0 && massZ > 60 && massZ < 120'], #
'weight1': ['1'],
'xTitle': 'GENMZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


saveName = 'm4lreco_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lrefit_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
#'rootfile1': 'ggH125_2016MC.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState == 2 && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'xTitle': 'mass4lREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lreco_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'], #
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
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState == 1 && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'xTitle': 'mass4lREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lreco_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lrefit_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'xTitle': 'mass4lREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}



saveName = 'GENmassZ2_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb11/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 12, 100],
'vars1': ['GENmassZ2'],
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'],
'weight1': ['1'],
'xTitle': 'GENmassZ2',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'GENmassZ2_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb11/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 12, 100],
'vars1': ['GENmassZ2'],
'cuts1': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140'],
'weight1': ['1'],
'xTitle': 'GENmassZ2',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'GENmassZ2_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb11/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 12, 100],
'vars1': ['GENmassZ2'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'],
'weight1': ['1'],
'xTitle': 'GENmassZ2',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'massZ2_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb11/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [50, 12, 60],
'vars1': ['massZ2'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'],
'weight1': ['1'],
'xTitle': 'massZ2',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lErrPull_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo': [100, -10, 10],
'vars1': ['(mass4l-GENmass4l)/mass4lErr'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': '(mass4l-GENmass4l)/mass4lErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lErrPull_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo': [100, -10, 10],
'vars1': ['(mass4l-GENmass4l)/mass4lErr'],
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': '(mass4l-GENmass4l)/mass4lErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lErrPull_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo': [100, -10, 10],
'vars1': ['(mass4l-GENmass4l)/mass4lErr'],
'cuts1': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': '(mass4l-GENmass4l)/mass4lErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lErrREFITPull_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo': [100, -10, 10],
'vars1': ['(mass4lREFIT-GENmass4l)/mass4lErrREFIT'],
'cuts1': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': '(mass4lREFIT-GENmass4l)/mass4lErrREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}



saveName = 'm4lErrREFITPull_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo': [100, -10, 10],
'vars1': ['(mass4lREFIT-GENmass4l)/mass4lErrREFIT'],
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': '(mass4lREFIT-GENmass4l)/mass4lErrREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lErrREFITPull_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo': [100, -10, 10],
'vars1': ['(mass4lREFIT-GENmass4l)/mass4lErrREFIT'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': '(mass4lREFIT-GENmass4l)/mass4lErrREFIT',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}






saveName = 'm4lreco_2e2mu_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lreco_2e2mu_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lreco_4mu_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lreco_4mu_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'm4lreco_4e_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

saveName = 'm4lreco_4e_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'm4l_up_dn.root',
'tree1': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'Z4L_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4mu_nofsr'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
#'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
#'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_noFSR'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l_nofsr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4mu_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}

saveName = 'Z4L_4mu_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4mu_tchan'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}


saveName = 'Z4L_4mu_tchan_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}


saveName = 'Z4L_4mu_tchan_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}

saveName = 'Z4L_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}

saveName = 'Z4L_4e_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4e_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4e_tchan'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}



saveName = 'Z4L_4e_tchan_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}


saveName = 'Z4L_4e_tchan_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}


saveName = 'Z4L_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState > 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_2e2mu_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState > 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_2e2mu_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState > 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_2e2mu_tchan'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState > 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}


saveName = 'Z4L_2e2mu_tchan_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_up'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState > 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}


saveName = 'Z4L_2e2mu_tchan_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l_dn'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState > 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bkg'
}


saveName = 'Z4L_4mu_gen'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENmass4l'],
'cuts1': ['GENmass4l > 70 && GENmass4l < 105 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4e_gen'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENmass4l'],
'cuts1': ['GENmass4l > 70 && GENmass4l < 105 && finalState == 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_2e2mu_gen'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENmass4l'],
'cuts1': ['GENmass4l > 70 && GENmass4l < 105 && finalState > 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}



saveName = 'Z4L_2e2mu_gen'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENmass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState > 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}




saveName = 'H4L_4mu_rms_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'], #
'weight1': ['pdfRMSup'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4mu_rms_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'], #
'weight1': ['pdfRMSdown'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4mu_env_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'], #
'weight1': ['pdfENVup'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4mu_env_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'], #
'weight1': ['pdfENVdown'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4e_rms_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 2'], #
'weight1': ['pdfRMSup'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4e_rms_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 2'], #
'weight1': ['pdfRMSdown'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4e_env_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 2'], #
'weight1': ['pdfENVup'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4e_env_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 2'], #
'weight1': ['pdfENVdown'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'H4L_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 2'], #
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}


saveName = 'Z4L_4mu_rms_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['pdfRMSup'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath, 
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4mu_rms_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['pdfRMSdown'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4e_rms_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['pdfRMSup'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4e_rms_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['pdfRMSdown'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4mu_env_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['pdfENVup'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4mu_env_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'], #
'weight1': ['pdfENVdown'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4e_env_up'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['pdENVup'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'Z4L_4e_env_dn'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['mass4l'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 2'], #
'weight1': ['pdfENVdown'],
'xTitle': 'mass4l',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'GENZM_1_ZZSample'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root',
#'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENZ_mass[0]'],
'cuts1': ['GENmass4l > 180 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}

saveName = 'GENZM_1_ZZSample_tchan'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENZ_mass[0]'],
'cuts1': ['GENmass4l > 160'], #
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


saveName = 'GENZM_2_ZZSample'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENZ_mass[1]'],
'cuts1': ['GENmass4l > 180 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


saveName = 'GENZM_2_ZZSample_tchan'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENZ_mass[1]'],
'cuts1': ['GENmass4l > 160'], #
'weight1': ['1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'bw'
}


saveName = 'massZ_2_ZZSample'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['massZ2'],
'cuts1': ['mass4l > 180 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'massZ2',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxDCB'
}


saveName = 'massZ_1_ZZSample'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['massZ1'],
'cuts1': ['mass4l > 180 && finalState == 1'], #
'weight1': ['1'],
'xTitle': 'massZ1',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'BWxDCB'
}


saveName = 'massZ_ZZSample'
paraConfigs[saveName] = \
{\
#'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/',
#'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root',
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['massZ1','massZ2'],
'cuts1': ['passedFullSelection && mass4l > 180 && finalState == 1',\
          'passedFullSelection && mass4l > 180 && finalState == 1'], #
'weight1': ['1','1'],
'xTitle': 'massZ',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'GENZM_ZZSample'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'test.root',
'tree1': 'passedEvents',
'binInfo': [100, 70, 105],
'vars1': ['GENmassZ1','GENmassZ2'],
'cuts1': ['GENmass4l > 180 && finalState == 1','GENmass4l > 180 && finalState == 1'], #
'weight1': ['1','1'],
'xTitle': 'GENZM',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'model'
}


saveName = 'test_pT1_residual'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
#'rootfile1': 'ggH125_2016MC.root',
'tree1': 'passedEvents',
'binInfo': [100, -0.15, 0.15],
'vars1': ['(pTL1-pTGENL1)/pTGENL1'],
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'],
'weight1': ['1'],
'xTitle': '(pTL1-pTGENL1)/pTGENL1',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

