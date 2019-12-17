double Addprop(double dx, double dy){
  return sqrt(dx*dx+dy*dy);
}

void ume(double ac1cut=20){
  TFile *file0 = new TFile("survival2.root");
  TTree *tree = (TTree *) file0->Get("tree");

  TH1D *h, *h1[4];
  for(int i=0; i<4; i++){
    h1[i]=new TH1D(Form("h1[%d]", i), "", 400, -20, 20);
  }

  TCut ccut1,ccut2,ccut3,ccut4,ccut5,ccut6;
  ccut1="ctime[0]>=11 && ctime[0]<=13";
  ccut2="ctime[0]>=-9 && ctime[0]<=-7";
  ccut3="ctime[0]>=-11 && ctime[0]<=-9";
  ccut4="ctime[0]>=-13 && ctime[0]<=-11";
//  ccut5="ctime[0]>=-15 && ctime[0]<=-13";

  TCut cut1;
  cut1 ="R.a2.asum_c>4&&R.a2.asum_c<10";

//  tree->Draw("ctime[0]", cut1);
  tree->Project("h1[0]","ctime[0]-12", ccut1&&cut1);
  tree->Project("h1[1]","ctime[0]+8" , ccut2&&cut1);
  tree->Project("h1[2]","ctime[0]+10", ccut3&&cut1);
  tree->Project("h1[3]","ctime[0]+12", ccut4&&cut1);
 // tree->Project("h1[4]","ctime[0]+14", ccut5&&cut1);

  TList *l = new TList;
  for(int i=0; i<4; i++) l->Add(h1[i]);

//  TCanvas *c1=new TCanvas("c1", "",  1000, 1000);
  TH1D *h4 = new TH1D("h4","title",400,-20,20);
  h4->Merge(l);
//  h4->Draw("");

  int min, max;
  for(int i=1; i<=400; i++){
//    printf("binnum=%d, binv=%lf\n", i, h4->GetBinContent(i));
    if(h4->GetBinContent(i)>0){
      min=i;
      max=i+20-1;
      break;
    }
  }

  printf("min=%d and max=%d\n", min, max);

  TH1D *h5 = new TH1D("h5","title",400,-20,20);
  double hoge;

  for(int i=min; i<=max; i++){
    hoge=h4->GetBinContent(i);
    hoge=sqrt(hoge)/4;
    h5->SetBinContent(i, h4->GetBinContent(i)/4);
    h5->SetBinError(i, hoge);

    for(int j=1; j<=7; j++){
      h5->SetBinContent(i-20*j, h4->GetBinContent(i)/4);
      h5->SetBinError(i-20*j, hoge);
      h5->SetBinContent(i+20*j, h4->GetBinContent(i)/4);
      h5->SetBinError(i+20*j, hoge);
    }
  }

  TCanvas *c2=new TCanvas("c2", " ", 1000, 1000);
  tree->Draw("ctime[0]>>hsig(400, -20, 20)", cut1);
  TH1D *hsig = (TH1D*)gROOT ->FindObject("hsig");
  h5->SetLineColor(3);
  h5->Draw("same");

  TCanvas *c3=new TCanvas("c3", " ", 1000, 1000);
  TH1D* hre=new TH1D("hre", "",400, -20, 20);
  hre->Add(hsig, h5, 1, -1);
  hre->Draw();

  TCanvas* c4=new TCanvas("c4", "", 1000, 1000);
  TH1D* hnew=new TH1D("hnew", "",400, -20, 20);
  int sig, bg;
  for(int i=1; i<=400; i++){
    sig=hsig->GetBinContent(i);
    bg=h5->GetBinContent(i);

    hnew->SetBinContent(i, sig-bg);
    hnew->SetBinError(i, Addprop(sqrt(h4->GetBinContent(i))/4, sqrt(hsig->GetBinContent(i))));
  }
  hnew->Draw();
  hre->SetLineColor(3);
  hre->Draw("same");

//  TCanvas* c5=new TCanvas("c5", "", 1000, 1000);
//  hre->Draw();

  TF1 *f=new TF1("fit", "[0]*exp(-0.5*((x-[1])/[2])*((x-[1])/[2]))+[3]*exp(-0.5*((x-[4])/[5])*((x-[4])/[5]))");
  f->SetParameter(0, 190);
  f->SetParameter(1, -4);
  f->SetParameter(2, -1);
  f->SetParameter(3, 75);
  f->SetParameter(4, -1);
  f->SetParameter(5, 1);
  hre->Fit(f);

  TF1 *f1=new TF1("f1", "[0]*exp(-0.5*((x-[1])/[2])*((x-[1])/[2]))", -20, 20);
  f1->SetParameter(0, f->GetParameter(0));
  f1->SetParameter(1, f->GetParameter(1));
  f1->SetParameter(2, f->GetParameter(2));

  f1->SetLineColor(4);
  f1->Draw("");
  f->SetNpx(3000);
  f1->SetNpx(3000);
  double areaf1=f1->Integral(-1, 1.);
  printf("%lf\n", areaf1/(40./400.));

//  TCanvas *c5=new TCanvas("c5", "", 600, 600);
//  TH1D *hcon=new TH1D("hcon", "", 400, -20, 20);
//  hcon->Draw();
//  TF1 *f2=new TF1("f2", "[0]*exp(-0.5*((x-[1])/[2])*((x-[1])/[2]))", -20, 20);
//  f2->SetParameter(0, f->GetParameter(0));
//  f2->SetParameter(1, f->GetParameter(1));
//  f2->SetParameter(2, f->GetParameter(2));
//  f2->Draw("same");

//  double area_picon=Integral(-1., 1.);
//  cout << area_picon <<endl;
}
