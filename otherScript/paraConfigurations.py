paraConfigs = { }

savePath = '/home/mhl/public_html/2017/20170626_HZZefficiency/'

saveName = 'eff_ZZ4L_smallRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [200, 70, 500],
'vars1': ['GENmassZZ'],\
'vars2': ['GENmassZZ'], \
'cuts1': [' Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0 && passedFullSelection == 1'], \
'cuts2': [' Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0'], \
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'legend1': 'passedFullSelection 4mu events' ,
'legend2': 'all 4mu events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'eff_ZZ4L_tchan_smallRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_tchan_ext.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 90, 92],
'vars1': ['GENmassZZ'],\
'vars2': ['GENmassZZ'], \
'cuts1': [' Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0 && passedFullSelection == 1'], \
'cuts2': [' Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0'], \
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'legend1': 'passedFullSelection 4mu events' ,
'legend2': 'all 4mu events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'eff_ZZ4L_Z2AT4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2_20170627_v1.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2_20170627_v1.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [200, 70, 500],
'vars1': ['GENmassZZ'],\
'vars2': ['GENmassZZ'], \
'cuts1': [' Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0 && passedFullSelection == 1'], \
'cuts2': [' Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0'], \
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'legend1': 'passedFullSelection 4mu events' ,
'legend2': 'all 4mu events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'eff_ZZ4L_Z2AT4_midRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2_20170627_v1.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2_20170627_v1.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [2000, 70, 110],
'vars1': ['GENmassZZ'],\
'vars2': ['GENmassZZ'], \
'cuts1': [' Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0 && passedFullSelection == 1'], \
'cuts2': [' Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0'], \
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'legend1': 'passedFullSelection 4mu events' ,
'legend2': 'all 4mu events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}

saveName = 'eff_ggH125_smallRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'rootfile2': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 124, 126],
'vars1': ['GENmassZZ'],\
'vars2': ['GENmassZZ'], \
'cuts1': [' ( (Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0) || ( Sum$(abs(GENlep_id[])==11)>=4 &&  Sum$(abs(GENlep_id[])==15)==0 ) || (Sum$(abs(GENlep_id[])==11)>=2 && Sum$(abs(GENlep_id[])==13)>=2 && Sum$(abs(GENlep_id[])==15)==0) ) && passedFullSelection == 1'], \
'cuts2': ['( (Sum$(abs(GENlep_id[])==13)>=4 &&  Sum$(abs(GENlep_id[])==15)==0) || ( Sum$(abs(GENlep_id[])==11)>=4 &&  Sum$(abs(GENlep_id[])==15)==0 ) || (Sum$(abs(GENlep_id[])==11)>=2 && Sum$(abs(GENlep_id[])==13)>=2 && Sum$(abs(GENlep_id[])==15)==0) )  '], \
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'legend1': 'passedFullSelection 4mu events',
'legend2': 'all 4mu events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}

