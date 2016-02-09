#!/usr/bin/python

import matplotlib.pyplot as plt
import commands
import math
import uuid
import re
import os
import sys
#flags 
fetch_ifqsize = '-fetch:ifqsize'
ruu_size = '-ruu:size'
lsq_size = '-lsq:size'
res_ialu = '-res:ialu'
res_imult ='-res:imult'
res_fpalu = '-res:fpalu'
res_fpmult = '-res:fpmult'

def compute(flag, _xrange, _id, fileName):
	problemSize = 7
	xVals = []
	yVals = []
	meta = []

	for i in _xrange:
		flags = "%s %d"%(flag, i)
		tmpFile = uuid.uuid4().hex + ".tmp"
		cmdString = '/homes/phjk/simplesim-wattch/sim-outorder %s ./SSCA2v2.2/SSCA2 %s 2> %s '%(flags, problemSize, tmpFile)

		totalEnergy = 0
		noRuns = 1
		#Create and execute command
		for j in range(noRuns):
			p = str(commands.getstatusoutput(cmdString)[1])
			res = open(tmpFile, 'r').read()
			#Parse output
			regex = r'(\w+|\w+.\w+)(\s+)([-+]?\d*\.\d+|\d+)(\s+)(#)'
			results = {}
			for line in res.split("\n"):
				#print line
				match = re.search(regex, line)
				if match:
					results[str(match.group(1))]=float(match.group(3))
			totalEnergy = totalEnergy + results["total_power_cycle_cc1"]
		os.remove(tmpFile)
		xVals.append(i)
		yVals.append(float(totalEnergy)/noRuns)
	with open(fileName, 'w') as log:
		log.write("#Flags=%s"%(flag)+'\n')
		log.write("%s_xVals="%(_id) + str(xVals)+'\n') 
		log.write("%s_yVals="%(_id) + str(yVals)+'\n')
		#log.write("%s_meta="%(_id) + str(results)+'\n')

powOfTwo = [int(math.pow(2,x)) for x in range(9)]
powOfTwo2 = [int(math.pow(2,x)) for x in range(1,9)]
linear   = [x for x in range(1, 9)]
"""
print compute(fetch_ifqsize, powOfTwo, "fetch_ifqsize")
print compute(ruu_size, powOfTwo2, "ruu_size")
print compute(lsq_size, powOfTwo2, "lsq_size")

print compute(res_ialu, linear,"res_ialu")
print compute(res_imult, linear,"res_imult")
print compute(res_fpalu, linear,"res_fpalu")
print compute(res_fpmult, linear,"res_fpmult")
"""

if __name__ == "__main__":
	compute(sys.argv[1], eval(sys.argv[2]), sys.argv[3], sys.argv[4])
"""
scaledX = [math.log(x, 2) for x in xVals]
plt.xlabel("log_2(Number of interger multipliers/dividers")
plt.title("Energy Consumption vs Number of Integer Multipliers/dividers")
plt.ylabel("avg total_power_cycle_cc1")
plt.plot(scaledX, yVals)
plt.show()
"""
