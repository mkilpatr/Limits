import os
import json
import argparse

parser = argparse.ArgumentParser(
        description='Produce or print limits based on existing datacards')
parser.add_argument("-r", "--region", dest="region", default='',
                         help="Search region to use when running the maximum likelihood fit. [Default: Search region with 183]")
args = parser.parse_args()

# json file witll_BkgPred_v2e bkg predictions and signal yields
json_binMaps = ''
if args.region == 'SSR': json_binMaps = 'Datacards/setup/SUSYNano19/dc_BkgPred_BinMaps_SSR_master.json'
else:                    json_binMaps = 'Datacards/setup/SUSYNano19/dc_BkgPred_BinMaps_master.json'
json_lepPred = 'Datacards/setup/SUSYNano19/ll_BkgPred.json'
json_TTZPred = 'Datacards/setup/SUSYNano19/TTZ_pred.json'
json_RarePred = 'Datacards/setup/SUSYNano19/Rare_pred.json'
json_zinvPred = 'Datacards/setup/SUSYNano19/zinv_yields.json'
json_qcdPred = 'Datacards/setup/SUSYNano19/qcd_BkgPred.json'

def write_json(data, filename='Datacards/setup/SUSYNano19/combine_bkgPred.json'):
    with open(filename,'w') as f:
    	json.dump(data, f, indent=2, ensure_ascii=False)

with open(json_binMaps, "a+") as new:
    newData = json.load(new)

with open(json_TTZPred, "r") as ttz, open(json_RarePred, "r") as diboson, open(json_zinvPred, "r") as znunu, open(json_qcdPred, "r") as qcd, open(json_lepPred, "r") as lepcr:
    ttz_insert = json.load(ttz)
    diboson_insert = json.load(diboson)
    znunu_insert = json.load(znunu)
    qcd_insert = json.load(qcd)
    lep_insert = json.load(lepcr)
    newData['yieldsMap']['TTZ'] = {}
    newData['yieldsMap']['Rare'] = {}
    newData['yieldsMap']['TTZ'].update(ttz_insert['yieldsMap'])
    newData['yieldsMap']['Rare'].update(diboson_insert['yieldsMap'])
    newData['yieldsMap'].update(znunu_insert['yieldsMap'])
    newData['yieldsMap'].update(qcd_insert['yieldsMap'])
    newData['yieldsMap'].update(lep_insert['yieldsMap'])
write_json(newData)

