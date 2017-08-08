import csv
from urlparse import urlparse
import ast
import os
import statistics

# return url's domain
def parse_url(url):
	parsed_uri = urlparse(url)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	return domain

# convert list represented by string to list
def convert_to_list(input_str):
	ret = ast.literal_eval(input_str)
	ret = [n.strip() for n in ret]
	return ret

# each politician is a key in the hash table passed into create_lists(). each hash value is a list of size 10, 
# where each element is a list of =< 44 urls that appeared in the position of the index. 

# add top 10 results for a politician in a specific week to table, indexed by search result location
def create_lists(weeks_top_10_links, politician, table):
	if table.has_key(politician):
		for i in range(min(10, len(weeks_top_10_links))): # not every politician/week had 10 results
			table[politician][i].append(parse_url(weeks_top_10_links[i]))
	else:
		modes_list = [[] for i in range(10)]
		for i in range(min(10, len(weeks_top_10_links))):
			modes_list[i].append(parse_url(weeks_top_10_links[i]))
		table[politician] = modes_list


# table that contains all url's for all politicians.
# each politian is a key, each value is a list of size 10. 
# each element is a list of all url's that have been in the position of the index (ie index[0] means first search result)
urls_table = dict()


# for each csv file, iterate through all politicians and call on create_lists() for each
cwd = os.getcwd()
files = os.listdir(cwd + "/google_data")
csv_files = ["google_data/" + file for file in files if file[-4:]=='.csv']
for file in csv_files:
	with open(file, 'rU') as csvfile_r:
		reader = csv.reader(csvfile_r)
		for row in reader:
			if row[0] != 'Politician Name':		
				urls = convert_to_list(row[2])
				create_lists(urls, row[0], urls_table)



# frequencies is a hash table where each key is a politician, 
# and each value is a list of 10 elements where each element is the highest occuring probability of 
# a website appearing in each of all 10 positions
# (ie the first element will be the highest occuring proportion of a website appearing in the first search result position)
frequencies = dict()
politicians = urls_table.keys()
for politician in politicians:
	url_list = urls_table[politician] # retrieving all url's for politician
	for result_list in url_list: # iterating through each search result position
		if len(result_list) >= 40: # here we exclude any politicans who did not have close to 44 data points
			occurences = dict() # create a hash table to count occurrences of each url
			for url in result_list:
				if occurences.has_key(url):
					val = occurences[url]
					val = val + 1
					occurences[url] = val
				else:
					occurences[url] = 1
			vals = occurences.values() # returns all numeric occurrences of all url's, we disregard the url itself
			total = 0
			curr_max = 0
			for i in range(len(vals)):
				if vals[i] > curr_max:
					curr_max = vals[i] # getting most frequent url count
			total = len(result_list)
			proportion = (1.0 * curr_max) / total
			if frequencies.has_key(politician):
				frequencies[politician].append(proportion)
			else:
				frequencies[politician] = [proportion]

# a list of four hash tables, each hash table corresponding to the WAPs defined below. 
# for each hash table, the keys are the politicians. the values are the number of modes for each politician (for the given WAP).
# the tables' corresponding WAPs are in the same order as the following list WAPs.  
modes_list = [dict(), dict(), dict(), dict()]

WAPs = [0.33, 0.50, 0.66, 0.75]

for i in range(len(WAPs)):
	WAP = WAPs[i]
	modes = modes_list[i]
	for politician in politicians:
		if politician in frequencies: # not all politicians had the right numbers of data, so some were excluded
			freq_list = frequencies[politician]
			count = 0
			for i in freq_list:
				if i >= WAP:
					count = count + 1 # counting the modes
			modes[politician] = count

# calculating average mode counts
avgs = []
for i in range(len(modes_list)):
	avgs.append(statistics.mean(modes_list[i].values()))

print avgs # [6.350282485875706, 3.7655367231638417, 2.031073446327684, 1.612994350282486]


