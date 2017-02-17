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
#  python makePlot_1D.py -t "mc_DY15_genm2l_GENMZ_cutOnGEN_"${counter}

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

cp paraConfigurations_DY_DY.py paraConfigurations.py 

#python makePlot_1D.py -t "DY15_data_mc_pterr_e"
#python makePlot_1D.py -t "DY15_data_mc_pt_e"
#python makePlot_1D.py -t "mc_DY15_genm2l_recoZ_eta_0_0p9"
#python makePlot_1D.py -t "data15_2mu_relM2lErr"
#python makePlot_1D.py -t "DY_MC_genPt1_genPt2"
#python makePlot_1D.py -t "DY_MC_eta1_eta2"
#python makePlot_1D.py -t "dymc15_h15_pterr_test"
#python makePlot_1D.py -t "DYMC15_76corr_80corr_pterr_mu_pt_10_40_eta_0_0p9"
#python makePlot_1D.py -t "DYMC15_76corr_80corr_pterr_mu"
#python makePlot_1D.py -t "DYMC15_76corr_80corr_pt_mu"
#python makePlot_1D.py -t "data15_DYMC15_2mu_met"
#python makePlot_1D.py -t "DY15_MC_genLepPhi_bigRelErr_smallRelErr"
#python makePlot_1D.py -t "DY15_MC_genLepPhi_ifEtaSmallerThan0p9_bigRelErr_smallRelErr"
#python makePlot_1D.py -t "DY15_MC_genLepPhi_ifEtaSmallerThan0p5_bigRelErr_smallRelErr"
#python makePlot_1D.py -t "DY15_MC_genLepPhi_ifEtaSmallerThan0p2_bigRelErr_smallRelErr"

#python makePlot_1D.py -t "DY15_MC_genLepPhi_ifEtaSmallerThan0p1_bigRelErr_smallRelErr"
#python makePlot_1D.py -t "DY15_MC_genLepPhi_ifEtaSmallerThan0p1_bigRelErr_smallRelErr"
#python makePlot_1D.py -t "DY15_MC_genLepPhi_bigRelErr_smallRelErr_eta_0p1_0p8"
#python makePlot_1D.py -t "DY15_MC_genLepPhi_bigRelErr_smallRelErr_eta_1p3_1p5"

#python makePlot_1D.py -t "DY_2015_massZErr_2mu"
#python makePlot_1D.py -t "DY_2015_massZErr_2e"

#python makePlot_1D.py -t "DY_2015_relmZErr_2e"
#python makePlot_1D.py -t "DY15_MC_relMassZErr_e"
#python makePlot_1D.py -t "DY15_MC_relMassZErr_e"
#python makePlot_1D_fit.py -t "mc_DY15_pullz"
#python makePlot_1D_fit.py -t "mc_DY15_pullz_hasLeg1"
#python makePlot_1D_fit.py -t "mc_DY15_pullz_noRECOfsr"
#python makePlot_1D.py -t "DY15_MC_massZErr"
#python makePlot_1D.py -t "DY15_MC_GENZM_recoZcut_80_100"
#python makePlot_1D.py -t "DY15_MC_GENZM_recoZcut_70_110"
#python makePlot_1D.py -t "DY15_MC_GENZM_recoZcut_60_120"

#python makePlot_1D.py -t "DY_2015_pTErr_eta_0_0p8_e"
#python makePlot_1D.py -t "DY_2015_relpTErr_eta_0_0p8_e"
#python makePlot_1D.py -t "DY_2015_eta_eta_1p57_2p5_diffrelPtErr_e"
#python makePlot_1D.py -t "DY_2015_eta_eta_0p8_1p44_diffrelPtErr_e"
#python makePlot_1D.py -t "DY_2015_eta_eta_0_0p8_diffrelPtErr_e"
#python makePlot_1D.py -t "DY_2015_relPtErr_2e"
#python makePlot_1D.py -t "DY_2015_eta_eta_2_2p5_diffrelPtErr_e"

#python makePlot_1D.py -t "DY_2015_2e_ecalDriven"
#python makePlot_1D.py -t "DY_2015_ecalDriven_2e"
#python makePlot_1D.py -t "DY_2015_massZErr_ifRelMassZErrBigger0p03_2e"


