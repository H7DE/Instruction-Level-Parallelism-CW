#!/usr/bin/python

import commands
import sys
import re
import argparse
import os
import sqlite3
import time


db_filename="arch.db"
schema_filename="schema.sql"

def main(flags, problemSize, saveLogFile=False):
    #Create and execute command
    cmdString = '/homes/phjk/simplesim-wattch/sim-outorder %s SSCA2v2.2/SSCA2 %s'%(flags, problemSize)
    res = str(commands.getstatusoutput(cmdString))

    #Parse output
    regex = r'(\w+|\w+.\w+)(\s+)([-+]?\d*\.\d+|\d+)(\s+)#'

    results = {}
    for line in res.split("\\n"):
        print line 
        match = re.search(regex, line)
        if match:
            results[match.group(1)]=float(match.group(3))
    print results["total_power"]

    #Add results to database
    db_exist = os.path.exists(db_filename)
    with sqlite3.connect(db_filename) as conn:
        with open(schema_filename, 'rt') as f:
            if not db_exist:
                schema = f.read()
                conn.executescript(schema)

            cursor = conn.cursor()
            cursor.execute('insert or ignore into simulation values (?,?,?)', (flags, problemSize, results["total_power"]))
            conn.commit()
    if saveLogFile:
        id = "flags="+ "<" + flags +">"+ "_"+"size="+ "<" + str(problemSize) + ">"+ "_" + time.strftime("%d_%m_%Y_%H_%M") + ".log"
        print id
        with open(id, 'w') as logFile:
            logFile.write(res)


        #open('/vol/bitbucket/rh2512/arch/')


    #print results

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

    main(flags, problemSize, True)

    """
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('-f',help="", required=True)
    parser.add_arguments('-s', help="", require=True)
    args = vars(parser.parse_args())
    print args
    """
