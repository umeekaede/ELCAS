
void q1(){
  TF1 *f1=new TF1("upsc", "15", -10, 10);
  TF1 *f2=new TF1("downsc", "-15", -10, 10);
  f1->Draw();
  f2->Draw("same");
}