cp paraConfigurations_H.py paraConfigurations.py
#python makePlot_1D.py -t "H15_MC_mass4lErr_2e2mu"
#python makePlot_1D.py -t "H15_MC_mass4lErr_4mu"
#python makePlot_1D.py -t "H15_MC_relmass4lErr_4e"
#python makePlot_1D.py -t "H15_MC_relmass4lErr_4mu"
#python makePlot_1D.py -t "H15_MC_relmass4lErr_2e2mu"
#python makePlot_1D.py -t "H15_MC_relmass4lErr_4e_uncorr_corr"
#python makePlot_1D.py -t "DY15_H_mass4l_all_compare_relM4lBigger0p005"
#python makePlot_1D.py -t "DY15_H_mz1_mz1refit_newPara"
#python makePlot_1D.py -t "DY15_H_mz1_mz1refit_bw"
#python makePlot_1D.py -t "DY15_H_genmz1_mz1"
#python makePlot_1D.py -t "H_relM4lErr_old_new_4e"
#python makePlot_1D.py -t "H_relM4lErrREFIT_old_new_2e2mu"
#python makePlot_1D.py -t "DY15_H_mz1_mz1refit_test"
#python makePlot_1D.py -t "DY15_H_mz1_mz1refit_bw"
#python makePlot_1D.py -t "DY15_H_genmz1_mz1refit_newPara"
#python makePlot_1D.py -t "DY15_H_genmz1_mz1refit_test"
#python makePlot_1D.py -t "DY15_H_genmz1_mz1refit_kinZfiterPDF"
#python makePlot_1D.py -t "DY15_H_mz1_mz1refit_ifmz1recoBigger91p2"

#python makePlot_1D.py -t "DY15_H_mz1reco_mz1refit_pdfInPackage"

#python makePlot_1D.py -t "DY15_H_m4lreco_m4lrefit_pdfInPackage"

#python makePlot_1D.py -t "DY15_H_etaL1_patch2_3"
#python makePlot_1D.py -t "DY15_H_etaL2_patch2_3"
#python makePlot_1D.py -t "DY15_H_pTL1_patch2_3"
#python makePlot_1D.py -t "DY15_H_pTL2_patch2_3"
#python makePlot_1D.py -t "DY15_H_pTErrL1_patch2_3"
#python makePlot_1D.py -t "DY15_H_massZ1reco_patch2_3"
#python makePlot_1D.py -t "DY15_H_massZ1refit_patch2_3"
#python makePlot_1D.py -t "DY15_H_pTErrL2_patch2_3"

#python makePlot_1D.py -t "H_m4lErr_reco_refit_4mu"
#python makePlot_1D.py -t "H_m4lErr_refit_4mu_minos_hesse"
#python makePlot_1D.py -t "H_m4lErr_reco_refit_4mu_hesse"

#python makePlot_1D.py -t "H_m4lErr_refit_4mu_minos_average_sqrtSum"
#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015"

#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015_4mu"
#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015_4e"
#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015_2e2mu"
#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015_2mu2e"

#python makePlot_1D.py -t "H_GENmz1_13tev_2015_2016_4mu"
#python makePlot_1D.py -t "H_GENmz1_13tev_2015_2016_4e"
#python makePlot_1D.py -t "H_GENmz1_13tev_2015_2016_2e2mu"
#python makePlot_1D.py -t "H_GENmz1_13tev_2015_2016_2mu2e"

#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015_2e2mu_useGENZ_mass"
#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015_2mu2e_useGENZ_mass"
#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015_4e_useGENZ_mass"
#python makePlot_1D.py -t "H_GENmz1_8tev_13tev_2015_4mu_useGENZ_mass"

#python makePlot_1D.py -t "H_LepErr_2e2mu"
#python makePlot_1D.py -t "H_massZErr_2e2mu"
#python makePlot_1D.py -t "H_massZErr_2mu2e"
#python makePlot_1D.py -t "H_massZErr_4mu"
#python makePlot_1D.py -t "H_massZErr_4e"
#python makePlot_1D.py -t "H_lepErr_ratio"

#python makePlot_1D.py -t "H_m4l_reco_refit_4mu"
#python makePlot_1D.py -t "H_m4l_reco_refit_4e"
#python makePlot_1D.py -t "H_m4l_reco_refit_2e2mu"
#python makePlot_1D.py -t "H_m4l_reco_refit_2mu2e"

#python makePlot_1D.py -t "mz1_124_125_4mu"
#python makePlot_1D.py -t "mz1_124_125_4e"
#python makePlot_1D.py -t "mz1_124_125_2e2mu"
#python makePlot_1D.py -t "mz1_124_125_2mu2e"

#python makePlot_1D.py -t "mz1_126_125_4mu"
#python makePlot_1D.py -t "mz1_126_125_4e"
#python makePlot_1D.py -t "mz1_126_125_2e2mu"
#python makePlot_1D.py -t "mz1_126_125_2mu2e"
python makePlot_1D.py -t "H16_MC_relmass4lErr_4e"
