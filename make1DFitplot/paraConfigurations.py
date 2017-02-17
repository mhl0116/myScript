paraConfigs = { }

savePath = '/home/mhl/public_html/2017/20170216_fitTailParaFor2DModel/'

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
'rootfile1': 'test.root',
#'rootfile1': 'ggH125_2016MC.root',
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
'rootfile1': 'test.root',
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
'rootfile1': 'test.root',
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
'rootfile1': 'test.root',
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
'rootfile1': 'test.root',
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
'rootfile1': 'test.root',
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

