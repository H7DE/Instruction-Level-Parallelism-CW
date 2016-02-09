import matplotlib.pyplot as plt
import commands
import math
import uuid
import re

def compute():
    problemSize = 6
    
    xVals = []
    yVals = []
    
    for i in [2, 4, 8]:
        
        flags = "-res:imult %d"%(i)
        tmpFile = uuid.uuid4().hex + ".tmp"
        
        cmdString = '/homes/phjk/simplesim-wattch/sim-outorder %s ./SSCA2v2.2/SSCA2 %s 2> %s '%(flags, problemSize, tmpFile)
        print cmdString
        
        avgEnergy = 0
        noRuns = 3
        #Create and execute command
        for j in range(noRuns):
            p = str(commands.getstatusoutput(cmdString)[1])
                res = open(tmpFile, 'r').read()
                #print res
                #Parse output
                regex = r'(\w+|\w+.\w+)(\s+)([-+]?\d*\.\d+|\d+)(\s+)(#)'
                results = {}
                for line in res.split("\n"):
                    #print line
                    match = re.search(regex, line)
                    if match:
                        results[str(match.group(1))]=float(match.group(3))
            avgEnergy = avgEnergy + results["total_power_cycle_cc1"]

    xVals.append(i)
    yVals.append(float(avgEnergy)/noRuns)

    scaledX = [math.log(x, 2) for x in xVals]
    plt.xlabel("log_2(Number of interger multipliers/dividers")
    plt.title("Energy Consumption vs Number of Integer Multipliers/dividers")
    plt.ylabel("avg total_power_cycle_cc1")
    plt.plot(scaledX, yVals)
    plt.show()

compute()