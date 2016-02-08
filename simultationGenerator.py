import itertools
import run

"""
listOfFlags=['-fetch:ifqsize',  '-ruu:size', '-lsq:size', '-mem:width', '-res:ialu', '-res:imult', '-res:fpalu', '-res:fpmult', '-issue:inorder', '-issue:wrongpath', '-res:memports', '-fetch:mplat', '-issue:width','-bpred']
"""

limit = 2
listOfFlags=[('-fetch:ifqsize', [x for x in range(1, 8)]),
		('-ruu:size', [x**2 for x in range(2, 8)]),
		('-lsq:size', [x for x in range(1, 8)]), 
		('-mem:width',[x*32 for x in range(1, 3)]),
		('-res:ialu', [x for x in range(1, 8)]),
		('-res:imult',[x for x in range(1, 8)]),
		('-res:fpalu',[x for x in range(1, 8)]),
		('-res:fpmult',[x for x in range(1, 8)])
		]

#Performs an exhaustive search with all possible parameters of simple scalar
def runSim():
	unzipped = map(list, zip(*listOfFlags))
	for values in itertools.product(*unzipped[1]):
		commandString = ""
		for i in range(len(listOfFlags)):
			commandString = commandString + " " + listOfFlags[i][0] + " " + str(values[i])
			print "Running: ", commandString
			run.main(commandString, 7)	

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
