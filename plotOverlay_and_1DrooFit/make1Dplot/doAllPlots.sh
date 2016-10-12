counter=0
while [ $counter -le 8 ]
do
  
  cp paraConfigurations_DY_DY.py paraConfigurations.py
#  python makePlot_1D.py -t "mc_DY15_16_muPtErr_"${counter} 
#  python makePlot_1D.py -t "mc_DY16_genZ_recoZ_"${counter}
#  python makePlot_1D.py -t "mc_DY15_genZ_recoZ_"${counter}
#  python makePlot_1D.py -t "mc_DY15_muPt_gen_reco_"${counter}
#  python makePlot_1D.py -t "mc_DY16_muPt_gen_reco_"${counter}
#  python makePlot_1D.py -t "mc_DY15_16_muPt_leg1_"${counter}
#  python makePlot_1D.py -t "mc_DY15_16_muPt_leg2_"${counter}
#  python makePlot_1D.py -t "mc_DY15_v4_16_muPtErr_"${counter}
#  python makePlot_1D.py -t "mc_DY15_DY16_recoz_"${counter}
#  python makePlot_1D.py -t "mc_DY15_DY16_genz_"${counter}
#  python makePlot_1D.py -t "mc_DY15_genm2l_recoZ_"${counter}
#  python makePlot_1D.py -t "mc_DY15_genm2l_GENMZ_"${counter}
#  cp paraConfigurations_DY_H.py paraConfigurations.py
#  python makePlot_1D.py -t "mc_15_DY_H_muPtErr_"${counter}
#  python makePlot_1D.py -t "mc_16_DY_H_muPtErr_"${counter}
  python makePlot_1D.py -t "mc_DY15_genm2l_GENMZ_cutOnGEN_"${counter}

#  cp paraConfigurations_2D.py paraConfigurations.py
#  python makePlot_2D.py -t "mc_15_DY_pt_gen_reco_"${counter}
#  python makePlot_2D.py -t "mc_16_DY_pt_gen_reco_"${counter}
#  python makePlot_2D.py -t "mc_16_DY_mz_gen_reco_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_genm2l_recomz_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_massZ_GENMZ_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_genm2l_GENMZ_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_massZ_GENmass2l_diffBig_ptEta_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_pT_GENpT_"${counter}


#  cp paraConfigurations_DY_DY.py paraConfigurations.py 
#  python makePlot_1D_fit.py -t "mc_DY15_DY16_pullz_"${counter}

  counter=`expr $counter + 1`
done

#cp paraConfigurations_2D.py paraConfigurations.py
#python makePlot_2D.py -t "mc_15_DY_massZ_GENmass2l_diffBig_genpT1_genpT2"
#python makePlot_2D.py -t "mc_15_DY_massZ_GENmass2l_diffSmall_genpT1_genpT2"
#python makePlot_2D.py -t "mc_15_DY_massZ_GENmass2l_diffBig_pT1_pT2"
#python makePlot_2D.py -t "mc_15_DY_massZ_GENmass2l_diffSmall_pT1_pT2"
#python makePlot_2D.py -t "mc_15_DY_massZ_GENmass2l_diffBig_eta1_eta2"
#python makePlot_2D.py -t "mc_15_DY_massZ_GENmass2l_diffSmall_eta1_eta2"
#python makePlot_2D.py -t "mc_15_DY_pT_GENpT"
#python makePlot_2D.py -t "mc_15_DY_pT_GENpT_hasLeg1"
#python makePlot_2D.py -t "mc_15_DY_pT_GENpT_leg2_hasLeg1"
#python makePlot_2D.py -t "pull_vs_massZ_15MC"
#python makePlot_2D.py -t "pull_vs_GENmass2l_15MC"
#python makePlot_2D.py -t "mc_15_DY_pT_GENpT_leg2_oneLeg_in_pt10_40_eta0p0_0p9"
#python makePlot_2D.py -t "mc_15_DY_pT_eta_leg2_oneLeg_in_pt10_40_eta0p0_0p9"

#cp paraConfigurations_DY_DY.py paraConfigurations.py 
#python makePlot_1D_fit.py -t "mc_DY15_pullz"
#python makePlot_1D_fit.py -t "mc_DY15_pullz_hasLeg1"
#python makePlot_1D_fit.py -t "mc_DY15_pullz_noRECOfsr"
