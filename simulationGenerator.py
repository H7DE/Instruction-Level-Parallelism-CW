import itertools

"""
listOfFlags=['-fetch:ifqsize',  '-ruu:size', '-lsq:size', '-mem:width', '-res:ialu', '-res:imult', '-res:fpalu', '-res:fpmult', '-issue:inorder', '-issue:wrongpath', '-res:memports', '-fetch:mplat', '-issue:width','-bpred']
"""


listOfFlags=[('-fetch:ifqsize', [x for x in range(1, 3)]),
		('-ruu:size', [x for x in range(1, 3)]),
		('-lsq:size', [x for x in range(1, 3)]), 
		('-mem:width',[x for x in range(1, 3)]),
		('-res:ialu',[x for x in range(1, 3)]),
		('-res:imult',[x for x in range(1, 3)]),
		('-res:fpalu',[x for x in range(1, 3)]),
		('-res:fpmult',[x for x in range(1, 3)])
		]


unzipped = map(list, zip(*listOfFlags))

for values in itertools.product(*unzipped[1]):
	commandString = ""
	for i in range(len(listOfFlags)):
		commandString = commandString + " " + listOfFlags[i][0] + " " + str(values[i])
	print commandString


