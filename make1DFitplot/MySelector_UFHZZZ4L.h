//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Oct 25 10:47:23 2016 by ROOT version 6.02/13
// from TTree passedEvents/passedEvents
// found on file: /cms/data/store/user/t2/users/mhl/ggH_2015MC_mH125.root
//////////////////////////////////////////////////////////

#ifndef MySelector_UFHZZZ4L_h
#define MySelector_UFHZZZ4L_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>

// Header file for the classes stored in the TTree if any.
#include "string"
#include "vector"
#include "vector"
#include "vector"
#include "vector"

class MySelector_UFHZZZ4L : public TSelector {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   ULong64_t       Run;
   ULong64_t       Event;
   ULong64_t       LumiSect;
   Int_t           nVtx;
   Int_t           nInt;
   Int_t           finalState;
   string          *triggersPassed;
   Bool_t          passedTrig;
   Bool_t          passedFullSelection;
   Bool_t          passedZ4lSelection;
   Bool_t          passedQCDcut;
   Bool_t          passedZ1LSelection;
   Bool_t          passedZ4lZXCRSelection;
   Bool_t          passedZXCRSelection;
   Int_t           nZXCRFailedLeptons;
   Float_t         genWeight;
   Float_t         k_ggZZ;
   Float_t         k_qqZZ_qcd_dPhi;
   Float_t         k_qqZZ_qcd_M;
   Float_t         k_qqZZ_qcd_Pt;
   Float_t         k_qqZZ_ewk;
   vector<float>   *pdfWeights;
   vector<int>     *pdfWeightIDs;
   Float_t         pdfRMSup;
   Float_t         pdfRMSdown;
   Float_t         pdfENVup;
   Float_t         pdfENVdown;
   Float_t         pileupWeight;
   Float_t         dataMCWeight;
   Float_t         eventWeight;
   Float_t         crossSection;
   vector<int>     *lep_id;
   vector<float>   *lep_pt;
   vector<float>   *lep_pterr;
   vector<float>   *lep_pterrold;
   vector<float>   *lep_eta;
   vector<float>   *lep_phi;
   vector<float>   *lep_mass;
   vector<float>   *lepFSR_pt;
   vector<float>   *lepFSR_eta;
   vector<float>   *lepFSR_phi;
   vector<float>   *lepFSR_mass;
   Int_t           lep_Hindex[4];
   vector<int>     *lep_genindex;
   vector<int>     *lep_missingHits;
   vector<float>   *lep_mva;
   vector<int>     *lep_ecalDriven;
   vector<int>     *lep_tightId;
   vector<int>     *lep_tightIdSUS;
   vector<int>     *lep_tightIdHiPt;
   vector<float>   *lep_Sip;
   vector<float>   *lep_IP;
   vector<float>   *lep_isoNH;
   vector<float>   *lep_isoCH;
   vector<float>   *lep_isoPhot;
   vector<float>   *lep_isoPU;
   vector<float>   *lep_isoPUcorr;
   vector<float>   *lep_RelIso;
   vector<float>   *lep_RelIsoNoFSR;
   vector<float>   *lep_MiniIso;
   vector<float>   *lep_ptRatio;
   vector<float>   *lep_ptRel;
   vector<string>  *lep_filtersMatched;
   vector<float>   *lep_dataMC;
   vector<float>   *lep_dataMCErr;
   Int_t           nisoleptons;
   Float_t         muRho;
   Float_t         elRho;
   Float_t         pTL1;
   Float_t         pTL2;
   Float_t         pTL3;
   Float_t         pTL4;
   Int_t           idL1;
   Int_t           idL2;
   Int_t           idL3;
   Int_t           idL4;
   Float_t         etaL1;
   Float_t         etaL2;
   Float_t         etaL3;
   Float_t         etaL4;
   Float_t         pTL1FSR;
   Float_t         pTL2FSR;
   Float_t         pTL3FSR;
   Float_t         pTL4FSR;
   vector<int>     *tau_id;
   vector<float>   *tau_pt;
   vector<float>   *tau_eta;
   vector<float>   *tau_phi;
   vector<float>   *tau_mass;
   vector<float>   *H_pt;
   vector<float>   *H_eta;
   vector<float>   *H_phi;
   vector<float>   *H_mass;
   vector<float>   *H_noFSR_pt;
   vector<float>   *H_noFSR_eta;
   vector<float>   *H_noFSR_phi;
   vector<float>   *H_noFSR_mass;
   Float_t         mass4l;
   Float_t         mass4l_noFSR;
   Float_t         mass4lErr;
   Float_t         mass4lREFIT;
   Float_t         mass4lErrREFIT;
   Float_t         massZ1REFIT;
   Float_t         massZ1Err;
   Float_t         mass4mu;
   Float_t         mass4e;
   Float_t         mass2e2mu;
   Float_t         pT4l;
   Float_t         eta4l;
   Float_t         phi4l;
   Float_t         rapidity4l;
   Float_t         cosTheta1;
   Float_t         cosTheta2;
   Float_t         cosThetaStar;
   Float_t         Phi;
   Float_t         Phi1;
   Float_t         mass3l;
   vector<float>   *Z_pt;
   vector<float>   *Z_eta;
   vector<float>   *Z_phi;
   vector<float>   *Z_mass;
   vector<float>   *Z_noFSR_pt;
   vector<float>   *Z_noFSR_eta;
   vector<float>   *Z_noFSR_phi;
   vector<float>   *Z_noFSR_mass;
   Int_t           Z_Hindex[2];
   Float_t         massZ1;
   Float_t         massZ2;
   Float_t         pTZ1;
   Float_t         pTZ2;
   Float_t         met;
   Float_t         met_phi;
   Float_t         met_jesup;
   Float_t         met_phi_jesup;
   Float_t         met_jesdn;
   Float_t         met_phi_jesdn;
   Float_t         met_uncenup;
   Float_t         met_phi_uncenup;
   Float_t         met_uncendn;
   Float_t         met_phi_uncendn;
   vector<int>     *jet_iscleanH4l;
   vector<float>   *jet_pt;
   vector<float>   *jet_relpterr;
   vector<float>   *jet_eta;
   vector<float>   *jet_phi;
   vector<float>   *jet_phierr;
   vector<float>   *jet_mass;
   vector<int>     *jet_jesup_iscleanH4l;
   vector<float>   *jet_jesup_pt;
   vector<float>   *jet_jesup_eta;
   vector<float>   *jet_jesup_phi;
   vector<float>   *jet_jesup_mass;
   vector<int>     *jet_jesdn_iscleanH4l;
   vector<float>   *jet_jesdn_pt;
   vector<float>   *jet_jesdn_eta;
   vector<float>   *jet_jesdn_phi;
   vector<float>   *jet_jesdn_mass;
   vector<int>     *jet_jerup_iscleanH4l;
   vector<float>   *jet_jerup_pt;
   vector<float>   *jet_jerup_eta;
   vector<float>   *jet_jerup_phi;
   vector<float>   *jet_jerup_mass;
   vector<int>     *jet_jerdn_iscleanH4l;
   vector<float>   *jet_jerdn_pt;
   vector<float>   *jet_jerdn_eta;
   vector<float>   *jet_jerdn_phi;
   vector<float>   *jet_jerdn_mass;
   vector<float>   *jet_pumva;
   vector<float>   *jet_csvv2;
   vector<int>     *jet_isbtag;
   vector<int>     *jet_hadronFlavour;
   vector<int>     *jet_partonFlavour;
   vector<float>   *jet_QGTagger;
   vector<float>   *jet_axis2;
   vector<float>   *jet_ptD;
   vector<int>     *jet_mult;
   Int_t           njets_pt30_eta4p7;
   Int_t           njets_pt30_eta4p7_jesup;
   Int_t           njets_pt30_eta4p7_jesdn;
   Int_t           njets_pt30_eta4p7_jerup;
   Int_t           njets_pt30_eta4p7_jerdn;
   Int_t           nbjets_pt30_eta4p7;
   Int_t           nvjets_pt40_eta2p4;
   Float_t         pt_leadingjet_pt30_eta4p7;
   Float_t         pt_leadingjet_pt30_eta4p7_jesup;
   Float_t         pt_leadingjet_pt30_eta4p7_jesdn;
   Float_t         pt_leadingjet_pt30_eta4p7_jerup;
   Float_t         pt_leadingjet_pt30_eta4p7_jerdn;
   Float_t         absrapidity_leadingjet_pt30_eta4p7;
   Float_t         absrapidity_leadingjet_pt30_eta4p7_jesup;
   Float_t         absrapidity_leadingjet_pt30_eta4p7_jesdn;
   Float_t         absrapidity_leadingjet_pt30_eta4p7_jerup;
   Float_t         absrapidity_leadingjet_pt30_eta4p7_jerdn;
   Float_t         absdeltarapidity_hleadingjet_pt30_eta4p7;
   Float_t         absdeltarapidity_hleadingjet_pt30_eta4p7_jesup;
   Float_t         absdeltarapidity_hleadingjet_pt30_eta4p7_jesdn;
   Float_t         absdeltarapidity_hleadingjet_pt30_eta4p7_jerup;
   Float_t         absdeltarapidity_hleadingjet_pt30_eta4p7_jerdn;
   Float_t         DijetMass;
   Float_t         DijetDEta;
   Float_t         DijetFisher;
   vector<int>     *mergedjet_iscleanH4l;
   vector<float>   *mergedjet_pt;
   vector<float>   *mergedjet_eta;
   vector<float>   *mergedjet_phi;
   vector<float>   *mergedjet_mass;
   vector<float>   *mergedjet_tau1;
   vector<float>   *mergedjet_tau2;
   vector<float>   *mergedjet_L1;
   vector<float>   *mergedjet_softdropmass;
   vector<float>   *mergedjet_prunedmass;
   vector<int>     *mergedjet_nsubjet;
   vector<vector<float> > *mergedjet_subjet_pt;
   vector<vector<float> > *mergedjet_subjet_eta;
   vector<vector<float> > *mergedjet_subjet_phi;
   vector<vector<float> > *mergedjet_subjet_mass;
   vector<vector<float> > *mergedjet_subjet_btag;
   Int_t           nFSRPhotons;
   vector<float>   *allfsrPhotons_dR;
   vector<float>   *allfsrPhotons_iso;
   vector<float>   *allfsrPhotons_pt;
   vector<int>     *fsrPhotons_lepindex;
   vector<float>   *fsrPhotons_pt;
   vector<float>   *fsrPhotons_pterr;
   vector<float>   *fsrPhotons_eta;
   vector<float>   *fsrPhotons_phi;
   vector<float>   *fsrPhotons_dR;
   vector<float>   *fsrPhotons_iso;
   Float_t         theta12;
   Float_t         theta13;
   Float_t         theta14;
   Float_t         minM3l;
   Float_t         Z4lmaxP;
   Float_t         minDeltR;
   Float_t         m3l_soft;
   Float_t         minMass2Lep;
   Float_t         maxMass2Lep;
   Float_t         thetaPhoton;
   Float_t         thetaPhotonZ;
   Int_t           EventCat;
   Int_t           GENfinalState;
   Bool_t          passedFiducialSelection;
   vector<float>   *GENlep_pt;
   vector<float>   *GENlep_eta;
   vector<float>   *GENlep_phi;
   vector<float>   *GENlep_mass;
   vector<int>     *GENlep_id;
   vector<int>     *GENlep_status;
   vector<int>     *GENlep_MomId;
   vector<int>     *GENlep_MomMomId;
   Int_t           GENlep_Hindex[4];
   vector<float>   *GENlep_isoCH;
   vector<float>   *GENlep_isoNH;
   vector<float>   *GENlep_isoPhot;
   vector<float>   *GENlep_RelIso;
   vector<float>   *GENH_pt;
   vector<float>   *GENH_eta;
   vector<float>   *GENH_phi;
   vector<float>   *GENH_mass;
   Float_t         GENmass4l;
   Float_t         GENmass4mu;
   Float_t         GENmass4e;
   Float_t         GENmass2e2mu;
   Float_t         GENpT4l;
   Float_t         GENeta4l;
   Float_t         GENrapidity4l;
   Float_t         GENcosTheta1;
   Float_t         GENcosTheta2;
   Float_t         GENcosThetaStar;
   Float_t         GENPhi;
   Float_t         GENPhi1;
   Float_t         GENMH;
   vector<float>   *GENZ_pt;
   vector<float>   *GENZ_eta;
   vector<float>   *GENZ_phi;
   vector<float>   *GENZ_mass;
   vector<int>     *GENZ_DaughtersId;
   vector<int>     *GENZ_MomId;
   Float_t         GENmassZ1;
   Float_t         GENmassZ2;
   Float_t         GENpTZ1;
   Float_t         GENpTZ2;
   Float_t         GENdPhiZZ;
   Float_t         GENmassZZ;
   Float_t         GENpTZZ;
   Float_t         GENHmass;
   vector<float>   *GENjet_pt;
   vector<float>   *GENjet_eta;
   vector<float>   *GENjet_phi;
   vector<float>   *GENjet_mass;
   Int_t           GENnjets_pt30_eta4p7;
   Float_t         GENpt_leadingjet_pt30_eta4p7;
   Float_t         GENabsrapidity_leadingjet_pt30_eta4p7;
   Float_t         GENabsdeltarapidity_hleadingjet_pt30_eta4p7;
   Int_t           lheNj;
   Int_t           lheNb;
   Int_t           nGenStatus2bHad;
   Double_t        me_0plus_JHU;
   Double_t        me_qqZZ_MCFM;
   Double_t        p0plus_m4l;
   Double_t        bkg_m4l;
   Double_t        D_bkg_kin;
   Double_t        D_bkg;
   Double_t        Dgg10_VAMCFM;
   Double_t        Djet_VAJHU;
   Double_t        Djet_VAJHU_jesup;
   Double_t        Djet_VAJHU_jesdn;
   Double_t        D_g4;

