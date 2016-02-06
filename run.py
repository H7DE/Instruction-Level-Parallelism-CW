#!/usr/bin/python

import commands
import sys
import re
import argparse

def main(flags, problemSize):
    #Create and execute command
    cmdString = '/homes/phjk/simplesim-wattch/sim-outorder %s SSCA2v2.2/SSCA2 %s'%(flags, problemSize)
    res = str(commands.getstatusoutput(cmdString))
     
    #Parse output
    regex = r'(\w+|\w+.\w+)(\s+)([-+]?\d*\.\d+|\d+)(\s+)#'
    
    results = []
    for line in res.split("\\n"):
        print line 
        match = re.search(regex, line)
        if match:
            results.append((match.group(1), match.group(3)))

    print results

if __name__ == "__main__":
    
    usage = "usage: run.py -f <simple_scalar_flags> -s <problemSize>"
    example = "example: python run.py \"-ruu:size 8\" 9"
    helpString = usage + "\n" + example

    if len(sys.argv) <= 1:
        print helpString
        sys.exit(0)

    flags = sys.argv[1]
    problemSize = sys.argv[2]
 
    #print flags, problemSize

    main(flags, problemSize)

    """
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('-f',help="", required=True)
    parser.add_arguments('-s', help="", require=True)
    args = vars(parser.parse_args())
    print args
    """
