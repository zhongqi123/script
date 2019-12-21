#!/bin/bash
ip_list=`cat 73.txt`
for ip in ${ip_list}
do
	salt ${ip} cmd.run 'cat /etc/group|grep wheel'>${ip}.txt
	result=`cat ${ip}.txt|awk -F: 'NR==2{print $4}'`
	if [[  ${result} == *"cl-jieru"* ]]
	then
		echo "${ip}     yes">>end.txt
	else
		echo "${ip}     no">>end.txt
	fi
	rm -rvf ${ip}.txt
done