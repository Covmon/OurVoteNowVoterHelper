import pandas as pd
import os
from prettytable import PrettyTable
import cgi
import json
parameters = cgi.FieldStorage()

def gender_combiner_congressional(year,election_type,df_voted,df_registered,primary):
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
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_vs_gender_percent_voted.csv'.format(year,election_type))

def gender_combiner_county(year,election_type,df_voted,df_registered,county,primary):
	df_combined = pd.DataFrame()
	df_male = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_male_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_combined['PRECINCT NAME'] = df_voted['PRECINCT NAME']
	df_combined['MALE'] = ((df_male/df_male_r)*100).round(2)
	df_combined['FEMALE'] = ((df_female/df_female_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_vs_gender_percent_voted.csv'.format(year,election_type,county))

def gender_combiner_statewide(year,election_type,df_voted,df_registered,county,primary):
	df_combined = pd.DataFrame()
	df_male = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_male_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_combined['MALE'] = ((df_male/df_male_r)*100).round(2)
	df_combined['FEMALE'] = ((df_female/df_female_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Counties_vs_gender_percent_voted.csv'.format(year,election_type))

def race_combiner_congressional(year,election_type,df_voted,df_registered,primary):	
	df_combined = pd.DataFrame()
	df_black = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('BLACK')]].sum(axis=1)
	df_white = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('WHITE')]].sum(axis=1)
	df_latino = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('HISP')]].sum(axis=1)
	df_asian_pacific = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('ASIA')]].sum(axis=1)
	df_native = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('NATIVE')]].sum(axis=1)
	df_other = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('OTHER')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('UNKNOWN')]].sum(axis=1)
	df_black_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('BLACK')]].sum(axis=1)
	df_white_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('WHITE')]].sum(axis=1)
	df_latino_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('HISP')]].sum(axis=1)
	df_asian_pacific_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('ASIA')]].sum(axis=1)
	df_native_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('NATIVE')]].sum(axis=1)
	df_other_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('OTHER')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('UNKNOWN')]].sum(axis=1)
	df_combined['CONGRESSIONAL DISTRICT'] = pd.Series(list('District {}'.format(x) for x in range(1,15)))
	df_combined['ASIA-PI'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['HISP-LT'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AMERICAN'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_vs_race_percent_voted.csv'.format(year,election_type))

def race_combiner_county(year,election_type,df_voted,df_registered,county,primary):	
	df_combined = pd.DataFrame()
	df_black = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('BLACK')]].sum(axis=1)
	df_white = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('WHITE')]].sum(axis=1)
	df_latino = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('LATINO')]].sum(axis=1)
	df_asian_pacific = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('ASIAN')]].sum(axis=1)
	df_native = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('NATIVE')]].sum(axis=1)
	df_other = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('OTHER')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('UNKNOWN')]].sum(axis=1)
	df_black_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('BLACK')]].sum(axis=1)
	df_white_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('WHITE')]].sum(axis=1)
	df_latino_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('LATINO')]].sum(axis=1)
	df_asian_pacific_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('ASIAN')]].sum(axis=1)
	df_native_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('NATIVE')]].sum(axis=1)
	df_other_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('OTHER')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('UNKNOWN')]].sum(axis=1)
	df_combined['PRECINCT NAME'] = df_voted['PRECINCT NAME']
	df_combined['ASIAN-PACIFIC'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['LATINO'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AMERICAN'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_vs_race_percent_voted.csv'.format(year,election_type,county))

def race_combiner_statewide(year,election_type,df_voted,df_registered,county,primary):	
	df_combined = pd.DataFrame()
	df_black = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('BLACK')]].sum(axis=1)
	print df_voted
	raise ValueError('k')
	df_white = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('WHITE')]].sum(axis=1)
	df_latino = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('LATINO')]].sum(axis=1)
	df_asian_pacific = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('ASIAN')]].sum(axis=1)
	df_native = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('NATIVE')]].sum(axis=1)
	df_other = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('OTHER')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('UNKNOWN')]].sum(axis=1)
	df_black_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('BLACK')]].sum(axis=1)
	df_white_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('WHITE')]].sum(axis=1)
	df_latino_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('LATINO')]].sum(axis=1)
	df_asian_pacific_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('ASIAN')]].sum(axis=1)
	df_native_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('NATIVE')]].sum(axis=1)
	df_other_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('OTHER')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('UNKNOWN')]].sum(axis=1)
	df_combined['ASIAN-PACIFIC'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['LATINO'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AMERICAN'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Counties_vs_race_percent_voted.csv'.format(year,election_type))

def gender_vs_race_precinct(year,election_type,df_voted,df_registered,county,primary):	

	for precinct in df_voted['PRECINCT NAME'].unique():

		df_v = pd.DataFrame(columns=['RACE','MALE','FEMALE','UNKNOWN'])
		df_voted_precinct = df_voted.loc[df_voted['PRECINCT NAME']==precinct]
		df_registered_precinct = df_registered.loc[df_registered['PRECINCT NAME']==precinct]

		print df_voted_precinct
		print county
		for col,value in zip(df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' MALE')]].columns,df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' MALE')]].iloc[0]):
			col = col.replace(' MALE','')
			if col == 'UNKNOWN':
				df_v.loc[len(df_v)] = [col,value,'',0]
			else:	
				df_v.loc[len(df_v)] = [col,value,'','']
		for col,value in zip(df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' FEMALE')]].columns,df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' FEMALE')]].iloc[0]):
			col = col.replace(' FEMALE','')
			df_v.loc[df_v['RACE']==col,'FEMALE'] = value
		for col,value in zip(df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' UNKNOWN')]].columns,df_voted_precinct[df_voted_precinct.columns[pd.Series(df_voted_precinct.columns).str.endswith(' UNKNOWN')]].iloc[0]):
			if col != 'UNKNOWN':
				col = col.replace(' UNKNOWN','')
			df_v.loc[df_v['RACE']==col,'UNKNOWN'] = value
		df_v.fillna(0,inplace=True)	

		df_r = pd.DataFrame(columns=['RACE','MALE','FEMALE','UNKNOWN'])
		for col,value in zip(df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' MALE')]].columns,df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' MALE')]].iloc[0]):
			col = col.replace(' MALE','')
			if col == 'UNKNOWN':
				df_r.loc[len(df_r)] = [col,value,'',0]
			else:	
				df_r.loc[len(df_r)] = [col,value,'','']
		for col,value in zip(df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' FEMALE')]].columns,df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' FEMALE')]].iloc[0]):
			col = col.replace(' FEMALE','')
			df_r.loc[df_r['RACE']==col,'FEMALE'] = value
		for col,value in zip(df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' UNKNOWN')]].columns,df_registered_precinct[df_registered_precinct.columns[pd.Series(df_registered_precinct.columns).str.endswith(' UNKNOWN')]].iloc[0]):
			if col != 'UNKNOWN':
				col = col.replace(' UNKNOWN','')
			df_r.loc[df_r['RACE']==col,'UNKNOWN'] = value
		df_r.fillna(0,inplace=True)	

		for column in df_v.columns:
			if column != 'RACE':
				df_v[column] = df_v[column].apply(float)

		for column in df_r.columns:
			if column != 'RACE':
				df_r[column] = df_r[column].apply(float)

		df_combined = (df_v.loc[:,df_v.columns!='RACE'] / df_r.loc[:,df_r.columns!='RACE']).multiply(100).round(2)
		df_combined.fillna(0,inplace=True)
		df_combined.insert(loc=0,column='RACE',value=df_v['RACE'])
		df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_{}_gender_vs_race_percent_voted.csv'.format(year,election_type,county,precinct.replace('/','-')))

