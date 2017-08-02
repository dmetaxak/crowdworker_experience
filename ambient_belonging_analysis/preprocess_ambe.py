import csv, sys

def process(infile):
	of = open(inputfile.split(".")[0]+"_formatted.csv", 'wt')
	outfile = csv.writer(of)

	cols = ["finished", 