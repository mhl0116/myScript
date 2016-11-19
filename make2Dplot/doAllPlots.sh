counter=0
while [ $counter -le 8 ]
do
  
#  cp paraConfigurations_DY_DY.py paraConfigurations.py
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
#  python makePlot_1D.py -t "mc_DY15_genm2l_GENMZ_cutOnGEN_"${counter}

  cp paraConfigurations_2D.py paraConfigurations.py
#  python makePlot_2D.py -t "mc_15_DY_pt_gen_reco_"${counter}
#  python makePlot_2D.py -t "mc_16_DY_pt_gen_reco_"${counter}
#  python makePlot_2D.py -t "mc_16_DY_mz_gen_reco_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_genm2l_recomz_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_massZ_GENMZ_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_genm2l_GENMZ_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_massZ_GENmass2l_diffBig_ptEta_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_pT_GENpT_"${counter}
#  python makePlot_2D.py -t "mc_15_DY_pT_GENpT_cutOnGEN_"${counter}


#  cp paraConfigurations_DY_DY.py paraConfigurations.py 
#  python makePlot_1D_fit.py -t "mc_DY15_DY16_pullz_"${counter}

  counter=`expr $counter + 1`
done

cp paraConfigurations_2D.py paraConfigurations.py
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_eta_vs_GENmass2l"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l_genzm_88_94"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENMZ_genzm_88_94"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_eta_vs_GENmass2l_otherGENMu_pT_44_46"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_eta_vs_GENmass2l_otherGENMu_pT_40_42"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_eta_vs_GENmass2l_otherGENMu_pT_50_52"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l_otherGENMu_eta_0_0p1"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l_otherGENMu_eta_0p9_1p1"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_plot_otherGENMu_pT_vs_GENmass2l_otherGENMu_eta_2p1_2p4"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_GENmass2l_90_92_plotOtherGENMu_pT_eta"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_GENmass2l_85_87_plotOtherGENMu_pT_eta"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_GENmass2l_95_97_plotOtherGENMu_pT_eta"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_GENmass2l_95_100_plotOtherGENMu_pT_eta"
#python makePlot_2D.py -t "fixOneGENMu_pT_40_50_0_0p9_GENmass2l_80_87_plotOtherGENMu_pT_eta"

#python makePlot_2D.py -t "DY15_MC_leadGENpT_subGENpT"
#python makePlot_2D.py -t "DY15_MC_leadGENpT_eta"
#python makePlot_2D.py -t "DY15_MC_subleadGENpT_eta"
#python makePlot_2D.py -t "DY15_MC_GENpT1_GENpT2"
#python makePlot_2D.py -t "DY15_MC_GENpT1_GENpT2_eta_0"
#python makePlot_2D.py -t "DY15_MC_phi1_phi2_eta_0"

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

#python makePlot_2D.py -t "DY15_MC_pTErr_eta"
#python makePlot_2D.py -t "DY15_MC_pTErr_phi"
#python makePlot_2D.py -t "DY15_MC_pTErr_GENpT"
#python makePlot_2D.py -t "DY15_MC_pTErr_RECOpT"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_phi"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_eta"
#python makePlot_2D.py -t "DY15_MC_relpTErrRECO_phi"
#python makePlot_2D.py -t "DY15_MC_relpTErrRECO_eta"

#python makePlot_2D.py -t "mc_15_DY_pT_GENpT_leg2_hasLeg1_cutOnGEN"

#python makePlot_2D.py -t "DY15_MC_pTErr_GENpT_eta_0.0_0.9"
##python makePlot_2D.py -t "DY15_MC_pTErr_GENpT_eta_0.9_1.2"
#python makePlot_2D.py -t "DY15_MC_pTErr_GENpT_eta_0.9_1.8"
#python makePlot_2D.py -t "DY15_MC_pTErr_GENpT_eta_1.8_2.4"


#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_eta_pTSmallerThan60"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_eta_pTSmallerThan50"

#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_phi_eta_0p0_0p1"
#python makePlot_2D.py -t "DY16_MC_relpTErrRECO_eta"
#python makePlot_2D.py -t "DY16_data_relpTErrRECO_eta"

#python makePlot_2D.py -t "DY15_MC_eta_phi_relpTErrGENBiggerThan0.02_eta_0p0_0p1"
#python makePlot_2D.py -t "DY15_MC_eta1_eta2_relpTErrGENBiggerThan0.02_eta1_0p0_0p1"

#python makePlot_2D.py -t "DY15_MC_pTResidual_eta"
#python makePlot_2D.py -t "DY15_MC_pTResidual_phi"
#python makePlot_2D.py -t "DY15_MC_pTPull_eta"
#python makePlot_2D.py -t "DY15_MC_pTPull_phi"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_eta_phiBiggerThan0"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_eta_phi_minus_0p8_minus_0p9"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_eta_residual_0_0p01"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_eta_residual_0_0p01_pull_0_1"


