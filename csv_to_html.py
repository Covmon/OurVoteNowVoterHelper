import pandas as pd
from prettytable import PrettyTable

def gender_combiner(df_voted,df_registered):
	df_combined = pd.DataFrame()
	df_male = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_male_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_combined['CONGRESSIONAL DISTRICT'] = pd.Series(list('District {}'.format(x) for x in range(1,15)))
	df_combined['MALE'] = ((df_male/df_male_r)*100).round(2)
	df_combined['FEMALE'] = ((df_female/df_female_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL VOTERS'] = (df_voted['TOTAL VOTERS']/df_registered['TOTAL VOTERS']*100).round(2)
	df_combined.to_csv('/Users/sammahle/Downloads/Congressional/Congressional_percent_voted_gender.csv')

def race_combiner(df_voted,df_registered):	
	df_combined = pd.DataFrame()
	df_black = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].sum(axis=1)
	df_white = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_latino = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_asian_pacific = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_native = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_other = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_black_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].sum(axis=1)
	df_white_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_latino_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_asian_pacific_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_native_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_other_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_combined['CONGRESSIONAL DISTRICT'] = pd.Series(list('District {}'.format(x) for x in range(1,15)))
	df_combined['ASIAN-PACIFIC'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['LATINO'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AMERICAN'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL VOTERS'] = (df_voted['TOTAL VOTERS']/df_registered['TOTAL VOTERS']*100).round(2)
	df_combined.to_csv('/Users/sammahle/Downloads/Congressional/Congressional_percent_voted_race.csv')

def which_table_to_display(x_axis,y_axis,z_axis):

	race_combiner(pd.read_csv('/Users/sammahle/Downloads/Congressional/Congressional_total_voted.csv'),pd.read_csv('/Users/sammahle/Downloads/Congressional/Congressional_total_registered.csv'))
	gender_combiner(pd.read_csv('/Users/sammahle/Downloads/Congressional/Congressional_total_voted.csv'),pd.read_csv('/Users/sammahle/Downloads/Congressional/Congressional_total_registered.csv'))

	if x_axis == 'Statewide' or y_axis == 'Statewide':
		pass

	if x_axis == 'Congressional' or y_axis == 'Congressional':
		if x_axis == 'Gender and Race' or y_axis == 'Gender and Race':
			csv_file = open('/Users/sammahle/Downloads/Congressional/Congressional_percent_voted.csv','r')
		elif x_axis == 'Gender' or y_axis == 'Gender':
			csv_file = open('/Users/sammahle/Downloads/Congressional/Congressional_percent_voted_gender.csv','r')
		elif x_axis == 'Race' or y_axis == 'Race':
			csv_file = open('/Users/sammahle/Downloads/Congressional/Congressional_percent_voted_race.csv','r')

	if x_axis == 'County' or y_axis == 'County':
		#within congressional districts or all
		pass
	if x_axis == 'Precinct' or y_axis == 'Precinct':
		pass

	csv_file = csv_file.readlines()
	list_of_lines = []
	x = 0
	for line in csv_file:
		list_of_lines.append(csv_file[x].split(','))
		x += 1
	print list_of_lines
	zeroeth_element_in_list_of_lines  = list(listt[0] for listt in list_of_lines)
	pt = PrettyTable(zeroeth_element_in_list_of_lines)
	for a in range(1,len(list_of_lines[0])):
		certain_element_in_list_of_lines = list(listt[a] for listt in list_of_lines)
		pt.add_row(certain_element_in_list_of_lines)

	print pt

	"""print csv_file
	csv_file = csv_file.readlines()
	print csv_file
	line_1 = csv_file[0]
	line_1 = line_1.split(',')
	line_2 = csv_file[1]
	line_2 = line_2.split(',')
	print line_1
	x = PrettyTable([line_1[0],line_2[0]])
	for a in range(1,len(line_1)):
		x.add_row([line_1[a],line_2[a]])"""
	

	"""html_code = x.get_html_string()
	html_file = open('/Users/sammahle/Desktop/OurVoteNowVoterHelper/voting_stats_html.txt','w')
	html_file = html_file.write(html_code)	


	with open("html.txt", "r") as f1:
	    t1 = f1.readlines()
	with open("voter_stats.html", "r") as f2:
	    t2 = f2.readlines()


	#make sure voter html isn't all of them

	line_to_insert = 13
	for line in t1:
		t2.insert(line_to_insert, line)
		line_to_insert += 1
	 

	with open("file.html", "w") as f2:
	    f2.writelines(t2)"""

which_table_to_display('Gender','Congressional','-')
which_table_to_display('Gender','Congressional','-')



#county always vertical 
#then age 
#last demo	 



"""function postData(input) {
    $.ajax({
        type: "POST",
        url: "/reverse_pca.py",
        data: {x_axis=,y_axis=,z_axis=}
    });
}   """