   // List of branches
   TBranch        *b_Run;   //!
   TBranch        *b_Event;   //!
   TBranch        *b_LumiSect;   //!
   TBranch        *b_nVtx;   //!
   TBranch        *b_nInt;   //!
   TBranch        *b_finalState;   //!
   TBranch        *b_triggersPassed;   //!
   TBranch        *b_passedTrig;   //!
   TBranch        *b_passedFullSelection;   //!
   TBranch        *b_passedZ4lSelection;   //!
   TBranch        *b_passedQCDcut;   //!
   TBranch        *b_passedZ1LSelection;   //!
   TBranch        *b_passedZ4lZXCRSelection;   //!
   TBranch        *b_passedZXCRSelection;   //!
   TBranch        *b_nZXCRFailedLeptons;   //!
   TBranch        *b_genWeight;   //!
   TBranch        *b_k_ggZZ;   //!
   TBranch        *b_k_qqZZ_qcd_dPhi;   //!
   TBranch        *b_k_qqZZ_qcd_M;   //!
   TBranch        *b_k_qqZZ_qcd_Pt;   //!
   TBranch        *b_k_qqZZ_ewk;   //!
   TBranch        *b_pdfWeights;   //!
   TBranch        *b_pdfWeightIDs;   //!
   TBranch        *b_pdfRMSup;   //!
   TBranch        *b_pdfRMSdown;   //!
   TBranch        *b_pdfENVup;   //!
   TBranch        *b_pdfENVdown;   //!
   TBranch        *b_pileupWeight;   //!
   TBranch        *b_dataMCWeight;   //!
   TBranch        *b_eventWeight;   //!
   TBranch        *b_crossSection;   //!
   TBranch        *b_lep_id;   //!
   TBranch        *b_lep_pt;   //!
   TBranch        *b_lep_pterr;   //!
   TBranch        *b_lep_pterrold;   //!
   TBranch        *b_lep_eta;   //!
   TBranch        *b_lep_phi;   //!
   TBranch        *b_lep_mass;   //!
   TBranch        *b_lepFSR_pt;   //!
   TBranch        *b_lepFSR_eta;   //!
   TBranch        *b_lepFSR_phi;   //!
   TBranch        *b_lepFSR_mass;   //!
   TBranch        *b_lep_Hindex;   //!
   TBranch        *b_lep_genindex;   //!
   TBranch        *b_lep_missingHits;   //!
   TBranch        *b_lep_mva;   //!
   TBranch        *b_lep_ecalDriven;   //!
   TBranch        *b_lep_tightId;   //!
   TBranch        *b_lep_tightIdSUS;   //!
   TBranch        *b_lep_tightIdHiPt;   //!
   TBranch        *b_lep_Sip;   //!
   TBranch        *b_lep_IP;   //!
   TBranch        *b_lep_isoNH;   //!
   TBranch        *b_lep_isoCH;   //!
   TBranch        *b_lep_isoPhot;   //!
   TBranch        *b_lep_isoPU;   //!
   TBranch        *b_lep_isoPUcorr;   //!
   TBranch        *b_lep_RelIso;   //!
   TBranch        *b_lep_RelIsoNoFSR;   //!
   TBranch        *b_lep_MiniIso;   //!
   TBranch        *b_lep_ptRatio;   //!
   TBranch        *b_lep_ptRel;   //!
   TBranch        *b_lep_filtersMatched;   //!
   TBranch        *b_lep_dataMC;   //!
   TBranch        *b_lep_dataMCErr;   //!
   TBranch        *b_nisoleptons;   //!
   TBranch        *b_muRho;   //!
   TBranch        *b_elRho;   //!
   TBranch        *b_pTL1;   //!
   TBranch        *b_pTL2;   //!
   TBranch        *b_pTL3;   //!
   TBranch        *b_pTL4;   //!
   TBranch        *b_idL1;   //!
   TBranch        *b_idL2;   //!
   TBranch        *b_idL3;   //!
   TBranch        *b_idL4;   //!
   TBranch        *b_etaL1;   //!
   TBranch        *b_etaL2;   //!
   TBranch        *b_etaL3;   //!
   TBranch        *b_etaL4;   //!
   TBranch        *b_pTL1FSR;   //!
   TBranch        *b_pTL2FSR;   //!
   TBranch        *b_pTL3FSR;   //!
   TBranch        *b_pTL4FSR;   //!
   TBranch        *b_tau_id;   //!
   TBranch        *b_tau_pt;   //!
   TBranch        *b_tau_eta;   //!
   TBranch        *b_tau_phi;   //!
   TBranch        *b_tau_mass;   //!
   TBranch        *b_H_pt;   //!
   TBranch        *b_H_eta;   //!
   TBranch        *b_H_phi;   //!
   TBranch        *b_H_mass;   //!
   TBranch        *b_H_noFSR_pt;   //!
   TBranch        *b_H_noFSR_eta;   //!
   TBranch        *b_H_noFSR_phi;   //!
   TBranch        *b_H_noFSR_mass;   //!
   TBranch        *b_mass4l;   //!
   TBranch        *b_mass4l_noFSR;   //!
   TBranch        *b_mass4lErr;   //!
   TBranch        *b_mass4lREFIT;   //!
   TBranch        *b_mass4lErrREFIT;   //!
   TBranch        *b_massZ1REFIT;   //!
   TBranch        *b_massZ1Err;   //!
   TBranch        *b_mass4mu;   //!
   TBranch        *b_mass4e;   //!
   TBranch        *b_mass2e2mu;   //!
   TBranch        *b_pT4l;   //!
   TBranch        *b_eta4l;   //!
   TBranch        *b_phi4l;   //!
   TBranch        *b_rapidity4l;   //!
   TBranch        *b_cosTheta1;   //!
   TBranch        *b_cosTheta2;   //!
   TBranch        *b_cosThetaStar;   //!
   TBranch        *b_Phi;   //!
   TBranch        *b_Phi1;   //!
   TBranch        *b_mass3l;   //!
   TBranch        *b_Z_pt;   //!
   TBranch        *b_Z_eta;   //!
   TBranch        *b_Z_phi;   //!
   TBranch        *b_Z_mass;   //!
   TBranch        *b_Z_noFSR_pt;   //!
   TBranch        *b_Z_noFSR_eta;   //!
   TBranch        *b_Z_noFSR_phi;   //!
   TBranch        *b_Z_noFSR_mass;   //!
   TBranch        *b_Z_Hindex;   //!
   TBranch        *b_massZ1;   //!
   TBranch        *b_massZ2;   //!
   TBranch        *b_pTZ1;   //!
   TBranch        *b_pTZ2;   //!
   TBranch        *b_met;   //!
   TBranch        *b_met_phi;   //!
   TBranch        *b_met_jesup;   //!
   TBranch        *b_met_phi_jesup;   //!
   TBranch        *b_met_jesdn;   //!
   TBranch        *b_met_phi_jesdn;   //!
   TBranch        *b_met_uncenup;   //!
   TBranch        *b_met_phi_uncenup;   //!
   TBranch        *b_met_uncendn;   //!
   TBranch        *b_met_phi_uncendn;   //!
   TBranch        *b_jet_iscleanH4l;   //!
   TBranch        *b_jet_pt;   //!
   TBranch        *b_jet_relpterr;   //!
   TBranch        *b_jet_eta;   //!
   TBranch        *b_jet_phi;   //!
   TBranch        *b_jet_phierr;   //!
   TBranch        *b_jet_mass;   //!
   TBranch        *b_jet_jesup_iscleanH4l;   //!
   TBranch        *b_jet_jesup_pt;   //!
   TBranch        *b_jet_jesup_eta;   //!
   TBranch        *b_jet_jesup_phi;   //!
   TBranch        *b_jet_jesup_mass;   //!
   TBranch        *b_jet_jesdn_iscleanH4l;   //!
   TBranch        *b_jet_jesdn_pt;   //!
   TBranch        *b_jet_jesdn_eta;   //!
   TBranch        *b_jet_jesdn_phi;   //!
   TBranch        *b_jet_jesdn_mass;   //!
   TBranch        *b_jet_jerup_iscleanH4l;   //!
   TBranch        *b_jet_jerup_pt;   //!
   TBranch        *b_jet_jerup_eta;   //!
   TBranch        *b_jet_jerup_phi;   //!
   TBranch        *b_jet_jerup_mass;   //!
   TBranch        *b_jet_jerdn_iscleanH4l;   //!
   TBranch        *b_jet_jerdn_pt;   //!
   TBranch        *b_jet_jerdn_eta;   //!
   TBranch        *b_jet_jerdn_phi;   //!
   TBranch        *b_jet_jerdn_mass;   //!
   TBranch        *b_jet_pumva;   //!
   TBranch        *b_jet_csvv2;   //!
   TBranch        *b_jet_isbtag;   //!
   TBranch        *b_jet_hadronFlavour;   //!
   TBranch        *b_jet_partonFlavour;   //!
   TBranch        *b_jet_QGTagger;   //!
   TBranch        *b_jet_axis2;   //!
   TBranch        *b_jet_ptD;   //!
   TBranch        *b_jet_mult;   //!
   TBranch        *b_njets_pt30_eta4p7;   //!
   TBranch        *b_njets_pt30_eta4p7_jesup;   //!
   TBranch        *b_njets_pt30_eta4p7_jesdn;   //!
   TBranch        *b_njets_pt30_eta4p7_jerup;   //!
   TBranch        *b_njets_pt30_eta4p7_jerdn;   //!
   TBranch        *b_nbjets_pt30_eta4p7;   //!
   TBranch        *b_nvjets_pt40_eta2p4;   //!
   TBranch        *b_pt_leadingjet_pt30_eta4p7;   //!
   TBranch        *b_pt_leadingjet_pt30_eta4p7_jesup;   //!
   TBranch        *b_pt_leadingjet_pt30_eta4p7_jesdn;   //!
   TBranch        *b_pt_leadingjet_pt30_eta4p7_jerup;   //!
   TBranch        *b_pt_leadingjet_pt30_eta4p7_jerdn;   //!
   TBranch        *b_absrapidity_leadingjet_pt30_eta4p7;   //!
   TBranch        *b_absrapidity_leadingjet_pt30_eta4p7_jesup;   //!
   TBranch        *b_absrapidity_leadingjet_pt30_eta4p7_jesdn;   //!
   TBranch        *b_absrapidity_leadingjet_pt30_eta4p7_jerup;   //!
   TBranch        *b_absrapidity_leadingjet_pt30_eta4p7_jerdn;   //!
   TBranch        *b_absdeltarapidity_hleadingjet_pt30_eta4p7;   //!
   TBranch        *b_absdeltarapidity_hleadingjet_pt30_eta4p7_jesup;   //!
   TBranch        *b_absdeltarapidity_hleadingjet_pt30_eta4p7_jesdn;   //!
   TBranch        *b_absdeltarapidity_hleadingjet_pt30_eta4p7_jerup;   //!
   TBranch        *b_absdeltarapidity_hleadingjet_pt30_eta4p7_jerdn;   //!
   TBranch        *b_DijetMass;   //!
   TBranch        *b_DijetDEta;   //!
   TBranch        *b_DijetFisher;   //!
   TBranch        *b_mergedjet_iscleanH4l;   //!
   TBranch        *b_mergedjet_pt;   //!
   TBranch        *b_mergedjet_eta;   //!
   TBranch        *b_mergedjet_phi;   //!
   TBranch        *b_mergedjet_mass;   //!
   TBranch        *b_mergedjet_tau1;   //!
   TBranch        *b_mergedjet_tau2;   //!
   TBranch        *b_mergedjet_L1;   //!
   TBranch        *b_mergedjet_softdropmass;   //!
   TBranch        *b_mergedjet_prunedmass;   //!
   TBranch        *b_mergedjet_nsubjet;   //!
   TBranch        *b_mergedjet_subjet_pt;   //!
   TBranch        *b_mergedjet_subjet_eta;   //!
   TBranch        *b_mergedjet_subjet_phi;   //!
   TBranch        *b_mergedjet_subjet_mass;   //!
   TBranch        *b_mergedjet_subjet_btag;   //!
   TBranch        *b_nFSRPhotons;   //!
   TBranch        *b_allfsrPhotons_dR;   //!
   TBranch        *b_allfsrPhotons_iso;   //!
   TBranch        *b_allfsrPhotons_pt;   //!
   TBranch        *b_fsrPhotons_lepindex;   //!
   TBranch        *b_fsrPhotons_pt;   //!
   TBranch        *b_fsrPhotons_pterr;   //!
   TBranch        *b_fsrPhotons_eta;   //!
   TBranch        *b_fsrPhotons_phi;   //!
   TBranch        *b_fsrPhotons_dR;   //!
   TBranch        *b_fsrPhotons_iso;   //!
   TBranch        *b_theta12;   //!
   TBranch        *b_theta13;   //!
   TBranch        *b_theta14;   //!
   TBranch        *b_minM3l;   //!
   TBranch        *b_Z4lmaxP;   //!
   TBranch        *b_minDeltR;   //!
   TBranch        *b_m3l_soft;   //!
   TBranch        *b_minMass2Lep;   //!
   TBranch        *b_maxMass2Lep;   //!
   TBranch        *b_thetaPhoton;   //!
   TBranch        *b_thetaPhotonZ;   //!
   TBranch        *b_EventCat;   //!
   TBranch        *b_GENfinalState;   //!
   TBranch        *b_passedFiducialSelection;   //!
   TBranch        *b_GENlep_pt;   //!
   TBranch        *b_GENlep_eta;   //!
   TBranch        *b_GENlep_phi;   //!
   TBranch        *b_GENlep_mass;   //!
   TBranch        *b_GENlep_id;   //!
   TBranch        *b_GENlep_status;   //!
   TBranch        *b_GENlep_MomId;   //!
   TBranch        *b_GENlep_MomMomId;   //!
   TBranch        *b_GENlep_Hindex;   //!
   TBranch        *b_GENlep_isoCH;   //!
   TBranch        *b_GENlep_isoNH;   //!
   TBranch        *b_GENlep_isoPhot;   //!
   TBranch        *b_GENlep_RelIso;   //!
   TBranch        *b_GENH_pt;   //!
   TBranch        *b_GENH_eta;   //!
   TBranch        *b_GENH_phi;   //!
   TBranch        *b_GENH_mass;   //!
   TBranch        *b_GENmass4l;   //!
   TBranch        *b_GENmass4mu;   //!
   TBranch        *b_GENmass4e;   //!
   TBranch        *b_GENmass2e2mu;   //!
   TBranch        *b_GENpT4l;   //!
   TBranch        *b_GENeta4l;   //!
   TBranch        *b_GENrapidity4l;   //!
   TBranch        *b_GENcosTheta1;   //!
   TBranch        *b_GENcosTheta2;   //!
   TBranch        *b_GENcosThetaStar;   //!
   TBranch        *b_GENPhi;   //!
   TBranch        *b_GENPhi1;   //!
   TBranch        *b_GENMH;   //!
   TBranch        *b_GENZ_pt;   //!
   TBranch        *b_GENZ_eta;   //!
   TBranch        *b_GENZ_phi;   //!
   TBranch        *b_GENZ_mass;   //!
   TBranch        *b_GENZ_DaughtersId;   //!
   TBranch        *b_GENZ_MomId;   //!
   TBranch        *b_GENmassZ1;   //!
   TBranch        *b_GENmassZ2;   //!
   TBranch        *b_GENpTZ1;   //!
   TBranch        *b_GENpTZ2;   //!
   TBranch        *b_GENdPhiZZ;   //!
   TBranch        *b_GENmassZZ;   //!
   TBranch        *b_GENpTZZ;   //!
   TBranch        *b_GENHmass;   //!
   TBranch        *b_GENjet_pt;   //!
   TBranch        *b_GENjet_eta;   //!
   TBranch        *b_GENjet_phi;   //!
   TBranch        *b_GENjet_mass;   //!
   TBranch        *b_GENnjets_pt30_eta4p7;   //!
   TBranch        *b_GENpt_leadingjet_pt30_eta4p7;   //!
   TBranch        *b_GENabsrapidity_leadingjet_pt30_eta4p7;   //!
   TBranch        *b_GENabsdeltarapidity_hleadingjet_pt30_eta4p7;   //!
   TBranch        *b_lheNj;   //!
   TBranch        *b_lheNb;   //!
   TBranch        *b_nGenStatus2bHad;   //!
   TBranch        *b_me_0plus_JHU;   //!
   TBranch        *b_me_qqZZ_MCFM;   //!
   TBranch        *b_p0plus_m4l;   //!
   TBranch        *b_bkg_m4l;   //!
   TBranch        *b_D_bkg_kin;   //!
   TBranch        *b_D_bkg;   //!
   TBranch        *b_Dgg10_VAMCFM;   //!
   TBranch        *b_Djet_VAJHU;   //!
   TBranch        *b_Djet_VAJHU_jesup;   //!
   TBranch        *b_Djet_VAJHU_jesdn;   //!
   TBranch        *b_D_g4;   //!