#python makePlot_2D.py -t "DY15_MC_eta_phi_eta_0_0p9_relpTErr_big_0p02"
#python makePlot_2D.py -t "DY15_MC_eta_phi_eta_0p9_1p8_relpTErr_big_0p03"

#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_phi_eta_0_0p9"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_phi_eta_0p9_1p8"
#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_phi_eta_1p8_2p4"

#python makePlot_2D.py -t "DY15_MC_relpTErr_GENpT_eta_0_0p9"
#python makePlot_2D.py -t "DY15_MC_relpTErr_GENpT_eta_0p9_1p8"
#python makePlot_2D.py -t "DY15_MC_relpTErr_GENpT_eta_1p8_2p4"

#python makePlot_2D.py -t "DY15_MC_relpTErr_GENpT_eta_0_0p5_e"
#python makePlot_2D.py -t "DY15_MC_relpTErr_GENpT_eta_0p7_1_e"
#python makePlot_2D.py -t "DY15_MC_relpTErr_GENpT_eta_1_1p5_e"
#python makePlot_2D.py -t "DY15_MC_relpTErr_GENpT_eta_1p5_2_e"
#python makePlot_2D.py -t "DY15_MC_relpTErr_GENpT_eta_2_2p5_e"

#python makePlot_2D.py -t "DY15_MC_eta1_eta2_relmasszErr_0p007_0p008"
#python makePlot_2D.py -t "H15_MC_eta3_eta4_mass4lErr_0p6_0p9_4mu"
#python makePlot_2D.py -t "H15_MC_eta1_eta2_mass4lErr_0p6_0p9_4mu"

#python makePlot_2D.py -t "H15_MC_pT3_pT4_mass4lErr_0p6_0p9_4mu"
#python makePlot_2D.py -t "H15_MC_pT1_pT2_mass4lErr_0p6_0p9_4mu"

#python makePlot_2D.py -t "DY15_eta1_eta2_relMassErr_biggerThan_0p009"
#python makePlot_2D.py -t "DY15_eta1_eta2_relMassErr_smallerThan_0p009"

#python makePlot_2D.py -t "DY15_MC_relpTErrGEN_eta_e"
#python makePlot_2D.py -t "DY15_MC_pTErr_GENpT_e"

#python makePlot_2D.py -t "H15_MC_pT1_eta1_m4muErr_0p74_0p88"
#python makePlot_2D.py -t "H15_MC_pT2_eta2_m4muErr_0p74_0p88"
#python makePlot_2D.py -t "H15_MC_pT3_eta3_m4muErr_0p74_0p88"
#python makePlot_2D.py -t "H15_MC_pT4_eta4_m4muErr_0p74_0p88"
#python makePlot_2D.py -t "H15_MC_pT1_eta1_m4muErr_1p16_1p3"
#python makePlot_2D.py -t "H15_MC_pT2_eta2_m4muErr_1p16_1p3"
#python makePlot_2D.py -t "H15_MC_pT3_eta3_m4muErr_1p16_1p3"
#python makePlot_2D.py -t "H15_MC_pT4_eta4_m4muErr_1p16_1p3"

#python makePlot_2D.py -t "DY15_massZErr_relmassZErr"
#python makePlot_2D.py -t "massZ_genmz_CutmassZ_not_80_100"

#python makePlot_2D.py -t "H15_MC_relM4lErr_relM4lErrREFIT_0_0p005"

#python makePlot_2D.py -t "H15_MC_pT1_eta1_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT2_eta2_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT3_eta3_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT4_eta4_relM4lErrREFIT_0_0p005"

#python makePlot_2D.py -t "H15_MC_pT1_relpTErr1_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT1_pTErr1_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT2_relpTErr2_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT2_pTErr2_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT3_relpTErr3_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT3_pTErr3_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT4_relpTErr4_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_MC_pT4_pTErr4_relM4lErrREFIT_0_0p005"

#python makePlot_2D.py -t "H15_m4l_m4lREFIT_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_m4lErr_m4lErrREFIT_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_m4lErr_m4lErrREFIT_relM4lErrREFIT_biggerThan0p005"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_biggerThan0p005"

#python makePlot_2D.py -t "H15_pT4_pT4subtract2timespT4Err_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_pT4_pT4subtract2timespT4Err_relM4lErrREFIT_biggerThan0p005"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_biggerThan0p005"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_alleta_0_0p9"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_removeCorr"

