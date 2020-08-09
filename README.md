#Steps for producing datacards and computing limits locally:
1) Set up your conf file (dc_0l_setup.conf) in the Limits directory

2) To produce the datacards, run:
```
python Datacards/python/makeDatacards.py
```
or
```
python Datacards/python/makeDatacards.py <name_of_your.conf>
```
in case you want to run with a different conf file. WARNING: this will take quite a while, so be patient!

3) To run the limits, you need CMSSW_7_1_5 and the HiggsAnalysis/CombinedLimit package (see instructions at the top of Datacards/scripts/runLimits.py) and a separate shell using the corresponding CMSSW area as your CMSSW_BASE. In this shell, from the Limits directory, run:
```
python Datacards/python/runLimits.py
```
or
```
python Datacards/python/runLimits.py -c <name_of_your.conf>
```
if you're running with a different conf file than the default

4) If you've already run step 3) for a given set of datacards, you can print the results (from any shell) with:
```
python Datacards/python/runLimits.py -p [-c <name_of_your.conf>]
```

5) In order to fill a root file with the limit results for all mass points considered (needed for the final plots), run:
```
python Datacards/python/runLimits.py -f [-c <name_of_your.conf>]
```

6) To make the usual SMS exclusion plots, you can then run:
```
python PlotsSMS/python/makeSMSplots.py PlotsSMS/config/T2tt_SUS16005.cfg T2tt
```
which will produce the limit plots in pdf format

Steps for submitting jobs on Condor
Should run everything in CMSSW_10_2_9

## Set up necessary repositories
## Get Higgs Combined
```
cd CMSSW_10_2_9/src
cmsenv
git clone --single-branch --branch SUSYNano19 https://github.com/mkilpatr/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
scramv1 b clean
scramv1 b
```

## Get Combine Harvester
```
cd CMSSW_10_2_9/src
cmsenv
git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester
scram b
```

## Get Limits Repository
```
cd CMSSW_10_2_9/src
cmsenv
git clone -b SUSYNano19  https://github.com/susy2015/Limits.git Limits
```

## Copy Signal JSON from Anna
```
cd Datacards/setup/SUSYNano19/
cp -r /uscms/home/ahenckel/nobackup/TTZ/CMSSW_10_2_9/src/SusyAnaTools/Tools/fastsim_results/SMS_T2tt_fastsim .
cp -r /uscms/home/ahenckel/nobackup/TTZ/CMSSW_10_2_9/src/SusyAnaTools/Tools/fastsim_results/SMS_T1tttt_fastsim .
```

## To make the total JSON files from the individual ones
```
python Datacards/python/mergeJSONFiles.py
```

## Create Datacards
Here the -l is a link the the directory where the signal JSON files and systematics are located: Base: Datacards/setup/SUSYNano19/, -s is the name of the specific sample you want to work with
```
python Datacards/python/writeDatacard_SUSYNano19.py -l SMS_T2tt_fastsim -s T2tt_1000_0
python Datacards/python/runLimits.py -c dc_SUSY19Nano_setup.conf
python Datacards/python/runLimits.py -c dc_SUSY19Nano_setup.conf -f
python PlotsSMS/python/makeSMSplots.py PlotsSMS/config/T2tt_SUS16005.cfg T2tt_test
```

## Create condor submit file
Stored signal files as T2tt_signals.conf and T1tttt_signals.conf
This will create a submit bash script to submitt all of the jobs in the conf file to Condor. It will store the log files in $CMSSW_BASE/src/Limits/{outputdir in eos area}. All of the output files will be stored in your eos area at /store/user/{USER}/13TeV/{outputdir in eos area}/.
An Example command: 
./process.py -p Datacards/python/ -c dc_SUSY19Nano_setup.conf -m runLimits.py -o limits_multi_dry_T2tt -d SMS_T2tt_fastsim -l T2tt_signals.conf -e 15Jun2020_Run2_dev_v6 -b all
```
./process.py -p Datacards/python/ -c dc_SUSY19Nano_setup.conf -m runLimits.py -o {outputdir in eos area} -d {Location of signal files} -l {Signal conf file} -e {eos directory name where signal dir is located} -b {string match to subset of bins to use}
. ./submitall.sh
```
## Plotting
To make a root file with all of the limits you need to change the limit dir in dc_SUSY19Nano_setup_Local.conf to the limit dir from the previous command.
```
python Datacards/python/runLimits.py -c dc_SUSY19Nano_setup_Local.conf -f -e {outputdir in eos area} -a T2tt_signals.conf
python PlotsSMS/python/makeSMSplots.py PlotsSMS/config/T2tt_SUS16005.cfg T2tt_{extension for plot name}
```
