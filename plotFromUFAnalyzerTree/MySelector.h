//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Oct 28 09:48:37 2016 by ROOT version 6.06/01
// from TTree passedEvents/passedEvents
// found on file: /cms/data/store/user/t2/users/dsperka/dsperka/rootfiles_MC80X_20160716_MuCalib/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISpring16MiniAODv2.root
//////////////////////////////////////////////////////////

#ifndef MySelector_h
#define MySelector_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TTreeReader.h>
#include <TTreeReaderValue.h>
#include <TTreeReaderArray.h>

#include "RooWorkspace.h"
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooBreitWigner.h"
// Headers needed by this particular selector
#include <string>

#include <vector>



class MySelector : public TSelector {
public :
   TTreeReader     fReader;  //!the tree reader
   TTree          *fChain = 0;   //!pointer to the analyzed TTree or TChain

   // Readers to access the data (delete the ones you do not need).
/*   TTreeReaderValue<ULong64_t> Run = {fReader, "Run"};
   TTreeReaderValue<ULong64_t> Event = {fReader, "Event"};
   TTreeReaderValue<ULong64_t> LumiSect = {fReader, "LumiSect"};
   TTreeReaderValue<Int_t> nVtx = {fReader, "nVtx"};
   TTreeReaderValue<Int_t> nInt = {fReader, "nInt"};
   TTreeReaderValue<Int_t> finalState = {fReader, "finalState"};
   TTreeReaderValue<string> triggersPassed = {fReader, "triggersPassed"};
   TTreeReaderValue<Bool_t> passedTrig = {fReader, "passedTrig"};
   TTreeReaderValue<Bool_t> passedFullSelection = {fReader, "passedFullSelection"};
   TTreeReaderValue<Bool_t> passedZ4lSelection = {fReader, "passedZ4lSelection"};
   TTreeReaderValue<Bool_t> passedQCDcut = {fReader, "passedQCDcut"};
   TTreeReaderValue<Bool_t> passedZ1LSelection = {fReader, "passedZ1LSelection"};
   TTreeReaderValue<Bool_t> passedZ4lZ1LSelection = {fReader, "passedZ4lZ1LSelection"};
   TTreeReaderValue<Bool_t> passedZ4lZXCRSelection = {fReader, "passedZ4lZXCRSelection"};
   TTreeReaderValue<Bool_t> passedZXCRSelection = {fReader, "passedZXCRSelection"};
   TTreeReaderValue<Int_t> nZXCRFailedLeptons = {fReader, "nZXCRFailedLeptons"};
   TTreeReaderValue<Float_t> genWeight = {fReader, "genWeight"};
   TTreeReaderValue<Float_t> k_ggZZ = {fReader, "k_ggZZ"};
   TTreeReaderValue<Float_t> k_qqZZ_qcd_dPhi = {fReader, "k_qqZZ_qcd_dPhi"};
   TTreeReaderValue<Float_t> k_qqZZ_qcd_M = {fReader, "k_qqZZ_qcd_M"};
   TTreeReaderValue<Float_t> k_qqZZ_qcd_Pt = {fReader, "k_qqZZ_qcd_Pt"};
   TTreeReaderValue<Float_t> k_qqZZ_ewk = {fReader, "k_qqZZ_ewk"};
   TTreeReaderArray<float> pdfWeights = {fReader, "pdfWeights"};
   TTreeReaderArray<int> pdfWeightIDs = {fReader, "pdfWeightIDs"};
   TTreeReaderValue<Float_t> pdfRMSup = {fReader, "pdfRMSup"};
   TTreeReaderValue<Float_t> pdfRMSdown = {fReader, "pdfRMSdown"};
   TTreeReaderValue<Float_t> pdfENVup = {fReader, "pdfENVup"};
   TTreeReaderValue<Float_t> pdfENVdown = {fReader, "pdfENVdown"};
   TTreeReaderValue<Float_t> pileupWeight = {fReader, "pileupWeight"};
   TTreeReaderValue<Float_t> dataMCWeight = {fReader, "dataMCWeight"};
   TTreeReaderValue<Float_t> eventWeight = {fReader, "eventWeight"};
   TTreeReaderValue<Float_t> crossSection = {fReader, "crossSection"};
   TTreeReaderArray<int> lep_id = {fReader, "lep_id"};
   TTreeReaderArray<float> lep_pt = {fReader, "lep_pt"};
   TTreeReaderArray<float> lep_pterr = {fReader, "lep_pterr"};
   TTreeReaderArray<float> lep_pterrold = {fReader, "lep_pterrold"};
   TTreeReaderArray<float> lep_eta = {fReader, "lep_eta"};
   TTreeReaderArray<float> lep_phi = {fReader, "lep_phi"};
   TTreeReaderArray<float> lep_mass = {fReader, "lep_mass"};
   TTreeReaderArray<float> lepFSR_pt = {fReader, "lepFSR_pt"};
   TTreeReaderArray<float> lepFSR_eta = {fReader, "lepFSR_eta"};
   TTreeReaderArray<float> lepFSR_phi = {fReader, "lepFSR_phi"};
   TTreeReaderArray<float> lepFSR_mass = {fReader, "lepFSR_mass"};
   TTreeReaderArray<Int_t> lep_Hindex = {fReader, "lep_Hindex"};
   TTreeReaderArray<int> lep_genindex = {fReader, "lep_genindex"};
   TTreeReaderArray<int> lep_matchedR03_PdgId = {fReader, "lep_matchedR03_PdgId"};
   TTreeReaderArray<int> lep_matchedR03_MomId = {fReader, "lep_matchedR03_MomId"};
   TTreeReaderArray<int> lep_matchedR03_MomMomId = {fReader, "lep_matchedR03_MomMomId"};
   TTreeReaderArray<int> lep_missingHits = {fReader, "lep_missingHits"};
   TTreeReaderArray<float> lep_mva = {fReader, "lep_mva"};
   TTreeReaderArray<int> lep_ecalDriven = {fReader, "lep_ecalDriven"};
   TTreeReaderArray<int> lep_tightId = {fReader, "lep_tightId"};
   TTreeReaderArray<int> lep_tightIdSUS = {fReader, "lep_tightIdSUS"};
   TTreeReaderArray<int> lep_tightIdHiPt = {fReader, "lep_tightIdHiPt"};
   TTreeReaderArray<float> lep_Sip = {fReader, "lep_Sip"};
   TTreeReaderArray<float> lep_IP = {fReader, "lep_IP"};
   TTreeReaderArray<float> lep_isoNH = {fReader, "lep_isoNH"};
   TTreeReaderArray<float> lep_isoCH = {fReader, "lep_isoCH"};
   TTreeReaderArray<float> lep_isoPhot = {fReader, "lep_isoPhot"};
   TTreeReaderArray<float> lep_isoPU = {fReader, "lep_isoPU"};
   TTreeReaderArray<float> lep_isoPUcorr = {fReader, "lep_isoPUcorr"};
   TTreeReaderArray<float> lep_RelIso = {fReader, "lep_RelIso"};
   TTreeReaderArray<float> lep_RelIsoNoFSR = {fReader, "lep_RelIsoNoFSR"};
   TTreeReaderArray<float> lep_MiniIso = {fReader, "lep_MiniIso"};
   TTreeReaderArray<float> lep_ptRatio = {fReader, "lep_ptRatio"};
   TTreeReaderArray<float> lep_ptRel = {fReader, "lep_ptRel"};
   TTreeReaderArray<string> lep_filtersMatched = {fReader, "lep_filtersMatched"};
   TTreeReaderArray<float> lep_dataMC = {fReader, "lep_dataMC"};
   TTreeReaderArray<float> lep_dataMCErr = {fReader, "lep_dataMCErr"};
   TTreeReaderValue<Int_t> nisoleptons = {fReader, "nisoleptons"};
   TTreeReaderValue<Float_t> muRho = {fReader, "muRho"};
   TTreeReaderValue<Float_t> elRho = {fReader, "elRho"};
   TTreeReaderValue<Float_t> pTL1 = {fReader, "pTL1"};
   TTreeReaderValue<Float_t> pTL2 = {fReader, "pTL2"};
   TTreeReaderValue<Float_t> pTL3 = {fReader, "pTL3"};
   TTreeReaderValue<Float_t> pTL4 = {fReader, "pTL4"};
   TTreeReaderValue<Int_t> idL1 = {fReader, "idL1"};
   TTreeReaderValue<Int_t> idL2 = {fReader, "idL2"};
   TTreeReaderValue<Int_t> idL3 = {fReader, "idL3"};
   TTreeReaderValue<Int_t> idL4 = {fReader, "idL4"};
   TTreeReaderValue<Float_t> etaL1 = {fReader, "etaL1"};
   TTreeReaderValue<Float_t> etaL2 = {fReader, "etaL2"};
   TTreeReaderValue<Float_t> etaL3 = {fReader, "etaL3"};
   TTreeReaderValue<Float_t> etaL4 = {fReader, "etaL4"};
   TTreeReaderValue<Float_t> pTL1FSR = {fReader, "pTL1FSR"};
   TTreeReaderValue<Float_t> pTL2FSR = {fReader, "pTL2FSR"};
   TTreeReaderValue<Float_t> pTL3FSR = {fReader, "pTL3FSR"};
   TTreeReaderValue<Float_t> pTL4FSR = {fReader, "pTL4FSR"};
   TTreeReaderArray<int> tau_id = {fReader, "tau_id"};
   TTreeReaderArray<float> tau_pt = {fReader, "tau_pt"};
   TTreeReaderArray<float> tau_eta = {fReader, "tau_eta"};
   TTreeReaderArray<float> tau_phi = {fReader, "tau_phi"};
   TTreeReaderArray<float> tau_mass = {fReader, "tau_mass"};
   TTreeReaderArray<float> pho_pt = {fReader, "pho_pt"};
   TTreeReaderArray<float> pho_eta = {fReader, "pho_eta"};
   TTreeReaderArray<float> pho_phi = {fReader, "pho_phi"};
   TTreeReaderArray<float> H_pt = {fReader, "H_pt"};
   TTreeReaderArray<float> H_eta = {fReader, "H_eta"};
   TTreeReaderArray<float> H_phi = {fReader, "H_phi"};
   TTreeReaderArray<float> H_mass = {fReader, "H_mass"};
   TTreeReaderArray<float> H_noFSR_pt = {fReader, "H_noFSR_pt"};
   TTreeReaderArray<float> H_noFSR_eta = {fReader, "H_noFSR_eta"};
   TTreeReaderArray<float> H_noFSR_phi = {fReader, "H_noFSR_phi"};
   TTreeReaderArray<float> H_noFSR_mass = {fReader, "H_noFSR_mass"};
   TTreeReaderValue<Float_t> mass4l = {fReader, "mass4l"};
   TTreeReaderValue<Float_t> mass4l_noFSR = {fReader, "mass4l_noFSR"};
   TTreeReaderValue<Float_t> mass4lErr = {fReader, "mass4lErr"};
   TTreeReaderValue<Float_t> mass4lREFIT = {fReader, "mass4lREFIT"};
   TTreeReaderValue<Float_t> mass4lErrREFIT = {fReader, "mass4lErrREFIT"};
   TTreeReaderValue<Float_t> massZ1REFIT = {fReader, "massZ1REFIT"};
   TTreeReaderValue<Float_t> massZ2REFIT = {fReader, "massZ2REFIT"};
   TTreeReaderValue<Float_t> mass4mu = {fReader, "mass4mu"};
   TTreeReaderValue<Float_t> mass4e = {fReader, "mass4e"};
   TTreeReaderValue<Float_t> mass2e2mu = {fReader, "mass2e2mu"};
   TTreeReaderValue<Float_t> pT4l = {fReader, "pT4l"};
   TTreeReaderValue<Float_t> eta4l = {fReader, "eta4l"};
   TTreeReaderValue<Float_t> phi4l = {fReader, "phi4l"};
   TTreeReaderValue<Float_t> rapidity4l = {fReader, "rapidity4l"};
   TTreeReaderValue<Float_t> cosTheta1 = {fReader, "cosTheta1"};
   TTreeReaderValue<Float_t> cosTheta2 = {fReader, "cosTheta2"};
   TTreeReaderValue<Float_t> cosThetaStar = {fReader, "cosThetaStar"};
   TTreeReaderValue<Float_t> Phi = {fReader, "Phi"};
   TTreeReaderValue<Float_t> Phi1 = {fReader, "Phi1"};
   TTreeReaderValue<Float_t> mass3l = {fReader, "mass3l"};
   TTreeReaderArray<float> Z_pt = {fReader, "Z_pt"};
   TTreeReaderArray<float> Z_eta = {fReader, "Z_eta"};
   TTreeReaderArray<float> Z_phi = {fReader, "Z_phi"};
   TTreeReaderArray<float> Z_mass = {fReader, "Z_mass"};
   TTreeReaderArray<float> Z_noFSR_pt = {fReader, "Z_noFSR_pt"};
   TTreeReaderArray<float> Z_noFSR_eta = {fReader, "Z_noFSR_eta"};
   TTreeReaderArray<float> Z_noFSR_phi = {fReader, "Z_noFSR_phi"};
   TTreeReaderArray<float> Z_noFSR_mass = {fReader, "Z_noFSR_mass"};
   TTreeReaderArray<Int_t> Z_Hindex = {fReader, "Z_Hindex"};
   TTreeReaderValue<Float_t> massZ1 = {fReader, "massZ1"};
   TTreeReaderValue<Float_t> massZ1_Z1L = {fReader, "massZ1_Z1L"};
   TTreeReaderValue<Float_t> massZ2 = {fReader, "massZ2"};
   TTreeReaderValue<Float_t> pTZ1 = {fReader, "pTZ1"};
   TTreeReaderValue<Float_t> pTZ2 = {fReader, "pTZ2"};
   TTreeReaderValue<Float_t> met = {fReader, "met"};
   TTreeReaderValue<Float_t> met_phi = {fReader, "met_phi"};
   TTreeReaderValue<Float_t> met_jesup = {fReader, "met_jesup"};
   TTreeReaderValue<Float_t> met_phi_jesup = {fReader, "met_phi_jesup"};
   TTreeReaderValue<Float_t> met_jesdn = {fReader, "met_jesdn"};
   TTreeReaderValue<Float_t> met_phi_jesdn = {fReader, "met_phi_jesdn"};
   TTreeReaderValue<Float_t> met_uncenup = {fReader, "met_uncenup"};
   TTreeReaderValue<Float_t> met_phi_uncenup = {fReader, "met_phi_uncenup"};
   TTreeReaderValue<Float_t> met_uncendn = {fReader, "met_uncendn"};
   TTreeReaderValue<Float_t> met_phi_uncendn = {fReader, "met_phi_uncendn"};
   TTreeReaderArray<int> jet_iscleanH4l = {fReader, "jet_iscleanH4l"};
   TTreeReaderArray<float> jet_pt = {fReader, "jet_pt"};
   TTreeReaderArray<float> jet_relpterr = {fReader, "jet_relpterr"};
   TTreeReaderArray<float> jet_eta = {fReader, "jet_eta"};
   TTreeReaderArray<float> jet_phi = {fReader, "jet_phi"};
   TTreeReaderArray<float> jet_phierr = {fReader, "jet_phierr"};
   TTreeReaderArray<float> jet_mass = {fReader, "jet_mass"};
   TTreeReaderArray<int> jet_jesup_iscleanH4l = {fReader, "jet_jesup_iscleanH4l"};
   TTreeReaderArray<float> jet_jesup_pt = {fReader, "jet_jesup_pt"};
   TTreeReaderArray<float> jet_jesup_eta = {fReader, "jet_jesup_eta"};
   TTreeReaderArray<float> jet_jesup_phi = {fReader, "jet_jesup_phi"};
   TTreeReaderArray<float> jet_jesup_mass = {fReader, "jet_jesup_mass"};
   TTreeReaderArray<int> jet_jesdn_iscleanH4l = {fReader, "jet_jesdn_iscleanH4l"};
   TTreeReaderArray<float> jet_jesdn_pt = {fReader, "jet_jesdn_pt"};
   TTreeReaderArray<float> jet_jesdn_eta = {fReader, "jet_jesdn_eta"};
   TTreeReaderArray<float> jet_jesdn_phi = {fReader, "jet_jesdn_phi"};
   TTreeReaderArray<float> jet_jesdn_mass = {fReader, "jet_jesdn_mass"};
   TTreeReaderArray<int> jet_jerup_iscleanH4l = {fReader, "jet_jerup_iscleanH4l"};
   TTreeReaderArray<float> jet_jerup_pt = {fReader, "jet_jerup_pt"};
   TTreeReaderArray<float> jet_jerup_eta = {fReader, "jet_jerup_eta"};
   TTreeReaderArray<float> jet_jerup_phi = {fReader, "jet_jerup_phi"};
   TTreeReaderArray<float> jet_jerup_mass = {fReader, "jet_jerup_mass"};
   TTreeReaderArray<int> jet_jerdn_iscleanH4l = {fReader, "jet_jerdn_iscleanH4l"};
   TTreeReaderArray<float> jet_jerdn_pt = {fReader, "jet_jerdn_pt"};
   TTreeReaderArray<float> jet_jerdn_eta = {fReader, "jet_jerdn_eta"};
   TTreeReaderArray<float> jet_jerdn_phi = {fReader, "jet_jerdn_phi"};
   TTreeReaderArray<float> jet_jerdn_mass = {fReader, "jet_jerdn_mass"};
   TTreeReaderArray<float> jet_pumva = {fReader, "jet_pumva"};
   TTreeReaderArray<float> jet_csvv2 = {fReader, "jet_csvv2"};
   TTreeReaderArray<int> jet_isbtag = {fReader, "jet_isbtag"};
   TTreeReaderArray<int> jet_hadronFlavour = {fReader, "jet_hadronFlavour"};
   TTreeReaderArray<int> jet_partonFlavour = {fReader, "jet_partonFlavour"};
   TTreeReaderArray<float> jet_QGTagger = {fReader, "jet_QGTagger"};
   TTreeReaderArray<float> jet_QGTagger_jesup = {fReader, "jet_QGTagger_jesup"};
   TTreeReaderArray<float> jet_QGTagger_jesdn = {fReader, "jet_QGTagger_jesdn"};
   TTreeReaderArray<float> jet_axis2 = {fReader, "jet_axis2"};
   TTreeReaderArray<float> jet_ptD = {fReader, "jet_ptD"};
   TTreeReaderArray<int> jet_mult = {fReader, "jet_mult"};
   TTreeReaderValue<Int_t> njets_pt30_eta4p7 = {fReader, "njets_pt30_eta4p7"};
   TTreeReaderValue<Int_t> njets_pt30_eta4p7_jesup = {fReader, "njets_pt30_eta4p7_jesup"};
   TTreeReaderValue<Int_t> njets_pt30_eta4p7_jesdn = {fReader, "njets_pt30_eta4p7_jesdn"};
   TTreeReaderValue<Int_t> njets_pt30_eta4p7_jerup = {fReader, "njets_pt30_eta4p7_jerup"};
   TTreeReaderValue<Int_t> njets_pt30_eta4p7_jerdn = {fReader, "njets_pt30_eta4p7_jerdn"};
   TTreeReaderValue<Int_t> nbjets_pt30_eta4p7 = {fReader, "nbjets_pt30_eta4p7"};
   TTreeReaderValue<Int_t> nvjets_pt40_eta2p4 = {fReader, "nvjets_pt40_eta2p4"};
   TTreeReaderValue<Float_t> pt_leadingjet_pt30_eta4p7 = {fReader, "pt_leadingjet_pt30_eta4p7"};
   TTreeReaderValue<Float_t> pt_leadingjet_pt30_eta4p7_jesup = {fReader, "pt_leadingjet_pt30_eta4p7_jesup"};
   TTreeReaderValue<Float_t> pt_leadingjet_pt30_eta4p7_jesdn = {fReader, "pt_leadingjet_pt30_eta4p7_jesdn"};
   TTreeReaderValue<Float_t> pt_leadingjet_pt30_eta4p7_jerup = {fReader, "pt_leadingjet_pt30_eta4p7_jerup"};
   TTreeReaderValue<Float_t> pt_leadingjet_pt30_eta4p7_jerdn = {fReader, "pt_leadingjet_pt30_eta4p7_jerdn"};
   TTreeReaderValue<Float_t> absrapidity_leadingjet_pt30_eta4p7 = {fReader, "absrapidity_leadingjet_pt30_eta4p7"};
   TTreeReaderValue<Float_t> absrapidity_leadingjet_pt30_eta4p7_jesup = {fReader, "absrapidity_leadingjet_pt30_eta4p7_jesup"};
   TTreeReaderValue<Float_t> absrapidity_leadingjet_pt30_eta4p7_jesdn = {fReader, "absrapidity_leadingjet_pt30_eta4p7_jesdn"};
   TTreeReaderValue<Float_t> absrapidity_leadingjet_pt30_eta4p7_jerup = {fReader, "absrapidity_leadingjet_pt30_eta4p7_jerup"};
   TTreeReaderValue<Float_t> absrapidity_leadingjet_pt30_eta4p7_jerdn = {fReader, "absrapidity_leadingjet_pt30_eta4p7_jerdn"};
   TTreeReaderValue<Float_t> absdeltarapidity_hleadingjet_pt30_eta4p7 = {fReader, "absdeltarapidity_hleadingjet_pt30_eta4p7"};
   TTreeReaderValue<Float_t> absdeltarapidity_hleadingjet_pt30_eta4p7_jesup = {fReader, "absdeltarapidity_hleadingjet_pt30_eta4p7_jesup"};
   TTreeReaderValue<Float_t> absdeltarapidity_hleadingjet_pt30_eta4p7_jesdn = {fReader, "absdeltarapidity_hleadingjet_pt30_eta4p7_jesdn"};
   TTreeReaderValue<Float_t> absdeltarapidity_hleadingjet_pt30_eta4p7_jerup = {fReader, "absdeltarapidity_hleadingjet_pt30_eta4p7_jerup"};
   TTreeReaderValue<Float_t> absdeltarapidity_hleadingjet_pt30_eta4p7_jerdn = {fReader, "absdeltarapidity_hleadingjet_pt30_eta4p7_jerdn"};
   TTreeReaderValue<Float_t> DijetMass = {fReader, "DijetMass"};
   TTreeReaderValue<Float_t> DijetDEta = {fReader, "DijetDEta"};
   TTreeReaderValue<Float_t> DijetFisher = {fReader, "DijetFisher"};
   TTreeReaderArray<int> mergedjet_iscleanH4l = {fReader, "mergedjet_iscleanH4l"};
   TTreeReaderArray<float> mergedjet_pt = {fReader, "mergedjet_pt"};
   TTreeReaderArray<float> mergedjet_eta = {fReader, "mergedjet_eta"};
   TTreeReaderArray<float> mergedjet_phi = {fReader, "mergedjet_phi"};
   TTreeReaderArray<float> mergedjet_mass = {fReader, "mergedjet_mass"};
   TTreeReaderArray<float> mergedjet_tau1 = {fReader, "mergedjet_tau1"};
   TTreeReaderArray<float> mergedjet_tau2 = {fReader, "mergedjet_tau2"};
   TTreeReaderArray<float> mergedjet_btag = {fReader, "mergedjet_btag"};
   TTreeReaderArray<float> mergedjet_L1 = {fReader, "mergedjet_L1"};
   TTreeReaderArray<float> mergedjet_softdropmass = {fReader, "mergedjet_softdropmass"};
   TTreeReaderArray<float> mergedjet_prunedmass = {fReader, "mergedjet_prunedmass"};
   TTreeReaderArray<int> mergedjet_nsubjet = {fReader, "mergedjet_nsubjet"};
   TTreeReaderArray<vector<float>> mergedjet_subjet_pt = {fReader, "mergedjet_subjet_pt"};
   TTreeReaderArray<vector<float>> mergedjet_subjet_eta = {fReader, "mergedjet_subjet_eta"};
   TTreeReaderArray<vector<float>> mergedjet_subjet_phi = {fReader, "mergedjet_subjet_phi"};
   TTreeReaderArray<vector<float>> mergedjet_subjet_mass = {fReader, "mergedjet_subjet_mass"};
   TTreeReaderArray<vector<float>> mergedjet_subjet_btag = {fReader, "mergedjet_subjet_btag"};
   TTreeReaderArray<vector<int>> mergedjet_subjet_partonFlavour = {fReader, "mergedjet_subjet_partonFlavour"};
   TTreeReaderArray<vector<int>> mergedjet_subjet_hadronFlavour = {fReader, "mergedjet_subjet_hadronFlavour"};
   TTreeReaderValue<Int_t> nFSRPhotons = {fReader, "nFSRPhotons"};
   TTreeReaderArray<float> allfsrPhotons_dR = {fReader, "allfsrPhotons_dR"};
   TTreeReaderArray<float> allfsrPhotons_iso = {fReader, "allfsrPhotons_iso"};
   TTreeReaderArray<float> allfsrPhotons_pt = {fReader, "allfsrPhotons_pt"};
   TTreeReaderArray<int> fsrPhotons_lepindex = {fReader, "fsrPhotons_lepindex"};
   TTreeReaderArray<float> fsrPhotons_pt = {fReader, "fsrPhotons_pt"};
   TTreeReaderArray<float> fsrPhotons_pterr = {fReader, "fsrPhotons_pterr"};
   TTreeReaderArray<float> fsrPhotons_eta = {fReader, "fsrPhotons_eta"};
   TTreeReaderArray<float> fsrPhotons_phi = {fReader, "fsrPhotons_phi"};
   TTreeReaderArray<float> fsrPhotons_dR = {fReader, "fsrPhotons_dR"};
   TTreeReaderArray<float> fsrPhotons_iso = {fReader, "fsrPhotons_iso"};
   TTreeReaderValue<Float_t> theta12 = {fReader, "theta12"};
   TTreeReaderValue<Float_t> theta13 = {fReader, "theta13"};
   TTreeReaderValue<Float_t> theta14 = {fReader, "theta14"};
   TTreeReaderValue<Float_t> minM3l = {fReader, "minM3l"};
   TTreeReaderValue<Float_t> Z4lmaxP = {fReader, "Z4lmaxP"};
   TTreeReaderValue<Float_t> minDeltR = {fReader, "minDeltR"};
   TTreeReaderValue<Float_t> m3l_soft = {fReader, "m3l_soft"};
   TTreeReaderValue<Float_t> minMass2Lep = {fReader, "minMass2Lep"};
   TTreeReaderValue<Float_t> maxMass2Lep = {fReader, "maxMass2Lep"};
   TTreeReaderValue<Float_t> thetaPhoton = {fReader, "thetaPhoton"};
   TTreeReaderValue<Float_t> thetaPhotonZ = {fReader, "thetaPhotonZ"};
   TTreeReaderValue<Int_t> EventCat = {fReader, "EventCat"};
   TTreeReaderValue<Int_t> GENfinalState = {fReader, "GENfinalState"};
   TTreeReaderValue<Bool_t> passedFiducialSelection = {fReader, "passedFiducialSelection"};
   TTreeReaderArray<float> GENlep_pt = {fReader, "GENlep_pt"};
   TTreeReaderArray<float> GENlep_eta = {fReader, "GENlep_eta"};
   TTreeReaderArray<float> GENlep_phi = {fReader, "GENlep_phi"};
   TTreeReaderArray<float> GENlep_mass = {fReader, "GENlep_mass"};
   TTreeReaderArray<int> GENlep_id = {fReader, "GENlep_id"};
   TTreeReaderArray<int> GENlep_status = {fReader, "GENlep_status"};
   TTreeReaderArray<int> GENlep_MomId = {fReader, "GENlep_MomId"};
   TTreeReaderArray<int> GENlep_MomMomId = {fReader, "GENlep_MomMomId"};
   TTreeReaderArray<Int_t> GENlep_Hindex = {fReader, "GENlep_Hindex"};
   TTreeReaderArray<float> GENlep_isoCH = {fReader, "GENlep_isoCH"};
   TTreeReaderArray<float> GENlep_isoNH = {fReader, "GENlep_isoNH"};
   TTreeReaderArray<float> GENlep_isoPhot = {fReader, "GENlep_isoPhot"};
   TTreeReaderArray<float> GENlep_RelIso = {fReader, "GENlep_RelIso"};
   TTreeReaderArray<float> GENH_pt = {fReader, "GENH_pt"};
   TTreeReaderArray<float> GENH_eta = {fReader, "GENH_eta"};
   TTreeReaderArray<float> GENH_phi = {fReader, "GENH_phi"};
   TTreeReaderArray<float> GENH_mass = {fReader, "GENH_mass"};
   TTreeReaderValue<Float_t> GENmass4l = {fReader, "GENmass4l"};
   TTreeReaderValue<Float_t> GENmass4mu = {fReader, "GENmass4mu"};
   TTreeReaderValue<Float_t> GENmass4e = {fReader, "GENmass4e"};
   TTreeReaderValue<Float_t> GENmass2e2mu = {fReader, "GENmass2e2mu"};
   TTreeReaderValue<Float_t> GENpT4l = {fReader, "GENpT4l"};
   TTreeReaderValue<Float_t> GENeta4l = {fReader, "GENeta4l"};
   TTreeReaderValue<Float_t> GENrapidity4l = {fReader, "GENrapidity4l"};
   TTreeReaderValue<Float_t> GENcosTheta1 = {fReader, "GENcosTheta1"};
   TTreeReaderValue<Float_t> GENcosTheta2 = {fReader, "GENcosTheta2"};
   TTreeReaderValue<Float_t> GENcosThetaStar = {fReader, "GENcosThetaStar"};
   TTreeReaderValue<Float_t> GENPhi = {fReader, "GENPhi"};
   TTreeReaderValue<Float_t> GENPhi1 = {fReader, "GENPhi1"};
   TTreeReaderValue<Float_t> GENMH = {fReader, "GENMH"};
   TTreeReaderArray<float> GENZ_pt = {fReader, "GENZ_pt"};
   TTreeReaderArray<float> GENZ_eta = {fReader, "GENZ_eta"};
   TTreeReaderArray<float> GENZ_phi = {fReader, "GENZ_phi"};
*/ 
   TTreeReaderArray<float> GENZ_mass = {fReader, "GENZ_mass"};
/*
   TTreeReaderArray<int> GENZ_DaughtersId = {fReader, "GENZ_DaughtersId"};
   TTreeReaderArray<int> GENZ_MomId = {fReader, "GENZ_MomId"};
   TTreeReaderValue<Float_t> GENmassZ1 = {fReader, "GENmassZ1"};
   TTreeReaderValue<Float_t> GENmassZ2 = {fReader, "GENmassZ2"};
   TTreeReaderValue<Float_t> GENpTZ1 = {fReader, "GENpTZ1"};
   TTreeReaderValue<Float_t> GENpTZ2 = {fReader, "GENpTZ2"};
   TTreeReaderValue<Float_t> GENdPhiZZ = {fReader, "GENdPhiZZ"};
   TTreeReaderValue<Float_t> GENmassZZ = {fReader, "GENmassZZ"};
   TTreeReaderValue<Float_t> GENpTZZ = {fReader, "GENpTZZ"};
   TTreeReaderValue<Float_t> GENHmass = {fReader, "GENHmass"};
   TTreeReaderArray<float> GENjet_pt = {fReader, "GENjet_pt"};
   TTreeReaderArray<float> GENjet_eta = {fReader, "GENjet_eta"};
   TTreeReaderArray<float> GENjet_phi = {fReader, "GENjet_phi"};
   TTreeReaderArray<float> GENjet_mass = {fReader, "GENjet_mass"};
   TTreeReaderValue<Int_t> GENnjets_pt30_eta4p7 = {fReader, "GENnjets_pt30_eta4p7"};
   TTreeReaderValue<Float_t> GENpt_leadingjet_pt30_eta4p7 = {fReader, "GENpt_leadingjet_pt30_eta4p7"};
   TTreeReaderValue<Float_t> GENabsrapidity_leadingjet_pt30_eta4p7 = {fReader, "GENabsrapidity_leadingjet_pt30_eta4p7"};
   TTreeReaderValue<Float_t> GENabsdeltarapidity_hleadingjet_pt30_eta4p7 = {fReader, "GENabsdeltarapidity_hleadingjet_pt30_eta4p7"};
   TTreeReaderValue<Int_t> lheNj = {fReader, "lheNj"};
   TTreeReaderValue<Int_t> lheNb = {fReader, "lheNb"};
   TTreeReaderValue<Int_t> nGenStatus2bHad = {fReader, "nGenStatus2bHad"};
   TTreeReaderValue<Float_t> me_0plus_JHU = {fReader, "me_0plus_JHU"};
   TTreeReaderValue<Float_t> me_qqZZ_MCFM = {fReader, "me_qqZZ_MCFM"};
   TTreeReaderValue<Float_t> p0plus_m4l = {fReader, "p0plus_m4l"};
   TTreeReaderValue<Float_t> bkg_m4l = {fReader, "bkg_m4l"};
   TTreeReaderValue<Float_t> D_bkg_kin = {fReader, "D_bkg_kin"};
   TTreeReaderValue<Float_t> D_bkg = {fReader, "D_bkg"};
   TTreeReaderValue<Float_t> Dgg10_VAMCFM = {fReader, "Dgg10_VAMCFM"};
   TTreeReaderValue<Float_t> D_g4 = {fReader, "D_g4"};
   TTreeReaderValue<Float_t> D_g1g4 = {fReader, "D_g1g4"};
   TTreeReaderValue<Float_t> D_VBF = {fReader, "D_VBF"};
   TTreeReaderValue<Float_t> D_VBF1j = {fReader, "D_VBF1j"};
   TTreeReaderValue<Float_t> D_HadWH = {fReader, "D_HadWH"};
   TTreeReaderValue<Float_t> D_HadZH = {fReader, "D_HadZH"};
   TTreeReaderValue<Float_t> D_VBF_QG = {fReader, "D_VBF_QG"};
   TTreeReaderValue<Float_t> D_VBF1j_QG = {fReader, "D_VBF1j_QG"};
   TTreeReaderValue<Float_t> D_HadWH_QG = {fReader, "D_HadWH_QG"};
   TTreeReaderValue<Float_t> D_HadZH_QG = {fReader, "D_HadZH_QG"};
*/
   RooWorkspace w;
   RooDataSet* dataset_genzm;
   int n_GENZ_mass_sizeBiggerThan1;
  
   MySelector(TTree * /*tree*/ =0) { 

     w.factory("genzm[80,100]");
     w.factory("BreitWigner::BW(genzm, bwMean[91.2,90,92], bwSigma[2.49,2,3])");
//     w.factory("BreitWigner::BW(bwMean[91.2,90,92], bwSigma[2.49,2,3])");

     dataset_genzm = new RooDataSet("dataset_genzm", "", *w.var("genzm"));

     n_GENZ_mass_sizeBiggerThan1 = 0;
   }
   virtual ~MySelector() { }
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

   ClassDef(MySelector,0);

};

#endif

#ifdef MySelector_cxx
void MySelector::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the reader is initialized.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   fReader.SetTree(tree);
}

Bool_t MySelector::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}


#endif // #ifdef MySelector_cxx