#python makePlot_2D.py -t "mz1_m4lREFIT_lowRange"
#python makePlot_2D.py -t "H15_MC_pT1_eta1_middleBlock_alleta_0_0p9"
#python makePlot_2D.py -t "H15_MC_pT2_eta2_middleBlock_alleta_0_0p9"
#python makePlot_2D.py -t "H15_MC_pT3_eta3_middleBlock_alleta_0_0p9"
#python makePlot_2D.py -t "H15_MC_pT4_eta4_middleBlock_alleta_0_0p9"
#python makePlot_2D.py -t "H15_MC_pT1_relpTErr1_middleBlock_alleta_0_0p9"
#python makePlot_2D.py -t "H15_MC_pT2_relpTErr2_middleBlock_alleta_0_0p9"
#python makePlot_2D.py -t "H15_MC_pT3_relpTErr3_middleBlock_alleta_0_0p9"
#python makePlot_2D.py -t "H15_MC_pT4_relpTErr4_middleBlock_alleta_0_0p9"

#python makePlot_2D.py -t "H15_pT1_pT2_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "H15_eta1_eta2_relM4lErrREFIT_0_0p005"
#python makePlot_2D.py -t "diffrelM4lErr_correlation"


#python makePlot_2D.py -t "pTErr1_pTErr2_lowRange"
#python makePlot_2D.py -t "pT1_pT2_lowRange"
#python makePlot_2D.py -t "pTErrREFIT1_pTErrREFIT2_lowRange"
#python makePlot_2D.py -t "pTErr1_pTErr2_middleRange"
#python makePlot_2D.py -t "pT1_pT2_lowRange"
#python makePlot_2D.py -t "pTErrREFIT1_pTErrREFIT2_middleRange"

#python makePlot_2D.py -t "pTErr1_pTErrREFIT1_middleRange"
#python makePlot_2D.py -t "pTErr2_pTErrREFIT2_middleRange"
#python makePlot_2D.py -t "pTErr1_pTErrREFIT1_lowRange"
#python makePlot_2D.py -t "pTErr2_pTErrREFIT2_lowRange"


#python makePlot_2D.py -t "H15_diffM4lErr_diffMZ1"
#python makePlot_2D.py -t "massZ1_massZ1REFIT_test"
#python makePlot_2D.py -t "massZ1_massZ1REFIT_test_3gauss_full"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_test_3gauss"
#python makePlot_2D.py -t "H15_m4lErr_m4lErrREFIT_fullRange_test"
#python makePlot_2D.py -t "GENmassZ1_massZ1"
#python makePlot_2D.py -t "massZ1_massZ1REFIT_pdfKinZFitter"
#python makePlot_2D.py -t "massZ1_massZ1REFIT_bw"
#python makePlot_2D.py -t "massZ1_massZ1REFIT_pdfKinZFitter_ichepNtuple"
#python makePlot_2D.py -t "massZ1_massZ1REFIT_upRange"
#python makePlot_2D.py -t "massZ1_massZ1REFIT_middleRange"
#python makePlot_2D.py -t "massZ1_massZ1REFIT_lowRange"
#python makePlot_2D.py -t "eta1_eta2_lowRange"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_norefittedMZ191p2"

#python makePlot_2D.py -t "pT1_pT2_lowRange"
#python makePlot_2D.py -t "pT1_pT2_middleRange"

#python makePlot_2D.py -t "pT1REFIT_pT2REFIT_lowRange"
#python makePlot_2D.py -t "pT1REFIT_pT2REFIT_middleRange"

#python makePlot_2D.py -t "pT1_pT1REFIT_lowRange"
#python makePlot_2D.py -t "pT1_pT1REFIT_middleRange"
#python makePlot_2D.py -t "pT2_pT2REFIT_lowRange"
#python makePlot_2D.py -t "pT2_pT2REFIT_middleRange"

#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_norecoMZ191p2"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_onlyrefittedMZ191p2"

#python makePlot_2D.py -t "H15_diffM4lErr_MZ1_test"
#python makePlot_2D.py -t "H15_diffM4lErr_MZ1_bw"
#python makePlot_2D.py -t "H15_diffM4lErr_MZ1_newPara_3gauss"
#python makePlot_2D.py -t "H15_diffM4lErr_MZ1_newPara_3gauss_minos_sqrtSum"
#python makePlot_2D.py -t "H15_relm4lErr_relm4lErrREFIT_relM4lErrREFIT_fullRange_minosAsym_sqrtSum"

#python makePlot_2D.py -t "H15_errUpDnDiff_mZ1_4mu"

#python makePlot_2D.py -t "H15_genPt_refitpT_4mu"
#python makePlot_2D.py -t "H15_genPt_recopT_4mu"
#python makePlot_2D.py -t "H15_recoPt_refitpT_4mu"

python makePlot_2D.py -t "H15_GENZ_mass_0_1"
