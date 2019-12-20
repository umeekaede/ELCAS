/*
  mkroot.cc
  Toshi Gogami
*/

void mkroot(){
  char name[500];
  char fname[500];
  char ofname[500];
  sprintf(name,"test9");
  sprintf(fname,"%s.dat",name);
  sprintf(ofname,"%s.root",name);
  ifstream* ifs = new ifstream(fname);
  double a1, a2;
  double t1, t2;

  TFile* fnew = new TFile(ofname,"recreate");
  TTree* tnew = new TTree("tree","Data for ELCAS 2019");
  tnew->Branch("adc1",&a1,"adc1/D");
  tnew->Branch("adc2",&a2,"adc2/D");
  //tnew->Branch("a2",&a2,"a2/D");
  tnew->Branch("time1",&t1,"time1/D");
  tnew->Branch("time2",&t2,"time2/D");

  while (!ifs->eof()){
    *ifs >> a1 >> a2 >> t1 >> t2;
    cout << " " << a1 << " " << a2 << " " << t1 << " " << t2 << endl;
    if(a1!=0 && a2!=0){
      tnew->Fill();
    }
  }
  tnew->Write();
  fnew->Close();
}
