#!/bin/bash
# simple demonstration of the getopts command

while getopts :ab:c opt
do
	case "$opt" in
	a) echo "Found the -a option";;
	b) echo "Found the -b option, with value $OPTARG";;
	c) echo "Found the -c option";;
	*) echo "Unknown option:$opt";;
	esac
done

shift $[ $OPTIND - 1 ]
count=1
for param in "$@"
do
	echo "Parameter $count: $param"
	count=$[ $count + 1 ]
done
