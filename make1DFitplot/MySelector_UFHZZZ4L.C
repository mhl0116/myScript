#define MySelector_UFHZZZ4L_cxx
// The class definition in MySelector_UFHZZZ4L.h has been generated automatically
// by the ROOT utility TTree::MakeSelector(). This class is derived
// from the ROOT class TSelector. For more information on the TSelector
// framework see $ROOTSYS/README/README.SELECTOR or the ROOT User Manual.

// The following methods are defined in this file:
//    Begin():        called every time a loop on the tree starts,
//                    a convenient place to create your histograms.
//    SlaveBegin():   called after Begin(), when on PROOF called only on the
//                    slave servers.
//    Process():      called for each event, in this function you decide what
//                    to read and fill your histograms.
//    SlaveTerminate: called at the end of the loop on the tree, when on PROOF
//                    called only on the slave servers.
//    Terminate():    called at the end of the loop on the tree,
//                    a convenient place to draw/fit your histograms.
//
// To use this file, try the following session on your Tree T:
//
// root> T->Process("MySelector_UFHZZZ4L.C")
// root> T->Process("MySelector_UFHZZZ4L.C","some options")
// root> T->Process("MySelector_UFHZZZ4L.C+")
//

#include "MySelector_UFHZZZ4L.h"
#include <TH2.h>
#include <TStyle.h>


void MySelector_UFHZZZ4L::Begin(TTree * /*tree*/)
{
   // The Begin() function is called at the start of the query.
   // When running with PROOF Begin() is only called on the client.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

   TH1F* pTPull_IF_genpT_5_10_FI_4mu = new TH1F("pTPull_IF_genpT_5_10_FI_4mu", "", 100, -3, 3);
   TH1F* pTPull_IF_genpT_10_20_FI_4mu = new TH1F("pTPull_IF_genpT_10_20_FI_4mu", "", 100, -3, 3);
   TH1F* pTPull_IF_genpT_20_30_FI_4mu = new TH1F("pTPull_IF_genpT_20_30_FI_4mu", "", 100, -3, 3);
   TH1F* pTPull_IF_genpT_30_40_FI_4mu = new TH1F("pTPull_IF_genpT_30_40_FI_4mu", "", 100, -3, 3);
   TH1F* pTPull_IF_genpT_40_50_FI_4mu = new TH1F("pTPull_IF_genpT_40_50_FI_4mu", "", 100, -3, 3);

}

void MySelector_UFHZZZ4L::SlaveBegin(TTree * /*tree*/)
{
   // The SlaveBegin() function is called after the Begin() function.
   // When running with PROOF SlaveBegin() is called on each slave server.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

}

Bool_t MySelector_UFHZZZ4L::Process(Long64_t entry)
{
   // The Process() function is called for each entry in the tree (or possibly
   // keyed object in the case of PROOF) to be processed. The entry argument
   // specifies which entry in the currently loaded tree is to be processed.
   // It can be passed to either MySelector_UFHZZZ4L::GetEntry() or TBranch::GetEntry()
   // to read either all or the required parts of the data. When processing
   // keyed objects with PROOF, the object is already loaded and is available
   // via the fObject pointer.
   //
   // This function should contain the "body" of the analysis. It can contain
   // simple or elaborate selection criteria, run algorithms on the data
   // of the event and typically fill histograms.
   //
   // The processing can be stopped by calling Abort().
   //
   // Use fStatus to set the return value of TTree::Process().
   //
   // The return value is currently not used.

   if (*finalState != 1 || !(passedFullSelection) ) return kTRUE;

   cout << "finalState: " << *finalState << endl;

   for (int i = 0; i < 4; i++) {

       lepIndex = (*lep_Hindex)[i];
       pT_reco = (*lep_pt)[lepIndex];
       pTErr = (*lep_pterr)[lepIndex];

       genIndex = (*lep_genindex)[lepIndex];
       pT_gen = (*GENlep_pt)[genIndex];

       if (pT_gen > 5 && pT_gen < 10) pTPull_IF_genpT_5_10_FI_4mu->Fill((pT_reco-pT_gen)/pTErr);
       if (pT_gen > 10 && pT_gen < 20) pTPull_IF_genpT_10_20_FI_4mu->Fill((pT_reco-pT_gen)/pTErr);
       if (pT_gen > 20 && pT_gen < 30) pTPull_IF_genpT_20_30_FI_4mu->Fill((pT_reco-pT_gen)/pTErr);
       if (pT_gen > 30 && pT_gen < 40) pTPull_IF_genpT_30_40_FI_4mu->Fill((pT_reco-pT_gen)/pTErr);
       if (pT_gen > 40 && pT_gen < 50) pTPull_IF_genpT_40_50_FI_4mu->Fill((pT_reco-pT_gen)/pTErr);

   } 

   return kTRUE;
}

void MySelector_UFHZZZ4L::SlaveTerminate()
{
   // The SlaveTerminate() function is called after all entries or objects
   // have been processed. When running with PROOF SlaveTerminate() is called
   // on each slave server.

}

void MySelector_UFHZZZ4L::Terminate()
{
   // The Terminate() function is the last function to be called during
   // a query. It always runs on the client, it can be used to present
   // the results graphically or save the results to file.

   RooWorkspace* w = new RooWorkspace('w');
   w->factory("DoubleCB::doubleCB_pTPull(pTPull[0,-3,3], meanDCB[-1,1], sigmaDCB[1,0,10],
                                         alphaDCB[1.1,0,50], nDCB[1,0,50], alpha2[1.1,0,50], n2[1,0,50])");

   RooDataHist* dataHist_IF_genpT_5_10_FI_4mu = new RooDataHist("d1","",RooArgList(w->var("pTPull")),*pTPull_IF_genpT_5_10_FI_4mu,1);
   RooDataHist* dataHist_IF_genpT_10_20_FI_4mu = new RooDataHist("d2","",RooArgList(w->var("pTPull")),*pTPull_IF_genpT_10_20_FI_4mu,1);
   RooDataHist* dataHist_IF_genpT_20_30_FI_4mu = new RooDataHist("d3","",RooArgList(w->var("pTPull")),*pTPull_IF_genpT_20_30_FI_4mu,1);
   RooDataHist* dataHist_IF_genpT_30_40_FI_4mu = new RooDataHist("d4","",RooArgList(w->var("pTPull")),*pTPull_IF_genpT_30_40_FI_4mu,1);
   RooDataHist* dataHist_IF_genpT_40_50_FI_4mu = new RooDataHist("d5","",RooArgList(w->var("pTPull")),*pTPull_IF_genpT_40_50_FI_4mu,1);

   pTPullFrame_1 = w->var("pTPull").frame();
   pTPullFrame_2 = w->var("pTPull").frame();
   pTPullFrame_3 = w->var("pTPull").frame();
   pTPullFrame_4 = w->var("pTPull").frame();
   pTPullFrame_5 = w->var("pTPull").frame();

   

}
