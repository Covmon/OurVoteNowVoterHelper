from prettytable import PrettyTable

def which_table_to_display(x_axis,y_axis,z_axis):

	csv_file = open('/Users/sammahle/Downloads/Congressional/tr.csv','r')
	csv_file = csv_file.readlines()
	line_1 = csv_file[0]
	line_1 = line_1.split(',')
	line_2 = csv_file[1]
	line_2 = line_2.split(',')
	print line_1
	x = PrettyTable([line_1[0],line_2[0]])
	for a in range(1,len(line_1)):
		x.add_row([line_1[a],line_2[a]])
	html_code = x.get_html_string()
	html_file = open('/Users/sammahle/Desktop/OurVoteNowVoterHelper/html.txt','w')
	html_file = html_file.write(html_code)	


	with open("html.txt", "r") as f1:
	    t1 = f1.readlines()
	with open("file.html", "r") as f2:
	    t2 = f2.readlines()

	line_to_insert = 13
	for line in t1:
		t2.insert(line_to_insert, line)
		line_to_insert += 1
	 

	with open("file.html", "w") as f2:
	    f2.writelines(t2)

#county always vertical 
#then age 
#last demo	    