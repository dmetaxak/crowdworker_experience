import csv
import statistics

# checks if strings are equivalent to 7 or 1
def checkstring(string):
	if string[0]=='7':
		return 7
	if string[0]=='1':
		return 1
	else:
		return int(string)

# adds a column
def write_column(variable_name, col_list, all_rows, i):
    if i==0 or i==1 or i==2: 
        all_rows[i].append(variable_name)
    else:
        dv_list = []
        for j in range(0, len(col_list)):
            col_num = col_list[j]
            variable_value = checkstring(all_rows[i][col_num])
            if col_num == 29 or col_num == 33 or col_num == 49: # flips values for AS1, FN2, GS1
            	variable_value = 8 - variable_value
            dv_list.append(variable_value)
        dv_value = statistics.mean(dv_list)
        all_rows[i].append(dv_value)

# adds calculated columns to 'ret.csv'
with open('pilot.csv', 'rb') as csvfile_r:
	with open('ret.csv', 'wb') as csvfile_w:
	    writer = csv.writer(csvfile_w)
	    reader = csv.reader(csvfile_r)
	    all_rows = [row for row in reader]
	    all_rows[0][53] = 'Gender' # renames Q18 header to Gender
	    for i in range(0, len(all_rows)):
	    	write_column('EnrollmentIntention', [21, 22, 23], all_rows, i)
	    	write_column('AmbientBelonging', [25, 26, 27, 28], all_rows, i)
	    	write_column('AnticipatedSuccess', [29, 30, 31], all_rows, i)
	    	write_column('Fun', [32, 33, 34], all_rows, i)
	    	write_column('NaturalSkill', [35, 36, 37], all_rows, i)
	    	write_column('Confidence', [38, 39], all_rows, i)
	    	write_column('LongtermBehavior', [40, 41, 42], all_rows, i)
	    	write_column('Stereotypes', [43, 44, 45], all_rows, i)
	    	write_column('Masculinity', [46, 47, 48], all_rows, i)
	    	write_column('GenderStereotypes', [49, 50, 51, 52], all_rows, i)
	    to_exclude = {1, 2} # excluding the 2nd and 3rd rows
	    all_rows_2 = [element for j, element in enumerate(all_rows) if j not in to_exclude]
	    writer.writerows(all_rows_2)
