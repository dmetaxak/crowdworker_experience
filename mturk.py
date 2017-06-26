import csv

# adding all mturk codes from csv file 1 to group 1 (experience level 0 - 50)
group1 = []
with open('mturkexperiencebias/mturk_exp1_0-50.csv', 'rb') as csvfile_1:
	reader = csv.reader(csvfile_1)
	next(reader, None)
	for row in reader:
		group1.append(row[-1])

# adding all mturk codes from csv file 2 to group 2 (experience level 50 - 100)
group2 = []
with open('mturkexperiencebias/mturk_exp2_50-100.csv', 'rb') as csvfile_2:
	reader = csv.reader(csvfile_2)
	next(reader, None)
	for row in reader:
		group2.append(row[-1])


# adding all mturk codes from csv file 3 to group 3 (experience level 100 - 500)
group3 = []
with open('mturkexperiencebias/mturk_exp3_100-500.csv', 'rb') as csvfile_3:
	reader = csv.reader(csvfile_3)
	next(reader, None)
	for row in reader:
		group3.append(row[-1])


# adding all mturk codes from csv file 4 to group 4 (experience level 500 - 1000)
group4 = []
with open('mturkexperiencebias/mturk_exp4_500-1000.csv', 'rb') as csvfile_4:
	reader = csv.reader(csvfile_4)
	next(reader, None)
	for row in reader:
		group4.append(row[-1])


# function for checking if a value is in each group
def findgroup(x):
    	if x in group1:
    		return 1
    	if x in group2:
    		return 2
    	if x in group3:
    		return 3
    	if x in group4:
    		return 4
    	else:
    		return 0

# creates a new csv file and writes original qualtrics file to it; also checks the mturk code using the findgroup function and appends the group number
with open('mturkexperiencebias/qualtrics_experiencedata.csv', 'rb') as csvfile_r:
	with open('mturkexperiencebias/qualtrics_experiencedata_new.csv', 'wb') as csvfile_w:
	    writer = csv.writer(csvfile_w)
	    reader = csv.reader(csvfile_r)
	    all_rows = [row for row in reader]
	    for i in range(0, len(all_rows)):
	    	if i==0:
	    		all_rows[i].append('GroupNumber')
	    	all_rows[i].append(findgroup(all_rows[i][-1]))
	    writer.writerows(all_rows)



