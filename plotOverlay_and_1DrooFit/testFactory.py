from ROOT import *

w = RooWorkspace('w')
w.factory('Gaussian::f(x[-10,10],mean[5],sigma[3])')	
w.factory('BreitWigner::bw(x[0,100],mean[5],sigma[3])')
w.Print()
