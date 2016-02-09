#!/usr/bin/python

import itertools
import run
import sys
import math
"""
listOfFlags=['-fetch:ifqsize',  '-ruu:size', '-lsq:size', '-mem:width', '-res:ialu', '-res:imult', '-res:fpalu', '-res:fpmult', '-issue:inorder', '-issue:wrongpath', '-res:memports', '-fetch:mplat', '-issue:width','-bpred']
"""
bLimit = 2
limit = 8
step = 2
listOfFlags=[('-fetch:ifqsize', [int(math.pow(2, x)) for x in range(bLimit, limit, step)]),
		('-ruu:size', [int(math.pow(2, x)) for x in range(bLimit, 8, step)]),
		('-lsq:size', [int(math.pow(2, x)) for x in range(bLimit, limit, step)]),
		('-res:ialu', [x for x in range(bLimit, limit, step)]),
		('-res:imult',[x for x in range(bLimit, limit, step)]),
		('-res:fpalu',[x for x in range(bLimit, limit, step)]),
		('-res:fpmult',[x for x in range(bLimit, limit, step)])
		]

fetch_ifqsize = '-fetch:ifqsize'
ruu_size = '-ruu:size'
lsq_size = '-lsq:size'
res_ialu = '-res:ialu'
res_imult ='-res:imult'
res_fpalu = '-res:fpalu'
res_fpmult = '-res:fpmult'

#Performs an exhaustive search with all possible parameters of simple scalar
def runSim():
	unzipped = map(list, zip(*listOfFlags))
	setOfParams = set(itertools.product(*unzipped[1]))
	#print list(setOfParams)[0:100]
	#sys.exit(0)
	with open("_condor.job", 'w') as condor:
		condor.write("universe        = vanilla\n")
		condor.write("executable      = ./run.py\n")
		condor.write("output          = /vol/bitbucket/rh2512/arch/uname.$(Process).out\n")
		condor.write("error           = /vol/bitbucket/rh2512/arch/uname.$(Process).err\n")
		condor.write("log             = /vol/bitbucket/rh2512/arch/uname.log\n")
		condor.write("Priority        = high\n") 

		count = 0
		for values in list(setOfParams):
			commandString = ""
			flagsValue = {}
			
			#set flags
			for i in range(len(unzipped[0])):
				flag = unzipped[0][i]
				valueOfFlag = str(values[i])
				commandString = commandString + " " + flag + " " + valueOfFlag

			#Run three simulations for statistical significance	
			for k in range(1, 3):
				#print "Running(%d): "%(k), commandString
				condor.write("arguments = " +"\"\' %s\' \'7' \"\n"%(commandString))
				condor.write("queue 1\n")
				#run.main(commandString, 7, flagsValue)	
				count = count + 1
		print "Num jobs:",count

if __name__ == "__main__":
	runSim()
	"""
	with open("condor.job", 'w') as condor:
		condor.write("universe=vanilla\n")
		condor.write("executable      = ./run.py\n")
		condor.write("output          = tmp/uname.$(Process).out\n")
		condor.write("error           = tmp/uname.$(Process).err\n")
		condor.write("log             = tmp/uname.log\n")
		condor.write("Priority        = high\n") 

		# This specifies what commandline arguments should be passed to the executable.
		unzipped = map(list, zip(*listOfFlags))

		for values in itertools.product(*unzipped[1]):
			commandString = ""
			for i in range(len(listOfFlags)):
				commandString = commandString + " " + listOfFlags[i][0] + " " + str(values[i])
				print "Running: ", commandString
				run.main(commandString, 7)	
				#condor.write("arguments   =\"\'%s\'  7\"\n"%(commandString))#flags , problem size
				#condor.write("queue 1\n")

	 """