def gender_vs_race_county(year,election_type,df_voted,df_registered,county,primary):	
		
	df_v = pd.DataFrame(columns=['RACE','MALE','FEMALE','UNKNOWN'])

	for col,value in zip(df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].columns,df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].iloc[0]):
		col = col.replace(' MALE','')
		if col == 'UNKNOWN':
			df_v.loc[len(df_v)] = [col,value,'',0]
		else:	
			df_v.loc[len(df_v)] = [col,value,'','']
	for col,value in zip(df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' FEMALE')]].columns,df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' FEMALE')]].iloc[0]):
		col = col.replace(' FEMALE','')
		df_v.loc[df_v['RACE']==col,'FEMALE'] = value
	for col,value in zip(df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' UNKNOWN')]].columns,df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' UNKNOWN')]].iloc[0]):
		if col != 'UNKNOWN':
			col = col.replace(' UNKNOWN','')
		df_v.loc[df_v['RACE']==col,'UNKNOWN'] = value
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
		df_r.loc[df_r['RACE']==col,'FEMALE'] = value
	for col,value in zip(df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' UNKNOWN')]].columns,df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' UNKNOWN')]].iloc[0]):
		if col != 'UNKNOWN':
			col = col.replace(' UNKNOWN','')
		df_r.loc[df_r['RACE']==col,'UNKNOWN'] = value
	df_r.fillna(0,inplace=True)	

	for column in df_v.columns:
		if column != 'RACE':
			df_v[column] = df_v[column].apply(float)

	for column in df_r.columns:
		if column != 'RACE':
			df_r[column] = df_r[column].apply(float)

	df_v['TOTAL'] = df_v.loc[:,df_v.columns!='-'].sum(axis=1)
	df_r['TOTAL'] = df_r.loc[:,df_r.columns!='-'].sum(axis=1)
	df_v = df_v.append(df_v.sum(axis=0),ignore_index=True)
	df_v['RACE'][len(df_v)-1] = 'TOTAL'
	df_r = df_r.append(df_r.sum(axis=0),ignore_index=True)
	df_r['RACE'][len(df_r)-1] = 'TOTAL'

	df_combined = (df_v.loc[:,df_v.columns!='RACE'] / df_r.loc[:,df_r.columns!='RACE']).multiply(100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.insert(loc=0,column='-',value=df_v['RACE'])
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_race_percent_voted.csv'.format(year,election_type,county),index=False)

def gender_vs_age_county(year,election_type,df_voted,df_registered,county,primary):	
			
	df_combined = pd.DataFrame()
	df_male = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_male_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_combined['-'] = df_voted['-']
	df_combined['MALE'] = ((df_male/df_male_r)*100).round(2)
	df_combined['FEMALE'] = ((df_female/df_female_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_age_percent_voted.csv'.format(year,election_type,county),index=False)

def race_vs_age_county(year,election_type,df_voted,df_registered,county,primary):	
	
	df_combined = pd.DataFrame()
	df_combined['-'] = df_voted['-']
	df_black = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('BLACK')]].sum(axis=1)
	df_white = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('WHITE')]].sum(axis=1)
	df_latino = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('LATINO')]].sum(axis=1)
	df_asian_pacific = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('ASIAN')]].sum(axis=1)
	df_native = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('NATIVE')]].sum(axis=1)
	df_other = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('OTHER')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.startswith('UNKNOWN')]].sum(axis=1)
	df_black_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('BLACK')]].sum(axis=1)
	df_white_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('WHITE')]].sum(axis=1)
	df_latino_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('LATINO')]].sum(axis=1)
	df_asian_pacific_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('ASIAN')]].sum(axis=1)
	df_native_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('NATIVE')]].sum(axis=1)
	df_other_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('OTHER')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.startswith('UNKNOWN')]].sum(axis=1)
	#df_combined['CONGRESSIONAL DISTRICT'] = pd.Series(list('District {}'.format(x) for x in range(1,15)))
	df_combined['-'] = df_voted['-']
	df_combined['ASIAN-PACIFIC'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['LATINO'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AMERICAN'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_race_vs_age_percent_voted_race.csv'.format(year,election_type,county),index=False)

def race_vs_inter_year_county(county,years={'2016':['General'],'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL'])#race names])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_race_vs_age_percent_voted_race.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['-']=='TOTAL'],ignore_index=True)
				df_combined['-'][len(df_combined)-1] = '{} {}'.format(year,election_type)

	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_race_percent_voted.csv'.format(county))		
	df_combined = df_combined[['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL']]

def gender_vs_inter_year_county(county,years={'2016':['General'],'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['-','MALE','FEMALE','UNKNOWN','TOTAL'])#race names])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_age_percent_voted.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['-']=='TOTAL'],ignore_index=True)
				df_combined['-'][len(df_combined)-1] = '{} {}'.format(year,election_type)

	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_gender_percent_voted.csv'.format(county))		
	df_combined = df_combined[['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL']]

def age_vs_inter_year_county(county,years={'2016':['General'],'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL'])#race names])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_age_percent_voted_race.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['-']=='TOTAL'],ignore_index=True)
				df_combined['-'][len(df_combined)-1] = '{} {}'.format(year,election_type)

	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_age_percent_voted.csv'.format(county))		
	df_combined = df_combined[['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL']]

def race_vs_inter_year_congressional(congressional_district,years={'2016':['General'],'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL'])#race names])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/{}_race_vs_age_percent_voted_race.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['-']=='TOTAL'],ignore_index=True)
				df_combined['-'][len(df_combined)-1] = '{} {}'.format(year,election_type)

	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_race_percent_voted.csv'.format(county))		
	df_combined = df_combined[['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL']]

def gender_vs_inter_year_congressional(congressional_district,years={'2016':['General'],'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['-','MALE','FEMALE','UNKNOWN','TOTAL'])#race names])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/{}_gender_vs_age_percent_voted.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['-']=='TOTAL'],ignore_index=True)
				df_combined['-'][len(df_combined)-1] = '{} {}'.format(year,election_type)

	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_gender_percent_voted.csv'.format(county))		
	df_combined = df_combined[['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL']]

def region_vs_inter_year_county(county,years={'2016':['General'],'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL'])#race names])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_race_vs_age_percent_voted_race.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['-']=='TOTAL'],ignore_index=True)
				df_combined['-'][len(df_combined)-1] = '{} {}'.format(year,election_type)

	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_race_percent_voted.csv'.format(county))		
	df_combined = df_combined[['-','ASIAN-PACIFIC','BLACK','LATINO','NATIVE-AMERICAN','OTHER','WHITE','UNKNOWN','TOTAL']]		

def race_vs_inter_year_precinct(years=['2016','2018']):
	
	df_combined = pd.DataFrame(columns=[])#race names])
	for precinct in df_voted['PRECINCT NAME'].unique():
		pass
		#for election in elections:
			#df_combined.loc[year] = pd.Series
	if os.existsdir('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}'.format(county)) == False:
		os.mkdir('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}'.format(county))
	df_combined.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/{}/{}_{}_race_vs_age_percent_voted_race.csv'.format(county,county,precinct))		

def which_table_to_display(x_axis,y_axis,z_axis,region_1,region_2,election_type,election_year):

	year = election_year
	#month = str(election_date.split('_')[0])[:len(str(election_date.split('_')[0]))-1]
	month_to_election_type_dict = {'March':'Presidential_Primary','May':'Primary','July':'Primary_Runoff','November':'General'}
	election_type_to_month_dict = {'Presidential_Primary':'March','Primary':'May','Primary_Runoff':'July','General':'November'}
	month = election_type_to_month_dict[election_type]

	list_of_axis = [x_axis,y_axis]

	ga_counties = ['APPLING', 'ATKINSON', 'BACON', 'BAKER', 'BALDWIN', 'BANKS', 'BARROW', 'BARTOW', 'BEN HILL', 'BERRIEN', 'BIBB', 'BLECKLEY', 'BRANTLEY', 'BROOKS', 'BRYAN', 'BULLOCH', 'BURKE', 'BUTTS', 'CALHOUN', 'CAMDEN', 'CANDLER', 'CARROLL', 'CATOOSA', 'CHARLTON', 'CHATHAM', 'CHATTAHOOCHEE', 'CHATTOOGA', 'CHEROKEE', 'CLARKE', 'CLAY', 'CLAYTON', 'CLINCH', 'COBB', 'COFFEE', 'COLQUITT', 'COLUMBIA', 'COOK', 'COWETA', 'CRAWFORD', 'CRISP', 'DADE', 'DAWSON', 'DECATUR', 'DEKALB', 'DODGE', 'DOOLY', 'DOUGHERTY', 'DOUGLAS', 'EARLY', 'ECHOLS', 'EFFINGHAM', 'ELBERT', 'EMANUEL', 'EVANS', 'FANNIN', 'FAYETTE', 'FLOYD', 'FORSYTH', 'FRANKLIN', 'FULTON', 'GILMER', 'GLASCOCK', 'GLYNN', 'GORDON', 'GRADY', 'GREENE', 'GWINNETT', 'HABERSHAM', 'HALL', 'HANCOCK', 'HARALSON', 'HARRIS', 'HART', 'HEARD', 'HENRY', 'HOUSTON', 'IRWIN', 'JACKSON', 'JASPER', 'JEFF DAVIS', 'JEFFERSON', 'JENKINS', 'JOHNSON', 'JONES', 'LAMAR', 'LANIER', 'LAURENS', 'LEE', 'LIBERTY', 'LINCOLN', 'LONG', 'LOWNDES', 'LUMPKIN', 'MCDUFFIE', 'MCINTOSH', 'MACON', 'MADISON', 'MARION', 'MERIWETHER', 'MILLER', 'MITCHELL', 'MONROE', 'MONTGOMERY', 'MORGAN', 'MURRAY', 'MUSCOGEE', 'NEWTON', 'OCONEE', 'OGLETHORPE', 'PAULDING', 'PEACH', 'PICKENS', 'PIERCE', 'PIKE', 'POLK', 'PULASKI', 'PUTNAM', 'QUITMAN', 'RABUN', 'RANDOLPH', 'RICHMOND', 'ROCKDALE', 'SCHLEY', 'SCREVEN', 'SEMINOLE', 'SPALDING', 'STEPHENS', 'STEWART', 'SUMTER', 'TALBOT', 'TALIAFERRO', 'TATTNALL', 'TAYLOR', 'TELFAIR', 'TERRELL', 'THOMAS', 'TIFT', 'TOOMBS', 'TOWNS', 'TREUTLEN', 'TROUP', 'TURNER', 'TWIGGS', 'UNION', 'UPSON', 'WALKER', 'WALTON', 'WARE', 'WARREN', 'WASHINGTON', 'WAYNE', 'WEBSTER', 'WHEELER', 'WHITE', 'WHITFIELD', 'WILCOX', 'WILKES', 'WILKINSON', 'WORTH']

	#race_combiner_congressional(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_total_registered.csv'.format(year,election_type)),'general')
	#gender_combiner_congressional(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_total_registered.csv'.format(year,election_type)),'general')
	#AYYYYYYrace_vs_gender_combiner(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,county)),county,'general')
	race_combiner_statewide(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_registered.csv'.format(year,election_type)),'general')
	gender_combiner_statewide(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_registered.csv'.format(year,election_type)),'general')
	#age_combiner_statewide(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_registered.csv'.format(year,election_type)),'general')

	for county in ga_counties:
		pass
		#AGE FOR STATEWIDE!
		#gender_vs_race_precinct(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_total_registered.csv'.format(year,election_type,county)),county,'general')
		#gender_vs_race_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,county)),county,'general')
		#race_combiner_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_registered.csv'.format(year,election_type,county)),county,'general')
		#gender_combiner_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_registered.csv'.format(year,election_type,county)),county,'general')
		#gender_vs_age_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,county)),county,'general')
		#race_vs_age_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,county)),county,'general')
		#race_vs_inter_year_county(county)

	"""if x_axis == 'Statewide' or y_axis == 'Statewide':
		pass
		#total row from one statewide

	if x_axis == 'Congressional' or y_axis == 'Congressional':
		if x_axis == 'Gender and Race' or y_axis == 'Gender and Race':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/Congressional/Congressional_percent_voted.csv'.format(election_year,election_type),'r')
		elif x_axis == 'Gender' or y_axis == 'Gender':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/Congressional/Congressional_percent_voted_gender.csv'.format(election_year,election_type),'r')
		elif x_axis == 'Race' or y_axis == 'Race':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/Congressional/Congressional_percent_voted_race.csv'.format(election_year,election_type),'r')

	if x_axis == 'County' or y_axis == 'County':
		if x_axis == 'Gender and Race' or y_axis == 'Gender and Race':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/Statewide/Statewide_percent_voted.csv'.format(election_year,election_type),'r')
		elif x_axis == 'Gender' or y_axis == 'Gender':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/Statewide/Statewide_percent_voted_gender.csv'.format(election_year,election_type),'r')
		elif x_axis == 'Race' or y_axis == 'Race':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/Statewide/Statewide_percent_voted_race.csv'.format(election_year,election_type),'r')
		#within congressional districts or all

	if x_axis == 'Precinct' or y_axis == 'Precinct':
		county = z_axis 
		if x_axis == 'Gender and Race' or y_axis == 'Gender and Race':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/County/{}_percent_voted.csv'.format(election_year,election_type,county),'r')
		elif x_axis == 'Gender' or y_axis == 'Gender':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/County/{}_percent_voted_gender.csv'.format(election_year,election_type,county),'r')
		elif x_axis == 'Race' or y_axis == 'Race':
			csv_file = open('Georgia_Election_Data_CSVs/{}/{}/County/{}_percent_voted_race.csv'.format(election_year,election_type,county),'r')

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
			county = region_1 
			#add gender and race vs age
			if 'Gender' in list_of_axis and 'Race' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_race_percent_voted.csv'.format(election_year,election_type,county),'r')
			elif 'Age 'in list_of_axis and 'Race' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/{}/{}/County/{}_race_vs_age_percent_voted'.format(election_year,election_type,county),'r')
			elif 'Gender' in list_of_axis and 'Age' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_age_percent_voted.csv'.format(election_year,election_type,county.upper()),'r')	
		if z_axis == 'Precinct':
			if 'Gender' in list_of_axis and 'Race' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_{}_percent_voted_race.csv'.format(election_year,election_type,county,precinct),'r')
		
	if 'Year' in list_of_axis:
		if z_axis == 'Statewide':
			if 'Gender' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/Statewide_inter_year_vs_gender_percent_voted.csv')
			elif 'Race' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/Statewide_inter_year_vs_race_percent_voted.csv')
		elif z_axis == 'Congressional':
			congressional_district = z_axis
			if 'Gender' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_gender_percent_voted.csv'.format(congressional_district))
			elif 'Race' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_race_percent_voted.csv'.format(congressional_district))
		elif z_axis == 'County':
			county = z_axis
			if 'Gender' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_gender_percent_voted.csv'.format(county))
			elif 'Race' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_race_percent_voted.csv'.format(county))
			elif 'Age' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/{}_inter_year_vs_age_percent_voted.csv'.format(county))
		elif z_axis == 'Precinct':
			precinct = z_axis
			if 'Gender' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/{}/{}_inter_year_vs_gender_percent_voted.csv'.format(precinct))
			elif 'Race' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/{}/{}_inter_year_vs_race_percent_voted.csv'.format(precinct))
		else:
			if 'Congressional' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/Inter_year_vs_congressional_percent_voted.csv')
			elif 'County' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/Inter_year_vs_county_percent_voted.csv')
			elif 'Precinct' in list_of_axis:
				csv_file = open('Georgia_Election_Data_CSVs/Inter_Year/Inter_year_vs_precinct_percent_voted.csv')

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

	html_code = pt.get_html_string()
	print html_code
	return html_code

	html_file = open('/Users/sammahle/Desktop/OurVoteNowVoterHelper/voting_stats_html.txt','w')
	html_file = html_file.write(html_code)	

	with open("voting_stats_html.txt", "r") as f1:
	    t1 = f1.readlines()
	with open("voter_stats.html", "r") as f2:
	    t2 = f2.readlines()

	line_to_insert = t2.index('        <table id="data-table" class="cell-border hover compact">\n')
	line_that_ends = t2.index('        </table>\n')

	t2 = t2[:line_to_insert+1] + t2[line_that_ends:]

	for line in t1:
		if line.strip() == '<table>' or line.strip() == '</table>':
			pass
		else:	
			t2.insert(line_to_insert+1, '        {}'.format(line))
			line_to_insert += 1

	with open("voter_stats.html", "w") as f2:
	    f2.writelines(t2)"""

which_table_to_display('Age','Gender','County','Fulton','-','General','2018')
#codeString = which_table_to_display(parameters.getvalue("x-axis"),parameters.getvalue("y-axis"),parameters.getvalue("z-axis"),parameters.getvalue("region_1"),parameters.getvalue("region_2"),parameters.getvalue("election_type"),parameters.getvalue("election_year"))

returnData = {
	"data": codeString
}
self.response.out.write(json.dumps(returnData))

#county always vertical 
#then age 
#last demo	 

#raise ValueError('l')


"""function postData(input) {
    $.ajax({
        type: "POST",
        url: "/reverse_pca.py",
        data: {x_axis=,y_axis=,z_axis=}
    });
}   """