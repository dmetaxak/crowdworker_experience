import csv
import statistics

import numpy as np
import matplotlib.pyplot as plt

#returns 4 lists of values, only for a single column
def calculate_single_column(col_num):
	g1 = []
	g2 = []
	g3 = []
	g4 = []
	with open('mturkexperiencebias/qualtrics_experiencedata_new.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[6]=='TRUE':
				if row[-1]=='1':
					g1.append(int(row[col_num]))
				if row[-1]=='2':
					g2.append(int(row[col_num]))
				if row[-1]=='3':
					g3.append(int(row[col_num]))
				if row[-1]=='4':
					g4.append(int(row[col_num]))

	return g1, g2, g3, g4		

# returns 4 lists of values, for two columns
def calculate_double_column(an_col_num, sp_col_num, ap_col_num, sn_col_num):
	g1 = []
	g2 = []
	g3 = []
	g4 = []
	with open('mturkexperiencebias/qualtrics_experiencedata_new.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[6]=='TRUE':
				if row[25]=='': # if allison is mom
					a = int(row[ap_col_num])
					s = int(row[sn_col_num])
				else: # if sally is the mom
					a = int(row[an_col_num])
					s = int(row[sp_col_num])
				if row[-1]=='1':
					g1.append(a)
					g1.append(s)
				if row[-1]=='2':
					g2.append(a)
					g2.append(s)
				if row[-1]=='3':
					g3.append(a)
					g3.append(s)
				if row[-1]=='4':
					g4.append(a)
					g4.append(s)

		return g1, g2, g3, g4	

# checks if a value is an invalid int, if so returns -1
def is_number(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return -1

# function for getting lists for late days; some of the late days data could not be converted to proper ints
def calculate_late_days_avg(an_col_num, sp_col_num, ap_col_num, sn_col_num):
	g1 = []
	g2 = []
	g3 = []
	g4 = []
	with open('mturkexperiencebias/qualtrics_experiencedata_new.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[6]=='TRUE':
				if row[25]=='': # if allison is mom
					a = is_number(row[ap_col_num])
					s = is_number(row[sn_col_num])
				else: # if sally is the mom
					a = is_number(row[an_col_num])
					s = is_number(row[sp_col_num])
				if row[-1]=='1':
					if a!=-1:
						g1.append(a)
					if s!=-1:
						g1.append(s)
				if row[-1]=='2':
					if a!=-1:
						g2.append(a)
					if s!=-1:
						g2.append(s)
				if row[-1]=='3':
					if a!=-1:
						g3.append(a)
					if s!=-1:
						g3.append(s)
				if row[-1]=='4':
					if a!=-1:
						g4.append(a)
					if s!=-1:
						g4.append(s)

		return g1, g2, g3, g4


# function for getting lists for late days; some of the late days data could not be converted to proper ints
def calculate_salary_avg(an_col_num, sp_col_num, ap_col_num, sn_col_num):
	g1 = []
	g2 = []
	g3 = []
	g4 = []
	with open('mturkexperiencebias/qualtrics_experiencedata_new.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[6]=='TRUE':
				if row[25]=='': # if allison is mom
					a = is_number(row[ap_col_num])
					s = is_number(row[sn_col_num])
				else: # if sally is the mom
					a = is_number(row[an_col_num])
					s = is_number(row[sp_col_num])
				if row[-1]=='1':
					if a!=-1 and a>999:
						g1.append(a)
					if s!=-1 and s>999:
						g1.append(s)
				if row[-1]=='2':
					if a!=-1 and a>999:
						g2.append(a)
					if s!=-1 and s>999:
						g2.append(s)
				if row[-1]=='3':
					if a!=-1 and a>999:
						g3.append(a)
					if s!=-1 and s>999:
						g3.append(s)
				if row[-1]=='4':
					if a!=-1 and a>999:
						g4.append(a)
					if s!=-1 and s>999:
						g4.append(s)

		return g1, g2, g3, g4

# function for calculating competence and returning 4 lists
def calculate_competence_avg():
	g1 = []
	g2 = []
	g3 = []
	g4 = []
	with open('mturkexperiencebias/qualtrics_experiencedata_new.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[6]=='TRUE':
				if row[25]=="": # if allison is the mom
					allison_competence = (int(row[59]) + int(row[60]) + int(row[61]) + int(row[62]) + int(row[63]) + int(row[64]) + int(row[65]) + int(row[66]))/8.0
					sally_competence = (int(row[76]) + int(row[77]) + int(row[78]) + int(row[79]) + int(row[80]) + int(row[81]) + int(row[82]) + int(row[83]))/8.0
					
				else: # if sally is the mom
					allison_competence = (int(row[25]) + int(row[26]) + int(row[27]) + int(row[28]) + int(row[29]) + int(row[30]) + int(row[31]) + int(row[32]))/8.0 ## should motivation be counted?
					sally_competence = (int(row[42]) + int(row[43]) + int(row[44]) + int(row[45]) + int(row[46]) + int(row[47]) + int(row[48]) + int(row[49]))/8.0
				
				if row[-1]=='1':
					g1.append(allison_competence)
					g1.append(sally_competence)
				if row[-1]=='2':
					g2.append(allison_competence)
					g2.append(sally_competence)
				if row[-1]=='3':
					g3.append(allison_competence)
					g3.append(sally_competence)
				if row[-1]=='4':
					g4.append(allison_competence)
					g4.append(sally_competence)

		return g1, g2, g3, g4

# takes in four lists and returns the means and std's
def stats(g1, g2, g3, g4):
	g1_avg = statistics.mean(g1)
	g2_avg = statistics.mean(g2)
	g3_avg = statistics.mean(g3)
	g4_avg = statistics.mean(g4)

	g1_std = statistics.stdev(g1)
	g2_std = statistics.stdev(g2)
	g3_std = statistics.stdev(g3)
	g4_std = statistics.stdev(g4)

	return g1_avg, g2_avg, g3_avg, g4_avg, g1_std, g2_std, g3_std, g4_std


group1_times, group2_times, group3_times, group4_times = calculate_single_column(5)
group1_times_avg, group2_times_avg, group3_times_avg, group4_times_avg, group1_times_std, group2_times_std, group3_times_std, group4_times_std = stats(group1_times, group2_times, group3_times, group4_times)

group1_commitment, group2_commitment, group3_commitment, group4_commitment = calculate_double_column(34, 51, 68, 85)
group1_commitment_avg, group2_commitment_avg, group3_commitment_avg, group4_commitment_avg, group1_commitment_std, group2_commitment_std, group3_commitment_std, group4_commitment_std = stats(group1_commitment, group2_commitment, group3_commitment, group4_commitment)

group1_late_days, group2_late_days, group3_late_days, group4_late_days = calculate_late_days_avg(37, 54, 71, 88)
group1_late_days_avg, group2_late_days_avg, group3_late_days_avg, group4_late_days_avg, group1_late_days_std, group2_late_days_std, group3_late_days_std, group4_late_days_std = stats(group1_late_days, group2_late_days, group3_late_days, group4_late_days)

group1_percentile, group2_percentile, group3_percentile, group4_percentile = calculate_double_column(36, 53, 70, 87)
group1_percentile_avg, group2_percentile_avg, group3_percentile_avg, group4_percentile_avg, group1_percentile_std, group2_percentile_std, group3_percentile_std, group4_percentile_std = stats(group1_percentile, group2_percentile, group3_percentile, group4_percentile)

# for salary, should we ignore results less than 1k or multiply by 1k?
group1_salary, group2_salary, group3_salary, group4_salary = calculate_salary_avg(38, 55, 72, 89)
group1_salary_avg, group2_salary_avg, group3_salary_avg, group4_salary_avg, group1_salary_std, group2_salary_std, group3_salary_std, group4_salary_std = stats(group1_salary, group2_salary, group3_salary, group4_salary)

group1_management, group2_management, group3_management, group4_management = calculate_double_column(40, 57, 74, 91)
group1_management_avg, group2_management_avg, group3_management_avg, group4_management_avg, group1_management_std, group2_management_std, group3_management_std, group4_management_std = stats(group1_management, group2_management, group3_management, group4_management)

group1_promotion, group2_promotion, group3_promotion, group4_promotion = calculate_double_column(39, 56, 73, 90)
group1_promotion_avg, group2_promotion_avg, group3_promotion_avg, group4_promotion_avg, group1_promotion_std, group2_promotion_std, group3_promotion_std, group4_promotion_std = stats(group1_promotion, group2_promotion, group3_promotion, group4_promotion)

group1_hire, group2_hire, group3_hire, group4_hire = calculate_double_column(41, 58, 75, 92)
group1_hire_avg, group2_hire_avg, group3_hire_avg, group4_hire_avg, group1_hire_std, group2_hire_std, group3_hire_std, group4_hire_std = stats(group1_hire, group2_hire, group3_hire, group4_hire)

group1_competence, group2_competence, group3_competence, group4_competence = calculate_competence_avg()
group1_competence_avg, group2_competence_avg, group3_competence_avg, group4_competence_avg, group1_competence_std, group2_competence_std, group3_competence_std, group4_competence_std = stats(group1_competence, group2_competence, group3_competence, group4_competence)


# takes in means and std's and creates a graph
def create_graph(avg1, avg2, avg3, avg4, std1, std2, std3, std4, title, yaxis, filename):
	N = 4
	means = (avg1, avg2, avg3, avg4)
	stds = (std1, std2, std3, std4)

	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, means, width, color='r', yerr=stds)

	# add some text for labels, title and axes ticks
	ax.set_ylabel(yaxis)
	ax.set_title(title)
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels(('G1', 'G2', 'G3', 'G4'))


	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
	                '%.3f' % height,
	                ha='center', va='bottom')

	autolabel(rects1)
	plt.savefig(filename + '.png')



create_graph(group1_times_avg, group2_times_avg, group3_times_avg, group4_times_avg, group1_times_std, group2_times_std, group3_times_std, group4_times_std, 'Average Duration', 'seconds', 'duration')
create_graph(group1_commitment_avg, group2_commitment_avg, group3_commitment_avg, group4_commitment_avg, group1_commitment_std, group2_commitment_std, group3_commitment_std, group4_commitment_std, 'Average Commitment', '1-7 point scale', 'commitment')
create_graph(group1_late_days_avg, group2_late_days_avg, group3_late_days_avg, group4_late_days_avg, group1_late_days_std, group2_late_days_std, group3_late_days_std, group4_late_days_std, 'Average Late Days', 'days', 'latedays')
create_graph(group1_percentile_avg, group2_percentile_avg, group3_percentile_avg, group4_percentile_avg, group1_percentile_std, group2_percentile_std, group3_percentile_std, group4_percentile_std, 'Average Percentile', '%', 'percentile')
create_graph(group1_salary_avg, group2_salary_avg, group3_salary_avg, group4_salary_avg, group1_salary_std, group2_salary_std, group3_salary_std, group4_salary_std, 'Average Salary', '$', 'salary')
create_graph(group1_management_avg, group2_management_avg, group3_management_avg, group4_management_avg, group1_management_std, group2_management_std, group3_management_std, group4_management_std, 'Average Management', '', 'management')
create_graph(group1_promotion_avg, group2_promotion_avg, group3_promotion_avg, group4_promotion_avg, group1_promotion_std, group2_promotion_std, group3_promotion_std, group4_promotion_std, 'Average Promotion', '', 'promotion')
create_graph(group1_hire_avg, group2_hire_avg, group3_hire_avg, group4_hire_avg, group1_hire_std, group2_hire_std, group3_hire_std, group4_hire_std, 'Average Hiring', '', 'hire')
create_graph(group1_competence_avg, group2_competence_avg, group3_competence_avg, group4_competence_avg, group1_competence_std, group2_competence_std, group3_competence_std, group4_competence_std, 'Average Competence', '1-7 point scale', 'competence')
