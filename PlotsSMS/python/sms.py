from array import *

class sms():

    def __init__(self, modelname):
        if modelname.find("T2tt") != -1: self.T2tt()
        if modelname.find("T2tb") != -1: self.T2tb()
        if modelname.find("T2bW") != -1: self.T2bW()
        if modelname.find("T2fbd") != -1: self.T2fbd()
        if modelname.find("T2cc") != -1: self.T2cc()
        if modelname.find("T1tttt") != -1: self.T1tttt()
        if modelname.find("T1ttbb") != -1: self.T1ttbb()
        if modelname.find("T1bbbb") != -1: self.T1bbbb()
        if modelname.find("T1qqqq") != -1: self.T1qqqq()
        if modelname.find("T5ttcc") != -1: self.T5ttcc()
        if modelname.find("T5tttt") != -1: self.T5tttt()
        if modelname.find("T2bWC") != -1: self.T2bWC()


    def T2tt(self):
        # model name
        self.modelname = "T2tt"
        # decay chain
        self.label = "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}"
        # scan range to plot
        self.Xmin = 150.
        self.Xmax = 1500.
        self.Ymin = 0.
        self.Ymax = 1000.
        self.Zmin = 0.0001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = True
        self.extraText = False

    def T2tb(self):
        # model name
        self.modelname = "T2tb"
        # decay chain
        self.label = "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b #tilde{#chi}^{#pm}_{1} #rightarrow b W^{#pm} #tilde{#chi}^{0}_{1} or #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}"
        # scan range to plot
        self.Xmin = 200.
        self.Xmax = 1500.
        self.Ymin = 0.
        self.Ymax = 850.
        self.Zmin = 0.001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = True
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = True
        self.extraText = True
        self.extratext1 = "m_{#tilde{#chi}_{1}^{#pm}}-m_{#tilde{#chi}_{1}^{0}} = 5 GeV"
        self.extratext2 = "BR(#tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}) = 50%"

    def T2bW(self):
        # model name
        self.modelname = "T2bW"
        # decay chain
        self.label = "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b #tilde{#chi}^{#pm}_{1}, #tilde{#chi}^{#pm}_{1} #rightarrow W^{#pm} #tilde{#chi}_{1}^{0}";
        # scan range to plot
        self.Xmin = 200.
        self.Xmax = 1400.
        self.Ymin = 0.
        self.Ymax = 850.
        self.Zmin = 0.001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = True
        self.extraText = True
        self.extratext1 = "m_{#tilde{#chi}_{1}^{#pm}} = (m_{#tilde{t}} + m_{#tilde{#chi}_{1}^{0}})/2"
        self.extratext2 = ""

    def T2bWC(self):
        # model name
        self.modelname = "T2bWC"
        # decay chain
        self.label = "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b #tilde{#chi}^{#pm}_{1}, #tilde{#chi}^{#pm}_{1} #rightarrow W^{#pm(*)} #tilde{#chi}_{1}^{0}"
        # scan range to plot
        self.Xmin = 300.
        self.Xmax = 1000.
#         self.Ymin = 300.
#         self.Ymax = 1000.
        self.Ymin = 10.
        self.Ymax = 110.
        self.Zmin = 0.02
        self.Zmax = 1.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
#         self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        self.LSP = "#Deltam( #tilde{t}, #tilde{#chi}_{1}^{0} ) [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.extraText = True
        self.extratext1 = "m_{#tilde{#chi}_{1}^{#pm}} = (m_{#tilde{t}} + m_{#tilde{#chi}_{1}^{0}})/2"
        self.extratext2 = ""
        self.preliminary = "Preliminary"

    def T2fbd(self):
        # model name
        self.modelname = "T2fbd"
        # decay chain
        self.label = "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b f #bar{f}' #tilde{#chi}^{0}_{1}"
        # scan range to plot
        self.Xmin = 300.
        self.Xmax = 750.
#         self.Ymin = 300.
#         self.Ymax = 1000.
        self.Ymin = 10.
        self.Ymax = 107.
        self.Zmin = 0.1
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
#         self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        self.LSP = "#Deltam( #tilde{t}, #tilde{#chi}_{1}^{0} ) [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.extraText = False
        self.preliminary = "Preliminary"

    def T2cc(self):
        # model name
        self.modelname = "T2cc"
        # decay chain
        self.label = "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow c #tilde{#chi}^{0}_{1}"
        # scan range to plot
        self.Xmin = 300.
        self.Xmax = 850.
#         self.Ymin = 200.
#         self.Ymax = 800.
        self.Ymin = 10.
        self.Ymax = 110.
        self.Zmin = 0.001
        self.Zmax = 1000.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
#         self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        self.LSP = "#Deltam( #tilde{t}, #tilde{#chi}_{1}^{0} ) [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.extraText = False
        self.preliminary = "Preliminary"

    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 600.
        self.Xmax = 2500.
        self.Ymin = 0.
        self.Ymax = 2100.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
	self.extraText = False
        
    def T1ttbb(self):
        # model name
        self.modelname = "T1ttbb"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{b} #tilde{#chi}^{#pm}_{1}, #tilde{#chi}^{#pm}_{1} #rightarrow W^{+} #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 800.
        self.Xmax = 2700.
        self.Ymin = 0.
        self.Ymax = 2100.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
	self.extraText = True
        self.extratext1 = "m_{#tilde{#chi}_{1}^{#pm}} = (m_{#tilde{g}} + m_{#tilde{#chi}_{1}^{0}})/2"
        self.extratext2 = ""
        
    def T5ttcc(self):
        # model name
        self.modelname = "T5ttcc"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow #tilde{t} t, #tilde{t} #rightarrow c #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 800.
        self.Xmax = 2400.
        self.Ymin = 0.
        self.Ymax = 2100.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
	self.extraText = True
        self.extratext1 = "m_{#tilde{t}} - m_{#tilde{#chi}_{1}^{0}} = 20 GeV"
        self.extratext2 = ""
        
    def T5tttt(self):
        # model name
        self.modelname = "T5tttt"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow #tilde{t} t, #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 800.
        self.Xmax = 2500.
        self.Ymin = 0.
        self.Ymax = 2100.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
	self.extraText = True
        self.extratext1 = "m_{#tilde{t}} - m_{#tilde{#chi}_{1}^{0}} = 175 GeV"
        self.extratext2 = ""
        
    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} #tilde{#chi}^{0}_{1}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 1950.
        self.Ymin = 0.
        self.Ymax = 1800.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False

    def T1qqqq(self):
        # model name
        self.modelname = "T1qqqq"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 1950.
        self.Ymin = 0.
        self.Ymax = 1600.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
