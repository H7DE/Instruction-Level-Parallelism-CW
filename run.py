#!/usr/bin/python
import commands
import sys
import re
import argparse
import os
import sqlite3
import time
import subprocess
from subprocess import check_output
import binascii
import uuid

db_filename="arch.db"
schema_filename="schema.sql"

fetch_ifqsize = 'fetch:ifqsize'
ruu_size = 'ruu:size'
lsq_size = 'lsq:size'
res_ialu = 'res:ialu'
res_imult ='res:imult'
res_fpalu = 'res:fpalu'
res_fpmult = 'res:fpmult'

decode_width = 'decode:width' #pow2, 1..4>
issue_width = "issue:width"  #pow2 1..4>
issue_wrong_path = "issue:wrongpath" #- false, true
commit_width = "commit:width" #0..16>
mem_width   = "mem:width" #p 1..4>
mem_port   =  "res:memport" #1..4

sim_ipc  ="sim_IPC"
sim_elapsed_time="sim_elapsed_time"
sim_cpi = "sim_CPI"
sim_cycle = "sim_cycle"
def main(flags, problemSize, flagsValue, saveLogFile=False):
	#Create and execute command
	tmpFile = uuid.uuid4().hex + ".tmp"
	cmdString = '/homes/phjk/simplesim-wattch/sim-outorder %s ./SSCA2v2.2/SSCA2 %s 2> %s '%(flags, problemSize, tmpFile)

	#print cmdString
	p = str(commands.getstatusoutput(cmdString)[1])
	res = open(tmpFile, 'r').read()
	print res
	#Parse output
	regex = r'(\w+|\w+.\w+)(\s+)([-+]?\d*\.\d+|\d+)(\s+)(#)'
	results = {}
	for line in res.split("\n"):
		#print line
		match = re.search(regex, line)
		if match:
			results[str(match.group(1))]=float(match.group(3))


	#print results

	os.remove(tmpFile)
	#sys.exit(0)
	#Add results to database
	db_exist = os.path.exists(db_filename)
	with sqlite3.connect(db_filename) as conn:
		with open(schema_filename, 'rt') as f:
			if not db_exist:
				schema = f.read()
				conn.executescript(schema)

			if "total_power_cycle_cc1" in results:
				cursor = conn.cursor()
				energy =  results["total_power_cycle_cc1"]

				print "Total energy:", energy 
				cursor.execute('insert or ignore into simulation values (?,?,?,?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?,?)', (flags, 
					problemSize,
					energy,
					results[fetch_ifqsize],
					results[ruu_size],
					results[lsq_size],
					results[res_ialu],
					results[res_imult],
					results[res_fpalu],
					results[res_fpmult],
			     	results[decode_width],
					results[issue_width],
					results[commit_width],
					results[mem_width],
					results[mem_port],
					results[sim_ipc],
					results[sim_elapsed_time],
					results[sim_cpi],
					results[sim_cycle]
					))
				conn.commit()

	#Save simulation output to bitbucket
	if saveLogFile:
		bitbucketPath='/vol/bitbucket/rh2512/arch/'
		id = "flags="+ "__" + flags +"__"+"size="+ "__" + str(problemSize) + "__"+ "time=" + time.strftime("%d_%m_%Y_%H_%M") + ".log"
		with open(bitbucketPath+id, 'w') as logFile:
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
	main(flags, problemSize, True)

	"""
	parser = argparse.ArgumentParser(description=usage)
	parser.add_argument('-f',help="", required=True)
	parser.add_arguments('-s', help="", require=True)
	args = vars(parser.parse_args())
	print args
	"""
