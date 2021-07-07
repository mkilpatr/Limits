#!/bin/bash

#declare -a StringArray=("T2tt" "T2bW" "T2tb" "T2fbd" "T2bWC" "T2cc" "T1tttt" "T1ttbb" "T5ttcc")
#declare -a StringArray=("T2tt" "T2bW" "T2tb" "T2fbd" "T2bWC" "T2cc" "T1tttt" "T1ttbb" "T5ttcc" "t2fbd" "t2bWC" "t2cc" "T2All")
declare -a StringArray=("T2tt" "T2bW" "T2tb" "t2fbd" "t2bWC" "t2cc" "T2All")
#declare -a StringArray=("t2fbd" "t2bWC" "t2cc")
 
# Iterate the string array using for loop
for val in ${StringArray[@]}; do

	loc="$val"
        conf=""
        suffix=""
        if [ "$val" = "t2fbd" ]; then
		loc="T2fbd"
		suffix="replot_"
	elif [ "$val" = "t2cc" ]; then
		loc="T2cc"
		suffix="replot_"
	elif [ "$val" = "t2bWC" ]; then
		loc="T2bWC"
		suffix="replot_"
	fi
        
	if [ "$val" != "T2All" ]; then
		echo python Datacards/python/runLimits.py -c dc_SUSY19Nano_setup_Local.conf -f -e limits_multi_${loc}_081820_UnblindRun2 -a ${loc}_signals${conf}.conf -n ${val}
		python Datacards/python/runLimits.py -c dc_SUSY19Nano_setup_Local.conf -f -e limits_multi_${loc}_081820_UnblindRun2 -a ${loc}_signals${conf}.conf -n ${val}
	fi

	echo python PlotsSMS/python/makeSMSplots.py PlotsSMS/config/${val}_SUS16005.cfg ${val}_v7smooth_AddEdge_${suffix}
	python PlotsSMS/python/makeSMSplots.py PlotsSMS/config/${val}_SUS16005.cfg ${val}_v7smooth_AddEdge_${suffix}

done
