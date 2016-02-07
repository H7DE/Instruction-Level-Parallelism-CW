import itertools

"""
listOfFlags=['-fetch:ifqsize',  '-ruu:size', '-lsq:size', '-mem:width', '-res:ialu', '-res:imult', '-res:fpalu', '-res:fpmult', '-issue:inorder', '-issue:wrongpath', '-res:memports', '-fetch:mplat', '-issue:width','-bpred']
"""

limit = 2
listOfFlags=[('-fetch:ifqsize', [x for x in range(1, 10)]),
		('-ruu:size', [x**2 for x in range(2, 3)]),
		('-lsq:size', [x for x in range(1, limit)]), 
		('-mem:width',[x*32 for x in range(1, 3)]),
		('-res:ialu', [x for x in range(1, limit)]),
		('-res:imult',[x for x in range(1, limit)]),
		('-res:fpalu',[x for x in range(1, limit)]),
		('-res:fpmult',[x for x in range(1, limit)])
		]

if __name__ == "__main__":
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
				condor.write("arguments   =\"\'%s\'  7\"\n"%(commandString))#flags , problem size
				condor.write("queue 1\n")
