import pandas as pd
from prettytable import PrettyTable

def gender_combiner(df_voted,df_registered,primary):
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

def gender_combiner_county(df_voted,df_registered,county,primary):
	df_combined = pd.DataFrame()
	df_male = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_male_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	#df_combined['CONGRESSIONAL DISTRICT'] = pd.Series(list('District {}'.format(x) for x in range(1,15)))
	df_combined['MALE'] = ((df_male/df_male_r)*100).round(2)
	df_combined['FEMALE'] = ((df_female/df_female_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL VOTERS'] = (df_voted['TOTAL VOTERS']/df_registered['TOTAL VOTERS']*100).round(2)
	df_combined.to_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted_gender.csv'.format(county))

def race_combiner(df_voted,df_registered,primary):	
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

def race_combiner_county(df_voted,df_registered,county,primary):	
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
	#df_combined['CONGRESSIONAL DISTRICT'] = pd.Series(list('District {}'.format(x) for x in range(1,15)))
	df_combined['ASIAN-PACIFIC'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['LATINO'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AMERICAN'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL VOTERS'] = (df_voted['TOTAL VOTERS']/df_registered['TOTAL VOTERS']*100).round(2)
	df_combined.to_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted_race.csv'.format(county))

def gender_vs_race_precinct(df_voted,df_registered,county,primary):	

	for precinct in df_voted['PRECINCT NAME'].unique():

		df_v = pd.DataFrame(columns=['-','MALE','FEMALE','UNKNOWN'])
		df_voted_precinct = df_voted.loc[df_voted['PRECINCT NAME']==precinct]
		df_registered_precinct = df_registered.loc[df_registered['PRECINCT NAME']==precinct]

		for col,value in zip(df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' MALE')]].columns,df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' MALE')]].iloc[0]):
			col = col.replace(' MALE','')
			if col == 'UNKNOWN':
				df_v.loc[len(df_v)] = [col,value,'',0]
			else:	
				df_v.loc[len(df_v)] = [col,value,'','']
		for col,value in zip(df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' FEMALE')]].columns,df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' FEMALE')]].iloc[0]):
			col = col.replace(' FEMALE','')
			df_v.loc[df_v['-']==col,'FEMALE'] = value
		for col,value in zip(df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' UNKNOWN')]].columns,df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' UNKNOWN')]].iloc[0]):
			if col != 'UNKNOWN':
				col = col.replace(' UNKNOWN','')
			df_v.loc[df_v['-']==col,'UNKNOWN'] = value
		df_v.fillna(0,inplace=True)	

		df_r = pd.DataFrame(columns=['-','MALE','FEMALE','UNKNOWN'])
		for col,value in zip(df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' MALE')]].columns,df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' MALE')]].iloc[0]):
			col = col.replace(' MALE','')
			if col == 'UNKNOWN':
				df_r.loc[len(df_r)] = [col,value,'',0]
			else:	
				df_r.loc[len(df_r)] = [col,value,'','']
		for col,value in zip(df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' FEMALE')]].columns,df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' FEMALE')]].iloc[0]):
			col = col.replace(' FEMALE','')
			df_r.loc[df_r['-']==col,'FEMALE'] = value
		for col,value in zip(df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' UNKNOWN')]].columns,df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' UNKNOWN')]].iloc[0]):
			if col != 'UNKNOWN':
				col = col.replace(' UNKNOWN','')
			df_r.loc[df_r['-']==col,'UNKNOWN'] = value
		df_r.fillna(0,inplace=True)	

		for column in df_v.columns:
			if column != '-':
				df_v[column] = df_v[column].apply(float)

		for column in df_r.columns:
			if column != '-':
				df_r[column] = df_r[column].apply(float)

		df_combined = (df_v.loc[:,df_v.columns!='-'] / df_r.loc[:,df_r.columns!='-']).multiply(100).round(2)
		df_combined.fillna(0,inplace=True)
		df_combined.insert(loc=0,column='-',value=df_v['-'])
		df_combined.to_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_{}_percent_voted.csv'.format(county,precinct.replace('/','-')))

