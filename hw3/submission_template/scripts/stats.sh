#!/bin/bash

test_file="$1"
wc -l $test_file | awk '{ print $1 }'
head -n 1 $test_file
if [ $(wc -l $test_file | awk '{ print $1 }') -lt 10000 ] 
then
	echo Error: "File has less than 10000 lines"
else
	tail -n 10000 $test_file | grep -c 'potus'  
	sed -n '100,200p' < $test_file | grep -c 'fake'

fi




