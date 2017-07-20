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
            dv_list.append(checkstring(all_rows[i][col_num]))
        dv_value = statistics.mean(dv_list)
        all_rows[i].append(dv_value)

# adds calculated columns to 'pilot_dvs.csv'
with open('pilot.csv', 'rb') as csvfile_r:
	with open('pilot_dvs.csv', 'wb') as csvfile_w:
	    writer = csv.writer(csvfile_w)
	    reader = csv.reader(csvfile_r)
	    all_rows = [row for row in reader]
	    for i in range(0, len(all_rows)):
	    	write_column('Enrollment Intention', [21, 22, 23], all_rows, i)
	    	write_column('Ambient Belonging', [25, 26, 27, 28], all_rows, i)
	    	write_column('Anticipated Success', [29, 30, 31], all_rows, i)
	    	write_column('Fun', [32, 33, 34], all_rows, i)
	    	write_column('Natural Skill', [35, 36, 37], all_rows, i)
	    	write_column('Confidence', [38, 39], all_rows, i)
	    	write_column('Longterm Behavior', [40, 41, 42], all_rows, i)
	    	write_column('Stereotypes', [43, 44, 45], all_rows, i)
	    	write_column('Masculinity', [46, 47, 48], all_rows, i)
	    	write_column('Gender Stereotypes', [49, 50, 51, 52], all_rows, i)
	    writer.writerows(all_rows)