def gender_vs_race_county(df_voted,df_registered,county,primary):	
		
	df_v = pd.DataFrame(columns=['-','MALE','FEMALE','UNKNOWN'])

	for col,value in zip(df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].columns,df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].iloc[0]):
		col = col.replace(' MALE','')
		if col == 'UNKNOWN':
			df_v.loc[len(df_v)] = [col,value,'',0]
		else:	
			df_v.loc[len(df_v)] = [col,value,'','']
	for col,value in zip(df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' FEMALE')]].columns,df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' FEMALE')]].iloc[0]):
		col = col.replace(' FEMALE','')
		df_v.loc[df_v['-']==col,'FEMALE'] = value
	for col,value in zip(df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' UNKNOWN')]].columns,df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' UNKNOWN')]].iloc[0]):
		if col != 'UNKNOWN':
			col = col.replace(' UNKNOWN','')
		df_v.loc[df_v['-']==col,'UNKNOWN'] = value
	df_v.fillna(0,inplace=True)	

	df_r = pd.DataFrame(columns=['-','MALE','FEMALE','UNKNOWN'])
	for col,value in zip(df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].columns,df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].iloc[0]):
		col = col.replace(' MALE','')
		if col == 'UNKNOWN':
			df_r.loc[len(df_r)] = [col,value,'',0]
		else:	
			df_r.loc[len(df_r)] = [col,value,'','']
	for col,value in zip(df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' FEMALE')]].columns,df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' FEMALE')]].iloc[0]):
		col = col.replace(' FEMALE','')
		df_r.loc[df_r['-']==col,'FEMALE'] = value
	for col,value in zip(df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' UNKNOWN')]].columns,df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' UNKNOWN')]].iloc[0]):
		if col != 'UNKNOWN':
			col = col.replace(' UNKNOWN','')
		df_r.loc[df_r['-']==col,'UNKNOWN'] = value
	df_r.fillna(0,inplace=True)	

	for column in df_v.columns:
		if column != '-':
			df_v[column] = df_v[column].apply(float)

	for column in df_r.columns:
		if column != '-':
			df_r[column] = df_r[column].apply(float)

	df_combined = (df_v.loc[:,df_v.columns!='-'] / df_r.loc[:,df_r.columns!='-']).multiply(100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.insert(loc=0,column='-',value=df_v['-'])
	df_combined.to_csv('/Users/sammahle/Downloads/Age_Nov_6/{}_gender_vs_race_percent_voted.csv'.format(county),index=False)

def gender_vs_age_county(df_voted,df_registered,county,primary):	
			
	df_combined = pd.DataFrame()
	df_male = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_male_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_combined['AGE GROUP'] = df_voted['AGE GROUP']
	df_combined['MALE'] = ((df_male/df_male_r)*100).round(2)
	df_combined['FEMALE'] = ((df_female/df_female_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL VOTERS'] = (df_voted['TOTAL VOTERS']/df_registered['TOTAL VOTERS']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Downloads/Age_Nov_6/{}_gender_vs_age_percent_voted.csv'.format(county),index=False)

def race_vs_age_county(df_voted,df_registered,county,primary):	
	
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
	#df_combined['CONGRESSIONAL DISTRICT'] = pd.Series(list('District {}'.format(x) for x in range(1,15)))
	df_combined['ASIAN-PACIFIC'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['LATINO'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AMERICAN'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL VOTERS'] = (df_voted['TOTAL VOTERS']/df_registered['TOTAL VOTERS']*100).round(2)
	df_combined.to_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_race_vs_age_percent_voted_race.csv'.format(county))

def which_table_to_display(x_axis,y_axis,z_axis,district):

	list_of_axis = [x_axis,y_axis]

	ga_counties = ['APPLING', 'ATKINSON', 'BACON', 'BAKER', 'BALDWIN', 'BANKS', 'BARROW', 'BARTOW', 'BEN HILL', 'BERRIEN', 'BIBB', 'BLECKLEY', 'BRANTLEY', 'BROOKS', 'BRYAN', 'BULLOCH', 'BURKE', 'BUTTS', 'CALHOUN', 'CAMDEN', 'CANDLER', 'CARROLL', 'CATOOSA', 'CHARLTON', 'CHATHAM', 'CHATTAHOOCHEE', 'CHATTOOGA', 'CHEROKEE', 'CLARKE', 'CLAY', 'CLAYTON', 'CLINCH', 'COBB', 'COFFEE', 'COLQUITT', 'COLUMBIA', 'COOK', 'COWETA', 'CRAWFORD', 'CRISP', 'DADE', 'DAWSON', 'DECATUR', 'DEKALB', 'DODGE', 'DOOLY', 'DOUGHERTY', 'DOUGLAS', 'EARLY', 'ECHOLS', 'EFFINGHAM', 'ELBERT', 'EMANUEL', 'EVANS', 'FANNIN', 'FAYETTE', 'FLOYD', 'FORSYTH', 'FRANKLIN', 'FULTON', 'GILMER', 'GLASCOCK', 'GLYNN', 'GORDON', 'GRADY', 'GREENE', 'GWINNETT', 'HABERSHAM', 'HALL', 'HANCOCK', 'HARALSON', 'HARRIS', 'HART', 'HEARD', 'HENRY', 'HOUSTON', 'IRWIN', 'JACKSON', 'JASPER', 'JEFF DAVIS', 'JEFFERSON', 'JENKINS', 'JOHNSON', 'JONES', 'LAMAR', 'LANIER', 'LAURENS', 'LEE', 'LIBERTY', 'LINCOLN', 'LONG', 'LOWNDES', 'LUMPKIN', 'MCDUFFIE', 'MCINTOSH', 'MACON', 'MADISON', 'MARION', 'MERIWETHER', 'MILLER', 'MITCHELL', 'MONROE', 'MONTGOMERY', 'MORGAN', 'MURRAY', 'MUSCOGEE', 'NEWTON', 'OCONEE', 'OGLETHORPE', 'PAULDING', 'PEACH', 'PICKENS', 'PIERCE', 'PIKE', 'POLK', 'PULASKI', 'PUTNAM', 'QUITMAN', 'RABUN', 'RANDOLPH', 'RICHMOND', 'ROCKDALE', 'SCHLEY', 'SCREVEN', 'SEMINOLE', 'SPALDING', 'STEPHENS', 'STEWART', 'SUMTER', 'TALBOT', 'TALIAFERRO', 'TATTNALL', 'TAYLOR', 'TELFAIR', 'TERRELL', 'THOMAS', 'TIFT', 'TOOMBS', 'TOWNS', 'TREUTLEN', 'TROUP', 'TURNER', 'TWIGGS', 'UNION', 'UPSON', 'WALKER', 'WALTON', 'WARE', 'WARREN', 'WASHINGTON', 'WAYNE', 'WEBSTER', 'WHEELER', 'WHITE', 'WHITFIELD', 'WILCOX', 'WILKES', 'WILKINSON', 'WORTH']

	"""race_combiner(pd.read_csv('/Users/sammahle/Downloads/Congressional/Congressional_total_voted.csv'),pd.read_csv('/Users/sammahle/Downloads/Congressional/Congressional_total_registered.csv'))
	gender_combiner(pd.read_csv('/Users/sammahle/Downloads/Congressional/Congressional_total_voted.csv'),pd.read_csv('/Users/sammahle/Downloads/Congressional/Congressional_total_registered.csv'))"""
	
	for county in ga_counties:

		if min('TWIGGS',county) != 'TWIGdwelksmgGS':
			gender_vs_race_county(pd.read_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_total_voted.csv'.format(county)),pd.read_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_total_registered.csv'.format(county)),county)
			#race_combiner_county(pd.read_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_total_voted.csv'.format(county)),pd.read_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_total_registered.csv'.format(county)),county)
			#gender_combiner_county(pd.read_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_total_voted.csv'.format(county)),pd.read_csv('/Users/sammahle/Downloads/Precinct_Nov_6/{}_total_registered.csv'.format(county)),county)
			#gender_vs_age_county(pd.read_csv('/Users/sammahle/Downloads/Age_Nov_6/{}_total_voted.csv'.format(county)),pd.read_csv('/Users/sammahle/Downloads/Age_Nov_6/{}_total_registered.csv'.format(county)),county)
			race_vs_age_county(pd.read_csv('/Users/sammahle/Downloads/Age_Nov_6/{}_total_voted.csv'.format(county)),pd.read_csv('/Users/sammahle/Downloads/Age_Nov_6/{}_total_registered.csv'.format(county)),county)


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
		if x_axis == 'Gender and Race' or y_axis == 'Gender and Race':
			csv_file = open('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted.csv','r')
		elif x_axis == 'Gender' or y_axis == 'Gender':
			csv_file = open('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted_gender.csv','r')
		elif x_axis == 'Race' or y_axis == 'Race':
			csv_file = open('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted_race.csv','r')
		elif x_axis == 'Race' or y_axis == 'Race':
			csv_file = open('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted_race.csv','r')
		#within congressional districts or all

	if x_axis == 'Precinct' or y_axis == 'Precinct':
		if x_axis == 'Gender and Race' or y_axis == 'Gender and Race':
			csv_file = open('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted.csv','r')
		elif x_axis == 'Gender' or y_axis == 'Gender':
			csv_file = open('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted_gender.csv','r')
		elif x_axis == 'Race' or y_axis == 'Race':
			csv_file = open('/Users/sammahle/Downloads/Precinct_Nov_6/{}_percent_voted_race.csv','r')

	if 'Precinct' not in list_of_axis and 'County' not in list_of_axis and 'County' not in list_of_axis and 'Statewide' not in list_of_axis:
		if z_axis == 'Statewide':
			if 'Gender' in list_of_axis and 'Race' in list_of_axis:
				pass
			elif 'Age 'in list_of_axis and 'Race' in list_of_axis:
				pass
			elif 'Gender' in list_of_axis and 'Age' in list_of_axis:
				pass	
		if z_axis == 'Congressional':
			if 'Gender' in list_of_axis and 'Race' in list_of_axis:
				pass
				#gender by race
		if z_axis == 'County':
			if 'Gender' in list_of_axis and 'Race' in list_of_axis:
				pass
			elif 'Age 'in list_of_axis and 'Race' in list_of_axis:
				pass
			elif 'Gender' in list_of_axis and 'Age' in list_of_axis:
				pass	
		if z_axis == 'Precinct':
			if 'Gender' in list_of_axis and 'Race' in list_of_axis:
				pass
				#for each precinct
				
	csv_file = csv_file.readlines()
	list_of_lines = []
	x = 0
	for line in csv_file:
		list_of_lines.append(csv_file[x].split(','))
		x += 1

	if len(list_of_lines) == 1:
		list_of_lines = list_of_lines[0]

	zeroeth_element_in_list_of_lines  = list(listt[0] for listt in list_of_lines)
	pt = PrettyTable(zeroeth_element_in_list_of_lines)
	for a in range(1,len(list_of_lines[0])):
		certain_element_in_list_of_lines = list(listt[a] for listt in list_of_lines)
		pt.add_row(certain_element_in_list_of_lines)

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

which_table_to_display('Gender','Congressional','-','-')

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