   MySelector_UFHZZZ4L(TTree * /*tree*/ =0) : fChain(0) { }
   virtual ~MySelector_UFHZZZ4L() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();

   ClassDef(MySelector_UFHZZZ4L,0);
};

#endif

#ifdef MySelector_UFHZZZ4L_cxx
void MySelector_UFHZZZ4L::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   triggersPassed = 0;
   pdfWeights = 0;
   pdfWeightIDs = 0;
   lep_id = 0;
   lep_pt = 0;
   lep_pterr = 0;
   lep_pterrold = 0;
   lep_eta = 0;
   lep_phi = 0;
   lep_mass = 0;
   lepFSR_pt = 0;
   lepFSR_eta = 0;
   lepFSR_phi = 0;
   lepFSR_mass = 0;
   lep_genindex = 0;
   lep_missingHits = 0;
   lep_mva = 0;
   lep_ecalDriven = 0;
   lep_tightId = 0;
   lep_tightIdSUS = 0;
   lep_tightIdHiPt = 0;
   lep_Sip = 0;
   lep_IP = 0;
   lep_isoNH = 0;
   lep_isoCH = 0;
   lep_isoPhot = 0;
   lep_isoPU = 0;
   lep_isoPUcorr = 0;
   lep_RelIso = 0;
   lep_RelIsoNoFSR = 0;
   lep_MiniIso = 0;
   lep_ptRatio = 0;
   lep_ptRel = 0;
   lep_filtersMatched = 0;
   lep_dataMC = 0;
   lep_dataMCErr = 0;
   tau_id = 0;
   tau_pt = 0;
   tau_eta = 0;
   tau_phi = 0;
   tau_mass = 0;
   H_pt = 0;
   H_eta = 0;
   H_phi = 0;
   H_mass = 0;
   H_noFSR_pt = 0;
   H_noFSR_eta = 0;
   H_noFSR_phi = 0;
   H_noFSR_mass = 0;
   Z_pt = 0;
   Z_eta = 0;
   Z_phi = 0;
   Z_mass = 0;
   Z_noFSR_pt = 0;
   Z_noFSR_eta = 0;
   Z_noFSR_phi = 0;
   Z_noFSR_mass = 0;
   jet_iscleanH4l = 0;
   jet_pt = 0;
   jet_relpterr = 0;
   jet_eta = 0;
   jet_phi = 0;
   jet_phierr = 0;
   jet_mass = 0;
   jet_jesup_iscleanH4l = 0;
   jet_jesup_pt = 0;
   jet_jesup_eta = 0;
   jet_jesup_phi = 0;
   jet_jesup_mass = 0;
   jet_jesdn_iscleanH4l = 0;
   jet_jesdn_pt = 0;
   jet_jesdn_eta = 0;
   jet_jesdn_phi = 0;
   jet_jesdn_mass = 0;
   jet_jerup_iscleanH4l = 0;
   jet_jerup_pt = 0;
   jet_jerup_eta = 0;
   jet_jerup_phi = 0;
   jet_jerup_mass = 0;
   jet_jerdn_iscleanH4l = 0;
   jet_jerdn_pt = 0;
   jet_jerdn_eta = 0;
   jet_jerdn_phi = 0;
   jet_jerdn_mass = 0;
   jet_pumva = 0;
   jet_csvv2 = 0;
   jet_isbtag = 0;
   jet_hadronFlavour = 0;
   jet_partonFlavour = 0;
   jet_QGTagger = 0;
   jet_axis2 = 0;
   jet_ptD = 0;
   jet_mult = 0;
   mergedjet_iscleanH4l = 0;
   mergedjet_pt = 0;
   mergedjet_eta = 0;
   mergedjet_phi = 0;
   mergedjet_mass = 0;
   mergedjet_tau1 = 0;
   mergedjet_tau2 = 0;
   mergedjet_L1 = 0;
   mergedjet_softdropmass = 0;
   mergedjet_prunedmass = 0;
   mergedjet_nsubjet = 0;
   mergedjet_subjet_pt = 0;
   mergedjet_subjet_eta = 0;
   mergedjet_subjet_phi = 0;
   mergedjet_subjet_mass = 0;
   mergedjet_subjet_btag = 0;
   allfsrPhotons_dR = 0;
   allfsrPhotons_iso = 0;
   allfsrPhotons_pt = 0;
   fsrPhotons_lepindex = 0;
   fsrPhotons_pt = 0;
   fsrPhotons_pterr = 0;
   fsrPhotons_eta = 0;
   fsrPhotons_phi = 0;
   fsrPhotons_dR = 0;
   fsrPhotons_iso = 0;
   GENlep_pt = 0;
   GENlep_eta = 0;
   GENlep_phi = 0;
   GENlep_mass = 0;
   GENlep_id = 0;
   GENlep_status = 0;
   GENlep_MomId = 0;
   GENlep_MomMomId = 0;
   GENlep_isoCH = 0;
   GENlep_isoNH = 0;
   GENlep_isoPhot = 0;
   GENlep_RelIso = 0;
   GENH_pt = 0;
   GENH_eta = 0;
   GENH_phi = 0;
   GENH_mass = 0;
   GENZ_pt = 0;
   GENZ_eta = 0;
   GENZ_phi = 0;
   GENZ_mass = 0;
   GENZ_DaughtersId = 0;
   GENZ_MomId = 0;
   GENjet_pt = 0;
   GENjet_eta = 0;
   GENjet_phi = 0;
   GENjet_mass = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("Run", &Run, &b_Run);
   fChain->SetBranchAddress("Event", &Event, &b_Event);
   fChain->SetBranchAddress("LumiSect", &LumiSect, &b_LumiSect);
   fChain->SetBranchAddress("nVtx", &nVtx, &b_nVtx);
   fChain->SetBranchAddress("nInt", &nInt, &b_nInt);
   fChain->SetBranchAddress("finalState", &finalState, &b_finalState);
   fChain->SetBranchAddress("triggersPassed", &triggersPassed, &b_triggersPassed);
   fChain->SetBranchAddress("passedTrig", &passedTrig, &b_passedTrig);
   fChain->SetBranchAddress("passedFullSelection", &passedFullSelection, &b_passedFullSelection);
   fChain->SetBranchAddress("passedZ4lSelection", &passedZ4lSelection, &b_passedZ4lSelection);
   fChain->SetBranchAddress("passedQCDcut", &passedQCDcut, &b_passedQCDcut);
   fChain->SetBranchAddress("passedZ1LSelection", &passedZ1LSelection, &b_passedZ1LSelection);
   fChain->SetBranchAddress("passedZ4lZXCRSelection", &passedZ4lZXCRSelection, &b_passedZ4lZXCRSelection);
   fChain->SetBranchAddress("passedZXCRSelection", &passedZXCRSelection, &b_passedZXCRSelection);
   fChain->SetBranchAddress("nZXCRFailedLeptons", &nZXCRFailedLeptons, &b_nZXCRFailedLeptons);
   fChain->SetBranchAddress("genWeight", &genWeight, &b_genWeight);
   fChain->SetBranchAddress("k_ggZZ", &k_ggZZ, &b_k_ggZZ);
   fChain->SetBranchAddress("k_qqZZ_qcd_dPhi", &k_qqZZ_qcd_dPhi, &b_k_qqZZ_qcd_dPhi);
   fChain->SetBranchAddress("k_qqZZ_qcd_M", &k_qqZZ_qcd_M, &b_k_qqZZ_qcd_M);
   fChain->SetBranchAddress("k_qqZZ_qcd_Pt", &k_qqZZ_qcd_Pt, &b_k_qqZZ_qcd_Pt);
   fChain->SetBranchAddress("k_qqZZ_ewk", &k_qqZZ_ewk, &b_k_qqZZ_ewk);
   fChain->SetBranchAddress("pdfWeights", &pdfWeights, &b_pdfWeights);
   fChain->SetBranchAddress("pdfWeightIDs", &pdfWeightIDs, &b_pdfWeightIDs);
   fChain->SetBranchAddress("pdfRMSup", &pdfRMSup, &b_pdfRMSup);
   fChain->SetBranchAddress("pdfRMSdown", &pdfRMSdown, &b_pdfRMSdown);
   fChain->SetBranchAddress("pdfENVup", &pdfENVup, &b_pdfENVup);
   fChain->SetBranchAddress("pdfENVdown", &pdfENVdown, &b_pdfENVdown);
   fChain->SetBranchAddress("pileupWeight", &pileupWeight, &b_pileupWeight);
   fChain->SetBranchAddress("dataMCWeight", &dataMCWeight, &b_dataMCWeight);
   fChain->SetBranchAddress("eventWeight", &eventWeight, &b_eventWeight);
   fChain->SetBranchAddress("crossSection", &crossSection, &b_crossSection);
   fChain->SetBranchAddress("lep_id", &lep_id, &b_lep_id);
   fChain->SetBranchAddress("lep_pt", &lep_pt, &b_lep_pt);
   fChain->SetBranchAddress("lep_pterr", &lep_pterr, &b_lep_pterr);
   fChain->SetBranchAddress("lep_pterrold", &lep_pterrold, &b_lep_pterrold);
   fChain->SetBranchAddress("lep_eta", &lep_eta, &b_lep_eta);
   fChain->SetBranchAddress("lep_phi", &lep_phi, &b_lep_phi);
   fChain->SetBranchAddress("lep_mass", &lep_mass, &b_lep_mass);
   fChain->SetBranchAddress("lepFSR_pt", &lepFSR_pt, &b_lepFSR_pt);
   fChain->SetBranchAddress("lepFSR_eta", &lepFSR_eta, &b_lepFSR_eta);
   fChain->SetBranchAddress("lepFSR_phi", &lepFSR_phi, &b_lepFSR_phi);
   fChain->SetBranchAddress("lepFSR_mass", &lepFSR_mass, &b_lepFSR_mass);
   fChain->SetBranchAddress("lep_Hindex", lep_Hindex, &b_lep_Hindex);
   fChain->SetBranchAddress("lep_genindex", &lep_genindex, &b_lep_genindex);
   fChain->SetBranchAddress("lep_missingHits", &lep_missingHits, &b_lep_missingHits);
   fChain->SetBranchAddress("lep_mva", &lep_mva, &b_lep_mva);
   fChain->SetBranchAddress("lep_ecalDriven", &lep_ecalDriven, &b_lep_ecalDriven);
   fChain->SetBranchAddress("lep_tightId", &lep_tightId, &b_lep_tightId);
   fChain->SetBranchAddress("lep_tightIdSUS", &lep_tightIdSUS, &b_lep_tightIdSUS);
   fChain->SetBranchAddress("lep_tightIdHiPt", &lep_tightIdHiPt, &b_lep_tightIdHiPt);
   fChain->SetBranchAddress("lep_Sip", &lep_Sip, &b_lep_Sip);
   fChain->SetBranchAddress("lep_IP", &lep_IP, &b_lep_IP);
   fChain->SetBranchAddress("lep_isoNH", &lep_isoNH, &b_lep_isoNH);
   fChain->SetBranchAddress("lep_isoCH", &lep_isoCH, &b_lep_isoCH);
   fChain->SetBranchAddress("lep_isoPhot", &lep_isoPhot, &b_lep_isoPhot);
   fChain->SetBranchAddress("lep_isoPU", &lep_isoPU, &b_lep_isoPU);
   fChain->SetBranchAddress("lep_isoPUcorr", &lep_isoPUcorr, &b_lep_isoPUcorr);
   fChain->SetBranchAddress("lep_RelIso", &lep_RelIso, &b_lep_RelIso);
   fChain->SetBranchAddress("lep_RelIsoNoFSR", &lep_RelIsoNoFSR, &b_lep_RelIsoNoFSR);
   fChain->SetBranchAddress("lep_MiniIso", &lep_MiniIso, &b_lep_MiniIso);
   fChain->SetBranchAddress("lep_ptRatio", &lep_ptRatio, &b_lep_ptRatio);
   fChain->SetBranchAddress("lep_ptRel", &lep_ptRel, &b_lep_ptRel);
   fChain->SetBranchAddress("lep_filtersMatched", &lep_filtersMatched, &b_lep_filtersMatched);
   fChain->SetBranchAddress("lep_dataMC", &lep_dataMC, &b_lep_dataMC);
   fChain->SetBranchAddress("lep_dataMCErr", &lep_dataMCErr, &b_lep_dataMCErr);
   fChain->SetBranchAddress("nisoleptons", &nisoleptons, &b_nisoleptons);
   fChain->SetBranchAddress("muRho", &muRho, &b_muRho);
   fChain->SetBranchAddress("elRho", &elRho, &b_elRho);
   fChain->SetBranchAddress("pTL1", &pTL1, &b_pTL1);
   fChain->SetBranchAddress("pTL2", &pTL2, &b_pTL2);
   fChain->SetBranchAddress("pTL3", &pTL3, &b_pTL3);
   fChain->SetBranchAddress("pTL4", &pTL4, &b_pTL4);
   fChain->SetBranchAddress("idL1", &idL1, &b_idL1);
   fChain->SetBranchAddress("idL2", &idL2, &b_idL2);
   fChain->SetBranchAddress("idL3", &idL3, &b_idL3);
   fChain->SetBranchAddress("idL4", &idL4, &b_idL4);
   fChain->SetBranchAddress("etaL1", &etaL1, &b_etaL1);
   fChain->SetBranchAddress("etaL2", &etaL2, &b_etaL2);
   fChain->SetBranchAddress("etaL3", &etaL3, &b_etaL3);
   fChain->SetBranchAddress("etaL4", &etaL4, &b_etaL4);
   fChain->SetBranchAddress("pTL1FSR", &pTL1FSR, &b_pTL1FSR);
   fChain->SetBranchAddress("pTL2FSR", &pTL2FSR, &b_pTL2FSR);
   fChain->SetBranchAddress("pTL3FSR", &pTL3FSR, &b_pTL3FSR);
   fChain->SetBranchAddress("pTL4FSR", &pTL4FSR, &b_pTL4FSR);
   fChain->SetBranchAddress("tau_id", &tau_id, &b_tau_id);
   fChain->SetBranchAddress("tau_pt", &tau_pt, &b_tau_pt);
   fChain->SetBranchAddress("tau_eta", &tau_eta, &b_tau_eta);
   fChain->SetBranchAddress("tau_phi", &tau_phi, &b_tau_phi);
   fChain->SetBranchAddress("tau_mass", &tau_mass, &b_tau_mass);
   fChain->SetBranchAddress("H_pt", &H_pt, &b_H_pt);
   fChain->SetBranchAddress("H_eta", &H_eta, &b_H_eta);
   fChain->SetBranchAddress("H_phi", &H_phi, &b_H_phi);
   fChain->SetBranchAddress("H_mass", &H_mass, &b_H_mass);
   fChain->SetBranchAddress("H_noFSR_pt", &H_noFSR_pt, &b_H_noFSR_pt);
   fChain->SetBranchAddress("H_noFSR_eta", &H_noFSR_eta, &b_H_noFSR_eta);
   fChain->SetBranchAddress("H_noFSR_phi", &H_noFSR_phi, &b_H_noFSR_phi);
   fChain->SetBranchAddress("H_noFSR_mass", &H_noFSR_mass, &b_H_noFSR_mass);
   fChain->SetBranchAddress("mass4l", &mass4l, &b_mass4l);
   fChain->SetBranchAddress("mass4l_noFSR", &mass4l_noFSR, &b_mass4l_noFSR);
   fChain->SetBranchAddress("mass4lErr", &mass4lErr, &b_mass4lErr);
   fChain->SetBranchAddress("mass4lREFIT", &mass4lREFIT, &b_mass4lREFIT);
   fChain->SetBranchAddress("mass4lErrREFIT", &mass4lErrREFIT, &b_mass4lErrREFIT);
   fChain->SetBranchAddress("massZ1REFIT", &massZ1REFIT, &b_massZ1REFIT);
   fChain->SetBranchAddress("massZ1Err", &massZ1Err, &b_massZ1Err);
   fChain->SetBranchAddress("mass4mu", &mass4mu, &b_mass4mu);
   fChain->SetBranchAddress("mass4e", &mass4e, &b_mass4e);
   fChain->SetBranchAddress("mass2e2mu", &mass2e2mu, &b_mass2e2mu);
   fChain->SetBranchAddress("pT4l", &pT4l, &b_pT4l);
   fChain->SetBranchAddress("eta4l", &eta4l, &b_eta4l);
   fChain->SetBranchAddress("phi4l", &phi4l, &b_phi4l);
   fChain->SetBranchAddress("rapidity4l", &rapidity4l, &b_rapidity4l);
   fChain->SetBranchAddress("cosTheta1", &cosTheta1, &b_cosTheta1);
   fChain->SetBranchAddress("cosTheta2", &cosTheta2, &b_cosTheta2);
   fChain->SetBranchAddress("cosThetaStar", &cosThetaStar, &b_cosThetaStar);
   fChain->SetBranchAddress("Phi", &Phi, &b_Phi);
   fChain->SetBranchAddress("Phi1", &Phi1, &b_Phi1);
   fChain->SetBranchAddress("mass3l", &mass3l, &b_mass3l);
   fChain->SetBranchAddress("Z_pt", &Z_pt, &b_Z_pt);
   fChain->SetBranchAddress("Z_eta", &Z_eta, &b_Z_eta);
   fChain->SetBranchAddress("Z_phi", &Z_phi, &b_Z_phi);
   fChain->SetBranchAddress("Z_mass", &Z_mass, &b_Z_mass);
   fChain->SetBranchAddress("Z_noFSR_pt", &Z_noFSR_pt, &b_Z_noFSR_pt);
   fChain->SetBranchAddress("Z_noFSR_eta", &Z_noFSR_eta, &b_Z_noFSR_eta);
   fChain->SetBranchAddress("Z_noFSR_phi", &Z_noFSR_phi, &b_Z_noFSR_phi);
   fChain->SetBranchAddress("Z_noFSR_mass", &Z_noFSR_mass, &b_Z_noFSR_mass);
   fChain->SetBranchAddress("Z_Hindex", Z_Hindex, &b_Z_Hindex);
   fChain->SetBranchAddress("massZ1", &massZ1, &b_massZ1);
   fChain->SetBranchAddress("massZ2", &massZ2, &b_massZ2);
   fChain->SetBranchAddress("pTZ1", &pTZ1, &b_pTZ1);
   fChain->SetBranchAddress("pTZ2", &pTZ2, &b_pTZ2);
   fChain->SetBranchAddress("met", &met, &b_met);
   fChain->SetBranchAddress("met_phi", &met_phi, &b_met_phi);
   fChain->SetBranchAddress("met_jesup", &met_jesup, &b_met_jesup);
   fChain->SetBranchAddress("met_phi_jesup", &met_phi_jesup, &b_met_phi_jesup);
   fChain->SetBranchAddress("met_jesdn", &met_jesdn, &b_met_jesdn);
   fChain->SetBranchAddress("met_phi_jesdn", &met_phi_jesdn, &b_met_phi_jesdn);
   fChain->SetBranchAddress("met_uncenup", &met_uncenup, &b_met_uncenup);
   fChain->SetBranchAddress("met_phi_uncenup", &met_phi_uncenup, &b_met_phi_uncenup);
   fChain->SetBranchAddress("met_uncendn", &met_uncendn, &b_met_uncendn);
   fChain->SetBranchAddress("met_phi_uncendn", &met_phi_uncendn, &b_met_phi_uncendn);
   fChain->SetBranchAddress("jet_iscleanH4l", &jet_iscleanH4l, &b_jet_iscleanH4l);
   fChain->SetBranchAddress("jet_pt", &jet_pt, &b_jet_pt);
   fChain->SetBranchAddress("jet_relpterr", &jet_relpterr, &b_jet_relpterr);
   fChain->SetBranchAddress("jet_eta", &jet_eta, &b_jet_eta);
   fChain->SetBranchAddress("jet_phi", &jet_phi, &b_jet_phi);
   fChain->SetBranchAddress("jet_phierr", &jet_phierr, &b_jet_phierr);
   fChain->SetBranchAddress("jet_mass", &jet_mass, &b_jet_mass);
   fChain->SetBranchAddress("jet_jesup_iscleanH4l", &jet_jesup_iscleanH4l, &b_jet_jesup_iscleanH4l);
   fChain->SetBranchAddress("jet_jesup_pt", &jet_jesup_pt, &b_jet_jesup_pt);
   fChain->SetBranchAddress("jet_jesup_eta", &jet_jesup_eta, &b_jet_jesup_eta);
   fChain->SetBranchAddress("jet_jesup_phi", &jet_jesup_phi, &b_jet_jesup_phi);
   fChain->SetBranchAddress("jet_jesup_mass", &jet_jesup_mass, &b_jet_jesup_mass);
   fChain->SetBranchAddress("jet_jesdn_iscleanH4l", &jet_jesdn_iscleanH4l, &b_jet_jesdn_iscleanH4l);
   fChain->SetBranchAddress("jet_jesdn_pt", &jet_jesdn_pt, &b_jet_jesdn_pt);
   fChain->SetBranchAddress("jet_jesdn_eta", &jet_jesdn_eta, &b_jet_jesdn_eta);
   fChain->SetBranchAddress("jet_jesdn_phi", &jet_jesdn_phi, &b_jet_jesdn_phi);
   fChain->SetBranchAddress("jet_jesdn_mass", &jet_jesdn_mass, &b_jet_jesdn_mass);
   fChain->SetBranchAddress("jet_jerup_iscleanH4l", &jet_jerup_iscleanH4l, &b_jet_jerup_iscleanH4l);
   fChain->SetBranchAddress("jet_jerup_pt", &jet_jerup_pt, &b_jet_jerup_pt);
   fChain->SetBranchAddress("jet_jerup_eta", &jet_jerup_eta, &b_jet_jerup_eta);
   fChain->SetBranchAddress("jet_jerup_phi", &jet_jerup_phi, &b_jet_jerup_phi);
   fChain->SetBranchAddress("jet_jerup_mass", &jet_jerup_mass, &b_jet_jerup_mass);
   fChain->SetBranchAddress("jet_jerdn_iscleanH4l", &jet_jerdn_iscleanH4l, &b_jet_jerdn_iscleanH4l);
   fChain->SetBranchAddress("jet_jerdn_pt", &jet_jerdn_pt, &b_jet_jerdn_pt);
   fChain->SetBranchAddress("jet_jerdn_eta", &jet_jerdn_eta, &b_jet_jerdn_eta);
   fChain->SetBranchAddress("jet_jerdn_phi", &jet_jerdn_phi, &b_jet_jerdn_phi);
   fChain->SetBranchAddress("jet_jerdn_mass", &jet_jerdn_mass, &b_jet_jerdn_mass);
   fChain->SetBranchAddress("jet_pumva", &jet_pumva, &b_jet_pumva);
   fChain->SetBranchAddress("jet_csvv2", &jet_csvv2, &b_jet_csvv2);
   fChain->SetBranchAddress("jet_isbtag", &jet_isbtag, &b_jet_isbtag);
   fChain->SetBranchAddress("jet_hadronFlavour", &jet_hadronFlavour, &b_jet_hadronFlavour);
   fChain->SetBranchAddress("jet_partonFlavour", &jet_partonFlavour, &b_jet_partonFlavour);
   fChain->SetBranchAddress("jet_QGTagger", &jet_QGTagger, &b_jet_QGTagger);
   fChain->SetBranchAddress("jet_axis2", &jet_axis2, &b_jet_axis2);
   fChain->SetBranchAddress("jet_ptD", &jet_ptD, &b_jet_ptD);
   fChain->SetBranchAddress("jet_mult", &jet_mult, &b_jet_mult);
   fChain->SetBranchAddress("njets_pt30_eta4p7", &njets_pt30_eta4p7, &b_njets_pt30_eta4p7);
   fChain->SetBranchAddress("njets_pt30_eta4p7_jesup", &njets_pt30_eta4p7_jesup, &b_njets_pt30_eta4p7_jesup);
   fChain->SetBranchAddress("njets_pt30_eta4p7_jesdn", &njets_pt30_eta4p7_jesdn, &b_njets_pt30_eta4p7_jesdn);
   fChain->SetBranchAddress("njets_pt30_eta4p7_jerup", &njets_pt30_eta4p7_jerup, &b_njets_pt30_eta4p7_jerup);
   fChain->SetBranchAddress("njets_pt30_eta4p7_jerdn", &njets_pt30_eta4p7_jerdn, &b_njets_pt30_eta4p7_jerdn);
   fChain->SetBranchAddress("nbjets_pt30_eta4p7", &nbjets_pt30_eta4p7, &b_nbjets_pt30_eta4p7);
   fChain->SetBranchAddress("nvjets_pt40_eta2p4", &nvjets_pt40_eta2p4, &b_nvjets_pt40_eta2p4);
   fChain->SetBranchAddress("pt_leadingjet_pt30_eta4p7", &pt_leadingjet_pt30_eta4p7, &b_pt_leadingjet_pt30_eta4p7);
   fChain->SetBranchAddress("pt_leadingjet_pt30_eta4p7_jesup", &pt_leadingjet_pt30_eta4p7_jesup, &b_pt_leadingjet_pt30_eta4p7_jesup);
   fChain->SetBranchAddress("pt_leadingjet_pt30_eta4p7_jesdn", &pt_leadingjet_pt30_eta4p7_jesdn, &b_pt_leadingjet_pt30_eta4p7_jesdn);
   fChain->SetBranchAddress("pt_leadingjet_pt30_eta4p7_jerup", &pt_leadingjet_pt30_eta4p7_jerup, &b_pt_leadingjet_pt30_eta4p7_jerup);
   fChain->SetBranchAddress("pt_leadingjet_pt30_eta4p7_jerdn", &pt_leadingjet_pt30_eta4p7_jerdn, &b_pt_leadingjet_pt30_eta4p7_jerdn);
   fChain->SetBranchAddress("absrapidity_leadingjet_pt30_eta4p7", &absrapidity_leadingjet_pt30_eta4p7, &b_absrapidity_leadingjet_pt30_eta4p7);
   fChain->SetBranchAddress("absrapidity_leadingjet_pt30_eta4p7_jesup", &absrapidity_leadingjet_pt30_eta4p7_jesup, &b_absrapidity_leadingjet_pt30_eta4p7_jesup);
   fChain->SetBranchAddress("absrapidity_leadingjet_pt30_eta4p7_jesdn", &absrapidity_leadingjet_pt30_eta4p7_jesdn, &b_absrapidity_leadingjet_pt30_eta4p7_jesdn);
   fChain->SetBranchAddress("absrapidity_leadingjet_pt30_eta4p7_jerup", &absrapidity_leadingjet_pt30_eta4p7_jerup, &b_absrapidity_leadingjet_pt30_eta4p7_jerup);
   fChain->SetBranchAddress("absrapidity_leadingjet_pt30_eta4p7_jerdn", &absrapidity_leadingjet_pt30_eta4p7_jerdn, &b_absrapidity_leadingjet_pt30_eta4p7_jerdn);
   fChain->SetBranchAddress("absdeltarapidity_hleadingjet_pt30_eta4p7", &absdeltarapidity_hleadingjet_pt30_eta4p7, &b_absdeltarapidity_hleadingjet_pt30_eta4p7);
   fChain->SetBranchAddress("absdeltarapidity_hleadingjet_pt30_eta4p7_jesup", &absdeltarapidity_hleadingjet_pt30_eta4p7_jesup, &b_absdeltarapidity_hleadingjet_pt30_eta4p7_jesup);
   fChain->SetBranchAddress("absdeltarapidity_hleadingjet_pt30_eta4p7_jesdn", &absdeltarapidity_hleadingjet_pt30_eta4p7_jesdn, &b_absdeltarapidity_hleadingjet_pt30_eta4p7_jesdn);
   fChain->SetBranchAddress("absdeltarapidity_hleadingjet_pt30_eta4p7_jerup", &absdeltarapidity_hleadingjet_pt30_eta4p7_jerup, &b_absdeltarapidity_hleadingjet_pt30_eta4p7_jerup);
   fChain->SetBranchAddress("absdeltarapidity_hleadingjet_pt30_eta4p7_jerdn", &absdeltarapidity_hleadingjet_pt30_eta4p7_jerdn, &b_absdeltarapidity_hleadingjet_pt30_eta4p7_jerdn);
   fChain->SetBranchAddress("DijetMass", &DijetMass, &b_DijetMass);
   fChain->SetBranchAddress("DijetDEta", &DijetDEta, &b_DijetDEta);
   fChain->SetBranchAddress("DijetFisher", &DijetFisher, &b_DijetFisher);
   fChain->SetBranchAddress("mergedjet_iscleanH4l", &mergedjet_iscleanH4l, &b_mergedjet_iscleanH4l);
   fChain->SetBranchAddress("mergedjet_pt", &mergedjet_pt, &b_mergedjet_pt);
   fChain->SetBranchAddress("mergedjet_eta", &mergedjet_eta, &b_mergedjet_eta);
   fChain->SetBranchAddress("mergedjet_phi", &mergedjet_phi, &b_mergedjet_phi);
   fChain->SetBranchAddress("mergedjet_mass", &mergedjet_mass, &b_mergedjet_mass);
   fChain->SetBranchAddress("mergedjet_tau1", &mergedjet_tau1, &b_mergedjet_tau1);
   fChain->SetBranchAddress("mergedjet_tau2", &mergedjet_tau2, &b_mergedjet_tau2);
   fChain->SetBranchAddress("mergedjet_L1", &mergedjet_L1, &b_mergedjet_L1);
   fChain->SetBranchAddress("mergedjet_softdropmass", &mergedjet_softdropmass, &b_mergedjet_softdropmass);
   fChain->SetBranchAddress("mergedjet_prunedmass", &mergedjet_prunedmass, &b_mergedjet_prunedmass);
   fChain->SetBranchAddress("mergedjet_nsubjet", &mergedjet_nsubjet, &b_mergedjet_nsubjet);
   fChain->SetBranchAddress("mergedjet_subjet_pt", &mergedjet_subjet_pt, &b_mergedjet_subjet_pt);
   fChain->SetBranchAddress("mergedjet_subjet_eta", &mergedjet_subjet_eta, &b_mergedjet_subjet_eta);
   fChain->SetBranchAddress("mergedjet_subjet_phi", &mergedjet_subjet_phi, &b_mergedjet_subjet_phi);
   fChain->SetBranchAddress("mergedjet_subjet_mass", &mergedjet_subjet_mass, &b_mergedjet_subjet_mass);
   fChain->SetBranchAddress("mergedjet_subjet_btag", &mergedjet_subjet_btag, &b_mergedjet_subjet_btag);
   fChain->SetBranchAddress("nFSRPhotons", &nFSRPhotons, &b_nFSRPhotons);
   fChain->SetBranchAddress("allfsrPhotons_dR", &allfsrPhotons_dR, &b_allfsrPhotons_dR);
   fChain->SetBranchAddress("allfsrPhotons_iso", &allfsrPhotons_iso, &b_allfsrPhotons_iso);
   fChain->SetBranchAddress("allfsrPhotons_pt", &allfsrPhotons_pt, &b_allfsrPhotons_pt);
   fChain->SetBranchAddress("fsrPhotons_lepindex", &fsrPhotons_lepindex, &b_fsrPhotons_lepindex);
   fChain->SetBranchAddress("fsrPhotons_pt", &fsrPhotons_pt, &b_fsrPhotons_pt);
   fChain->SetBranchAddress("fsrPhotons_pterr", &fsrPhotons_pterr, &b_fsrPhotons_pterr);
   fChain->SetBranchAddress("fsrPhotons_eta", &fsrPhotons_eta, &b_fsrPhotons_eta);
   fChain->SetBranchAddress("fsrPhotons_phi", &fsrPhotons_phi, &b_fsrPhotons_phi);
   fChain->SetBranchAddress("fsrPhotons_dR", &fsrPhotons_dR, &b_fsrPhotons_dR);
   fChain->SetBranchAddress("fsrPhotons_iso", &fsrPhotons_iso, &b_fsrPhotons_iso);
   fChain->SetBranchAddress("theta12", &theta12, &b_theta12);
   fChain->SetBranchAddress("theta13", &theta13, &b_theta13);
   fChain->SetBranchAddress("theta14", &theta14, &b_theta14);
   fChain->SetBranchAddress("minM3l", &minM3l, &b_minM3l);
   fChain->SetBranchAddress("Z4lmaxP", &Z4lmaxP, &b_Z4lmaxP);
   fChain->SetBranchAddress("minDeltR", &minDeltR, &b_minDeltR);
   fChain->SetBranchAddress("m3l_soft", &m3l_soft, &b_m3l_soft);
   fChain->SetBranchAddress("minMass2Lep", &minMass2Lep, &b_minMass2Lep);
   fChain->SetBranchAddress("maxMass2Lep", &maxMass2Lep, &b_maxMass2Lep);
   fChain->SetBranchAddress("thetaPhoton", &thetaPhoton, &b_thetaPhoton);
   fChain->SetBranchAddress("thetaPhotonZ", &thetaPhotonZ, &b_thetaPhotonZ);
   fChain->SetBranchAddress("EventCat", &EventCat, &b_EventCat);
   fChain->SetBranchAddress("GENfinalState", &GENfinalState, &b_GENfinalState);
   fChain->SetBranchAddress("passedFiducialSelection", &passedFiducialSelection, &b_passedFiducialSelection);
   fChain->SetBranchAddress("GENlep_pt", &GENlep_pt, &b_GENlep_pt);
   fChain->SetBranchAddress("GENlep_eta", &GENlep_eta, &b_GENlep_eta);
   fChain->SetBranchAddress("GENlep_phi", &GENlep_phi, &b_GENlep_phi);
   fChain->SetBranchAddress("GENlep_mass", &GENlep_mass, &b_GENlep_mass);
   fChain->SetBranchAddress("GENlep_id", &GENlep_id, &b_GENlep_id);
   fChain->SetBranchAddress("GENlep_status", &GENlep_status, &b_GENlep_status);
   fChain->SetBranchAddress("GENlep_MomId", &GENlep_MomId, &b_GENlep_MomId);
   fChain->SetBranchAddress("GENlep_MomMomId", &GENlep_MomMomId, &b_GENlep_MomMomId);
   fChain->SetBranchAddress("GENlep_Hindex", GENlep_Hindex, &b_GENlep_Hindex);
   fChain->SetBranchAddress("GENlep_isoCH", &GENlep_isoCH, &b_GENlep_isoCH);
   fChain->SetBranchAddress("GENlep_isoNH", &GENlep_isoNH, &b_GENlep_isoNH);
   fChain->SetBranchAddress("GENlep_isoPhot", &GENlep_isoPhot, &b_GENlep_isoPhot);
   fChain->SetBranchAddress("GENlep_RelIso", &GENlep_RelIso, &b_GENlep_RelIso);
   fChain->SetBranchAddress("GENH_pt", &GENH_pt, &b_GENH_pt);
   fChain->SetBranchAddress("GENH_eta", &GENH_eta, &b_GENH_eta);
   fChain->SetBranchAddress("GENH_phi", &GENH_phi, &b_GENH_phi);
   fChain->SetBranchAddress("GENH_mass", &GENH_mass, &b_GENH_mass);
   fChain->SetBranchAddress("GENmass4l", &GENmass4l, &b_GENmass4l);
   fChain->SetBranchAddress("GENmass4mu", &GENmass4mu, &b_GENmass4mu);
   fChain->SetBranchAddress("GENmass4e", &GENmass4e, &b_GENmass4e);
   fChain->SetBranchAddress("GENmass2e2mu", &GENmass2e2mu, &b_GENmass2e2mu);
   fChain->SetBranchAddress("GENpT4l", &GENpT4l, &b_GENpT4l);
   fChain->SetBranchAddress("GENeta4l", &GENeta4l, &b_GENeta4l);
   fChain->SetBranchAddress("GENrapidity4l", &GENrapidity4l, &b_GENrapidity4l);
   fChain->SetBranchAddress("GENcosTheta1", &GENcosTheta1, &b_GENcosTheta1);
   fChain->SetBranchAddress("GENcosTheta2", &GENcosTheta2, &b_GENcosTheta2);
   fChain->SetBranchAddress("GENcosThetaStar", &GENcosThetaStar, &b_GENcosThetaStar);
   fChain->SetBranchAddress("GENPhi", &GENPhi, &b_GENPhi);
   fChain->SetBranchAddress("GENPhi1", &GENPhi1, &b_GENPhi1);
   fChain->SetBranchAddress("GENMH", &GENMH, &b_GENMH);
   fChain->SetBranchAddress("GENZ_pt", &GENZ_pt, &b_GENZ_pt);
   fChain->SetBranchAddress("GENZ_eta", &GENZ_eta, &b_GENZ_eta);
   fChain->SetBranchAddress("GENZ_phi", &GENZ_phi, &b_GENZ_phi);
   fChain->SetBranchAddress("GENZ_mass", &GENZ_mass, &b_GENZ_mass);
   fChain->SetBranchAddress("GENZ_DaughtersId", &GENZ_DaughtersId, &b_GENZ_DaughtersId);
   fChain->SetBranchAddress("GENZ_MomId", &GENZ_MomId, &b_GENZ_MomId);
   fChain->SetBranchAddress("GENmassZ1", &GENmassZ1, &b_GENmassZ1);
   fChain->SetBranchAddress("GENmassZ2", &GENmassZ2, &b_GENmassZ2);
   fChain->SetBranchAddress("GENpTZ1", &GENpTZ1, &b_GENpTZ1);
   fChain->SetBranchAddress("GENpTZ2", &GENpTZ2, &b_GENpTZ2);
   fChain->SetBranchAddress("GENdPhiZZ", &GENdPhiZZ, &b_GENdPhiZZ);
   fChain->SetBranchAddress("GENmassZZ", &GENmassZZ, &b_GENmassZZ);
   fChain->SetBranchAddress("GENpTZZ", &GENpTZZ, &b_GENpTZZ);
   fChain->SetBranchAddress("GENHmass", &GENHmass, &b_GENHmass);
   fChain->SetBranchAddress("GENjet_pt", &GENjet_pt, &b_GENjet_pt);
   fChain->SetBranchAddress("GENjet_eta", &GENjet_eta, &b_GENjet_eta);
   fChain->SetBranchAddress("GENjet_phi", &GENjet_phi, &b_GENjet_phi);
   fChain->SetBranchAddress("GENjet_mass", &GENjet_mass, &b_GENjet_mass);
   fChain->SetBranchAddress("GENnjets_pt30_eta4p7", &GENnjets_pt30_eta4p7, &b_GENnjets_pt30_eta4p7);
   fChain->SetBranchAddress("GENpt_leadingjet_pt30_eta4p7", &GENpt_leadingjet_pt30_eta4p7, &b_GENpt_leadingjet_pt30_eta4p7);
   fChain->SetBranchAddress("GENabsrapidity_leadingjet_pt30_eta4p7", &GENabsrapidity_leadingjet_pt30_eta4p7, &b_GENabsrapidity_leadingjet_pt30_eta4p7);
   fChain->SetBranchAddress("GENabsdeltarapidity_hleadingjet_pt30_eta4p7", &GENabsdeltarapidity_hleadingjet_pt30_eta4p7, &b_GENabsdeltarapidity_hleadingjet_pt30_eta4p7);
   fChain->SetBranchAddress("lheNj", &lheNj, &b_lheNj);
   fChain->SetBranchAddress("lheNb", &lheNb, &b_lheNb);
   fChain->SetBranchAddress("nGenStatus2bHad", &nGenStatus2bHad, &b_nGenStatus2bHad);
   fChain->SetBranchAddress("me_0plus_JHU", &me_0plus_JHU, &b_me_0plus_JHU);
   fChain->SetBranchAddress("me_qqZZ_MCFM", &me_qqZZ_MCFM, &b_me_qqZZ_MCFM);
   fChain->SetBranchAddress("p0plus_m4l", &p0plus_m4l, &b_p0plus_m4l);
   fChain->SetBranchAddress("bkg_m4l", &bkg_m4l, &b_bkg_m4l);
   fChain->SetBranchAddress("D_bkg_kin", &D_bkg_kin, &b_D_bkg_kin);
   fChain->SetBranchAddress("D_bkg", &D_bkg, &b_D_bkg);
   fChain->SetBranchAddress("Dgg10_VAMCFM", &Dgg10_VAMCFM, &b_Dgg10_VAMCFM);
   fChain->SetBranchAddress("Djet_VAJHU", &Djet_VAJHU, &b_Djet_VAJHU);
   fChain->SetBranchAddress("Djet_VAJHU_jesup", &Djet_VAJHU_jesup, &b_Djet_VAJHU_jesup);
   fChain->SetBranchAddress("Djet_VAJHU_jesdn", &Djet_VAJHU_jesdn, &b_Djet_VAJHU_jesdn);
   fChain->SetBranchAddress("D_g4", &D_g4, &b_D_g4);
}

Bool_t MySelector_UFHZZZ4L::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

#endif // #ifdef MySelector_UFHZZZ4L_cxx
