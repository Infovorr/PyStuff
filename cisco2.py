# This script is for configuring the hostnames of Cisco devices en masse,
# Takes two files as input, a cfg file containing the configs of the various Cisco devices, and a csv file containing the 
# the IPs and hostnames of all devices to be configured in the format <IP>,<hostname>.
# The script then returns the config file with the hostnames properly configured.

# WARNING: Be sure to compare the lengths of the modified cfg and original cfg; on extremely rare occasions Python will 
# leave out a newline character.

# Example: python cisco2.py cisco_monitor.cfg cisco_list.csv

import re
import sys

if __name__ == "__main__":
	x = sys.argv
	original = []
	modified = []
	
	f = open(x[1], "r")
	fileLines = f.readlines()
	f.close()
	
	g = open(x[2], "r")
	holder = g.readlines()
	g.close()
	
	for line in holder:
		tempList = line.split(",")
		print(tempList)
		original.append(tempList[0])
		modified.append(tempList[1])
	
	modNum = 0
	for values in original:
		pattern = re.compile("\s*name = " + original[modNum] + "$")
		lineNum = 0
		for line in fileLines:
			if pattern.match(line):
				print("Found a match on line " + str(lineNum + 1))
				fileLines[lineNum] = fileLines[lineNum].rstrip("\n\r")
				fileLines[lineNum] = re.sub("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", modified[modNum], fileLines[lineNum])
				print("Wrote: " + fileLines[lineNum])
			lineNum += 1
		modNum += 1
	
	f = open(x[1], "w")
	for line in fileLines:
		f.write(line)
	f.close()
