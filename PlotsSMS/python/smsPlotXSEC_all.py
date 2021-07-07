import ROOT as rt
from array import *
from sms import *
from smsPlotABS_all import *
from ROOT import gROOT, TFile, TTree, TH1D, TH2D, TChain, TGraph2D

# class producing the 2D plot with xsec colors
class smsPlotXSEC_all(smsPlotABS_all):

    def __init__(self, modelname, histo, obsLimits, expLimits, energy, lumi, preliminary, label, signal):
        self.standardDef(modelname, histo, obsLimits, expLimits, energy, lumi, preliminary)
        self.LABEL = label
        self.SIGNAL = signal
        # canvas for the plot
        self.c = rt.TCanvas("cCONT_%s" %label,"cCONT_%s" %label,600,600)
        self.histo = []
        self.histo.append(histo[i]['histogram'] for i in histo)
        # canvas style
        self.setStyle()
        #self.setStyleCOLZ()

    # define the plot canvas
    def setStyleCOLZ(self):        
        # set z axis
        self.histo.GetZaxis().SetLabelFont(42)
        self.histo.GetZaxis().SetTitleFont(42)
        self.histo.GetZaxis().SetLabelSize(0.035)
        self.histo.GetZaxis().SetTitleSize(0.035)
        self.histo.SetMinimum(self.model.Zmin)
        self.histo.SetMaximum(self.model.Zmax)

        # define the palette for z axis
        NRGBs = 5
        NCont = 255
        stops = array("d",[0.00, 0.34, 0.61, 0.84, 1.00])
        red= array("d",[0.50, 0.50, 1.00, 1.00, 1.00])
        green = array("d",[ 0.50, 1.00, 1.00, 0.60, 0.50])
        blue = array("d",[1.00, 1.00, 0.50, 0.40, 0.50])
        rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
        rt.gStyle.SetNumberContours(NCont)
        
        self.c.cd()
        self.histo.Draw("colz")
        
        rt.gPad.Update()
        palette = self.histo.GetListOfFunctions().FindObject("palette")
        palette.SetX1NDC(1.-0.18)
        palette.SetY1NDC(0.14)
        palette.SetX2NDC(1.-0.13)
        palette.SetY2NDC(1.-0.08)
        palette.SetLabelFont(42)
        palette.SetLabelSize(0.035)

    def DrawPaletteLabel(self):
        textCOLZ = rt.TLatex(0.98,0.15,"95% CL upper limit on cross section [pb]")
        textCOLZ.SetNDC()
        #textCOLZ.SetTextAlign(13)
        textCOLZ.SetTextFont(42)
        textCOLZ.SetTextSize(0.045)
        textCOLZ.SetTextAngle(90)
        textCOLZ.Draw()
        self.c.textCOLZ = textCOLZ
            
    def Draw(self):
        self.emptyHisto.GetXaxis().SetRangeUser(self.model.Xmin, self.model.Xmax)
        self.emptyHisto.GetYaxis().SetRangeUser(self.model.Ymin, self.model.Ymax)
        self.emptyHisto.GetZaxis().SetRangeUser(self.model.Zmin, self.model.Zmax)
        self.emptyHisto.Draw()
        #for h in self.histo:
        #    h.Draw("COLZSAME")
        self.DrawLines()
        self.DrawDiagonal()
        self.DrawText()
        self.DrawLegend()
        f = TFile("Limit_scan_all.root", "RECREATE")
        for i in self.SIGNAL:
            for obs in self.OBS[i]['nominal'] :
                obs.SetName(obs.GetName() + "_" + i)
                obs.Write()
            for exp in self.EXP[i]['nominal'] :
                exp.SetName(exp.GetName() + '_' + i)
                exp.Write()
        #self.DrawPaletteLabel()
        
