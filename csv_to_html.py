import pandas as pd
import os
from prettytable import PrettyTable
import cgi
import json
import re
parameters = cgi.FieldStorage()

def zero_filler(df):
	df = df.astype(str)
	for col in df.columns[1:]:
		df[col] = df[col].str.pad(5,side='right',fillchar='0').replace('0.000','0.00')
	return df

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

	df_divided = pd.concat([df_male,df_female,df_unknown,df_voted['TOTAL']],axis=1)/pd.concat([df_male_r,df_female_r,df_unknown_r,df_registered['TOTAL']],axis=1)
	pd_seires = pd.Series(df_divided.loc[len(df_divided)-1])
	pd_seires = (pd_seires*100).round(2)
	pd_seires['CONGRESSIONAL DISTRICT'] = 'TOTAL'
	pd_seires.rename({0:'MALE',1:'FEMALE',2:'UNKNOWN',3:'TOTAL'},inplace=True)
	df_combined.loc[len(df_combined)+2] = pd_seires
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_vs_gender_percent_voted.csv'.format(year,election_type),index=False)

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
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_vs_gender_percent_voted.csv'.format(year,election_type,county),index=False)

def gender_combiner_statewide(year,election_type,df_voted,df_registered,primary):
	df_combined = pd.DataFrame()
	df_male = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown = df_voted[df_voted.columns[pd.Series(df_voted.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_male_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith(' MALE')]].sum(axis=1)
	df_female_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('FEMALE')]].sum(axis=1)
	df_unknown_r = df_registered[df_registered.columns[pd.Series(df_registered.columns).str.endswith('UNKNOWN')]].sum(axis=1)
	df_combined['COUNTY NAME'] = df_voted['COUNTY NAME']
	df_combined['MALE'] = ((df_male/df_male_r)*100).round(2)
	df_combined['FEMALE'] = ((df_female/df_female_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Counties_vs_gender_percent_voted.csv'.format(year,election_type),index=False)

def age_vs_gender_combiner_statewide(year,election_type,df_voted,df_registered,primary):
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
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Gender_vs_age_percent_voted.csv'.format(year,election_type),index=False)

def age_vs_race_combiner_statewide(year,election_type,df_voted,df_registered,primary):
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
	df_combined['AGE GROUP'] = df_voted['AGE GROUP']
	df_combined['ASIA-PI'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['HISP-LT'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AM'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Race_vs_age_percent_voted.csv'.format(year,election_type),index=False)

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
	df_combined['NATIVE-AM'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	
	df_divided = pd.concat([df_black,df_white,df_latino,df_asian_pacific,df_native,df_other,df_unknown,df_voted['TOTAL']],axis=1)/pd.concat([df_black_r,df_white_r,df_latino_r,df_asian_pacific_r,df_native_r,df_other_r,df_unknown_r,df_registered['TOTAL']],axis=1)
	pd_seires = pd.Series(df_divided.loc[len(df_divided)-1])
	pd_seires = (pd_seires*100).round(2)
	pd_seires['CONGRESSIONAL DISTRICT'] = 'TOTAL'
	pd_seires.rename({0:'BLACK',1:'WHITE',2:'HISP-LT',3:'ASIA-PI',4:'NATIVE-AM',5:'OTHER',6:'UNKNOWN',7:'TOTAL'},inplace=True)
	df_combined.loc[len(df_combined)+2] = pd_seires
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_vs_race_percent_voted.csv'.format(year,election_type),index=False)

def race_combiner_county(year,election_type,df_voted,df_registered,county,primary):	
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
	df_combined['PRECINCT NAME'] = df_voted['PRECINCT NAME']
	df_combined['ASIA-PI'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['HISP-LT'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AM'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_vs_race_percent_voted.csv'.format(year,election_type,county),index=False)

def race_combiner_statewide(year,election_type,df_voted,df_registered,primary):	
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
	df_combined['COUNTY NAME'] = df_voted['COUNTY NAME']
	df_combined['ASIA-PI'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['HISP-LT'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AM'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Counties_vs_race_percent_voted.csv'.format(year,election_type),index=False)

def gender_vs_race_statewide(year,election_type,df_voted,df_registered,primary):

		df_v = pd.DataFrame(columns=['RACE','MALE','FEMALE','UNKNOWN'])
		df_voted_precinct = df_voted.loc[df_voted['COUNTY NAME']=='TOTAL']
		df_registered_precinct = df_registered.loc[df_registered['COUNTY NAME']=='TOTAL']

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

		df_r = df_r.append(df_r.sum(axis=0),ignore_index=True)
		df_r['TOTAL'] = df_r.sum(axis=1)
		df_r['RACE'][len(df_r)-1] = 'TOTAL'
		df_v = df_v.append(df_v.sum(axis=0),ignore_index=True)
		df_v['TOTAL'] = df_v.sum(axis=1)
		df_v['RACE'][len(df_v)-1] = 'TOTAL'
		
		for column in df_v.columns:
			if column != 'RACE':
				df_v[column] = df_v[column].apply(float)

		for column in df_r.columns:
			if column != 'RACE':
				df_r[column] = df_r[column].apply(float)

		df_combined = (df_v.loc[:,df_v.columns!='RACE'] / df_r.loc[:,df_r.columns!='RACE']).multiply(100).round(2)
		df_combined.fillna(0,inplace=True)
		df_combined.insert(loc=0,column='RACE',value=df_v['RACE'])
		zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Gender_vs_race_percent_voted.csv'.format(year,election_type),index=False)

def gender_vs_race_precinct(year,election_type,df_voted,df_registered,county,primary):	

	for precinct in df_voted['PRECINCT NAME'].unique():

		df_v = pd.DataFrame(columns=['RACE','MALE','FEMALE','UNKNOWN'])
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

		df_r = df_r.append(df_r.sum(axis=0),ignore_index=True)
		df_r['TOTAL'] = df_r.sum(axis=1)
		df_r['RACE'][len(df_r)-1] = 'TOTAL'
		df_v = df_v.append(df_v.sum(axis=0),ignore_index=True)
		df_v['TOTAL'] = df_v.sum(axis=1)
		df_v['RACE'][len(df_v)-1] = 'TOTAL'
		
		for column in df_v.columns:
			if column != 'RACE':
				df_v[column] = df_v[column].apply(float)

		for column in df_r.columns:
			if column != 'RACE':
				df_r[column] = df_r[column].apply(float)

		df_combined = (df_v.loc[:,df_v.columns!='RACE'] / df_r.loc[:,df_r.columns!='RACE']).multiply(100).round(2)
		df_combined.fillna(0,inplace=True)
		df_combined.insert(loc=0,column='RACE',value=df_v['RACE'])
		zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_{}_gender_vs_race_percent_voted.csv'.format(year,election_type,county,precinct.replace('/','-')),index=False)

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

	df_r = pd.DataFrame(columns=['RACE','MALE','FEMALE','UNKNOWN'])
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

	df_v['TOTAL'] = df_v.loc[:,df_v.columns!='RACE'].sum(axis=1)
	df_r['TOTAL'] = df_r.loc[:,df_r.columns!='RACE'].sum(axis=1)
	df_v = df_v.append(df_v.sum(axis=0),ignore_index=True)
	df_v['RACE'][len(df_v)-1] = 'TOTAL'
	df_r = df_r.append(df_r.sum(axis=0),ignore_index=True)
	df_r['RACE'][len(df_r)-1] = 'TOTAL'

	df_combined = (df_v.loc[:,df_v.columns!='RACE'] / df_r.loc[:,df_r.columns!='RACE']).multiply(100).round(2)
	df_combined.fillna(0,inplace=True)
	df_combined.insert(loc=0,column='RACE',value=df_v['RACE'])
	
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_race_percent_voted.csv'.format(year,election_type,county),index=False)

def gender_vs_age_county(year,election_type,df_voted,df_registered,county,primary):	
			
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
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_age_percent_voted.csv'.format(year,election_type,county),index=False)

def race_vs_age_county(year,election_type,df_voted,df_registered,county,primary):	
	
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
	df_combined['AGE GROUP'] = df_voted['AGE GROUP']
	df_combined['ASIA-PI'] = ((df_asian_pacific/df_asian_pacific_r)*100).round(2)
	df_combined['BLACK'] =  ((df_black/df_black_r)*100).round(2)
	df_combined['HISP-LT'] = ((df_latino/df_latino_r)*100).round(2)
	df_combined['NATIVE-AM'] = ((df_native/df_native_r)*100).round(2)
	df_combined['OTHER'] = ((df_other/df_other_r)*100).round(2)
	df_combined['WHITE'] = ((df_white/df_white_r)*100).round(2)
	df_combined['UNKNOWN'] = ((df_unknown/df_unknown_r)*100).round(2)
	df_combined['TOTAL'] = (df_voted['TOTAL']/df_registered['TOTAL']*100).round(2)
	df_combined.fillna(0,inplace=True)
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_race_vs_age_percent_voted.csv'.format(year,election_type,county),index=False)

def gender_vs_race_congressional(year,election_type,df_voted,df_registered,congressional_district,primary):	

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

	df_r = pd.DataFrame(columns=['RACE','MALE','FEMALE','UNKNOWN'])
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
	df_combined.insert(loc=0,column='RACE',value=df_v['RACE'])
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/US{}_gender_vs_race_percent_voted.csv'.format(year,election_type,str(congressional_district).zfill(2)),index=False)

def race_vs_inter_year_county(county,years={'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','ASIA-PI','BLACK','HISP-LT','NATIVE-AM','OTHER','WHITE','UNKNOWN','TOTAL'])#race names])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_race_vs_age_percent_voted.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['AGE GROUP']=='TOTAL'],ignore_index=True)
				df_combined['ELECTION TYPE/YEAR'][len(df_combined)-1] = '{} {}'.format(year,election_type)
	
	df_combined = df_combined[['ELECTION TYPE/YEAR','ASIA-PI','BLACK','HISP-LT','NATIVE-AM','OTHER','WHITE','UNKNOWN','TOTAL']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/County/{}_inter_year_vs_race_percent_voted.csv'.format(county),index=False)		

def gender_vs_inter_year_county(county,years={'2016':['General'],'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','MALE','FEMALE','UNKNOWN','TOTAL'])#race names])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_age_percent_voted.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['AGE GROUP']=='TOTAL'],ignore_index=True)
				df_combined['ELECTION TYPE/YEAR'][len(df_combined)-1] = '{} {}'.format(year,election_type)
	
	df_combined = df_combined[['ELECTION TYPE/YEAR','MALE','FEMALE','UNKNOWN','TOTAL']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/County/{}_inter_year_vs_gender_percent_voted.csv'.format(county),index=False)				

def age_vs_inter_year_county(county,years={'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-OVER','TOTAL'])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_gender_vs_age_percent_voted.csv'.format(year,election_type,county))		
				df_year = df_year[['AGE GROUP','TOTAL VOTERS']].T
				df_year.columns = df_year.iloc[0]
				df_year = df_year.reindex(df_year.index.drop('AGE GROUP'))
				df_year.index = ['{} {}'.format(year,election_type)]
				df_year.reset_index(inplace=True)
				df_year.rename(columns={'index':'ELECTION TYPE/YEAR'},inplace=True)
				df_combined = df_year
				
	df_combined = df_combined[['ELECTION TYPE/YEAR','18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-OVER','TOTAL']]

	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/County/{}_inter_year_vs_age_percent_voted.csv'.format(county),index=False)			

def race_vs_inter_year_statewide(years={'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','ASIA-PI','BLACK','HISP-LT','NATIVE-AM','OTHER','WHITE','UNKNOWN','TOTAL'])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Race_vs_age_percent_voted.csv'.format(year,election_type))		
				df_combined = df_combined.append(df_year.loc[df_year['AGE GROUP']=='TOTAL'],ignore_index=True)
				df_combined['ELECTION TYPE/YEAR'][len(df_combined)-1] = '{} {}'.format(year,election_type)
	
	df_combined = df_combined[['ELECTION TYPE/YEAR','ASIA-PI','BLACK','HISP-LT','NATIVE-AM','OTHER','WHITE','UNKNOWN','TOTAL']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Statewide/Inter_year_vs_race_percent_voted.csv',index=False)		

def gender_vs_inter_year_statewide(years={'2016':['General'],'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','MALE','FEMALE','UNKNOWN','TOTAL'])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Gender_vs_age_percent_voted.csv'.format(year,election_type))		
				df_combined = df_combined.append(df_year.loc[df_year['AGE GROUP']=='TOTAL'],ignore_index=True)
				df_combined['ELECTION TYPE/YEAR'][len(df_combined)-1] = '{} {}'.format(year,election_type)
	
	df_combined = df_combined[['ELECTION TYPE/YEAR','MALE','FEMALE','UNKNOWN','TOTAL']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Statewide/Inter_year_vs_gender_percent_voted.csv',index=False)				

def age_vs_inter_year_statewide(years={'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-OVER','TOTAL'])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Gender_vs_age_percent_voted.csv'.format(year,election_type))		
				df_year = df_year[['AGE GROUP','TOTAL']].T
				df_year.columns = df_year.iloc[0]
				df_year = df_year.reindex(df_year.index.drop('AGE GROUP'))
				df_year.index = ['{} {}'.format(year,election_type)]
				df_year.reset_index(inplace=True)
				df_year.rename(columns={'index':'ELECTION TYPE/YEAR'},inplace=True)
				df_combined = df_year
				
	df_combined = df_combined[['ELECTION TYPE/YEAR','18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-OVER','TOTAL']]

	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Statewide/Inter_year_vs_age_percent_voted.csv',index=False)			

def race_vs_inter_year_congressional(congressional_district,years={'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','ASIA-PI','BLACK','HISP-LT','NATIVE-AM','OTHER','WHITE','UNKNOWN','TOTAL'])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/US{}_gender_vs_race_percent_voted.csv'.format(year,election_type,str(congressional_district).zfill(2)))	
				df_year = df_year[['RACE','TOTAL']].T
				df_year.columns = df_year.iloc[0]
				df_year = df_year.reindex(df_year.index.drop('RACE'))
				df_year.index = ['{} {}'.format(year,election_type)]
				df_year.reset_index(inplace=True)
				df_year.rename(columns={'index':'ELECTION TYPE/YEAR'},inplace=True)
				df_combined = df_year

				#df_combined = df_combined.append(df_year.loc[df_year['RACE']=='TOTAL'],ignore_index=True)
				#df_combined['ELECTION TYPE/YEAR'][len(df_combined)-1] = '{} {}'.format(year,election_type)
	
	df_combined = df_combined[['ELECTION TYPE/YEAR','ASIA-PI','BLACK','HISP-LT','NATIVE-AM','OTHER','WHITE','UNKNOWN','TOTAL']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Congressional/US{}_inter_year_vs_race_percent_voted.csv'.format(str(congressional_district).zfill(2)),index=False)			

def gender_vs_inter_year_congressional(congressional_district,years={'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','MALE','FEMALE','UNKNOWN','TOTAL'])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/US{}_gender_vs_race_percent_voted.csv'.format(year,election_type,str(congressional_district).zfill(2)))		
				df_combined = df_combined.append(df_year.loc[df_year['RACE']=='TOTAL'],ignore_index=True)
				df_combined['ELECTION TYPE/YEAR'][len(df_combined)-1] = '{} {}'.format(year,election_type)
	
	df_combined = df_combined[['ELECTION TYPE/YEAR','MALE','FEMALE','UNKNOWN','TOTAL']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Congressional/US{}_inter_year_vs_gender_percent_voted.csv'.format(str(congressional_district).zfill(2)),index=False)				

def county_vs_inter_year(years={'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR', 'APPLING', 'ATKINSON', 'BACON', 'BAKER', 'BALDWIN', 'BANKS', 'BARROW', 'BARTOW', 'BEN HILL', 'BERRIEN', 'BIBB', 'BLECKLEY', 'BRANTLEY', 'BROOKS', 'BRYAN', 'BULLOCH', 'BURKE', 'BUTTS', 'CALHOUN', 'CAMDEN', 'CANDLER', 'CARROLL', 'CATOOSA', 'CHARLTON', 'CHATHAM', 'CHATTAHOOCHEE', 'CHATTOOGA', 'CHEROKEE', 'CLARKE', 'CLAY', 'CLAYTON', 'CLINCH', 'COBB', 'COFFEE', 'COLQUITT', 'COLUMBIA', 'COOK', 'COWETA', 'CRAWFORD', 'CRISP', 'DADE', 'DAWSON', 'DECATUR', 'DEKALB', 'DODGE', 'DOOLY', 'DOUGHERTY', 'DOUGLAS', 'EARLY', 'ECHOLS', 'EFFINGHAM', 'ELBERT', 'EMANUEL', 'EVANS', 'FANNIN', 'FAYETTE', 'FLOYD', 'FORSYTH', 'FRANKLIN', 'FULTON', 'GILMER', 'GLASCOCK', 'GLYNN', 'GORDON', 'GRADY', 'GREENE', 'GWINNETT', 'HABERSHAM', 'HALL', 'HANCOCK', 'HARALSON', 'HARRIS', 'HART', 'HEARD', 'HENRY', 'HOUSTON', 'IRWIN', 'JACKSON', 'JASPER', 'JEFF DAVIS', 'JEFFERSON', 'JENKINS', 'JOHNSON', 'JONES', 'LAMAR', 'LANIER', 'LAURENS', 'LEE', 'LIBERTY', 'LINCOLN', 'LONG', 'LOWNDES', 'LUMPKIN', 'MCDUFFIE', 'MCINTOSH', 'MACON', 'MADISON', 'MARION', 'MERIWETHER', 'MILLER', 'MITCHELL', 'MONROE', 'MONTGOMERY', 'MORGAN', 'MURRAY', 'MUSCOGEE', 'NEWTON', 'OCONEE', 'OGLETHORPE', 'PAULDING', 'PEACH', 'PICKENS', 'PIERCE', 'PIKE', 'POLK', 'PULASKI', 'PUTNAM', 'QUITMAN', 'RABUN', 'RANDOLPH', 'RICHMOND', 'ROCKDALE', 'SCHLEY', 'SCREVEN', 'SEMINOLE', 'SPALDING', 'STEPHENS', 'STEWART', 'SUMTER', 'TALBOT', 'TALIAFERRO', 'TATTNALL', 'TAYLOR', 'TELFAIR', 'TERRELL', 'THOMAS', 'TIFT', 'TOOMBS', 'TOWNS', 'TREUTLEN', 'TROUP', 'TURNER', 'TWIGGS', 'UNION', 'UPSON', 'WALKER', 'WALTON', 'WARE', 'WARREN', 'WASHINGTON', 'WAYNE', 'WEBSTER', 'WHEELER', 'WHITE', 'WHITFIELD', 'WILCOX', 'WILKES', 'WILKINSON', 'WORTH','TOTAL'])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_percent_voted.csv'.format(year,election_type))		
				df_year = df_year[['COUNTY NAME','TOTAL']].T
				df_year.columns = df_year.iloc[0]
				df_year = df_year.reindex(df_year.index.drop('COUNTY NAME'))
				df_year.index = ['{} {}'.format(year,election_type)]
				df_year.reset_index(inplace=True)
				df_year.rename(columns={'index':'ELECTION TYPE/YEAR'},inplace=True)
				df_combined = df_year

	df_combined = df_combined[['ELECTION TYPE/YEAR', 'APPLING', 'ATKINSON', 'BACON', 'BAKER', 'BALDWIN', 'BANKS', 'BARROW', 'BARTOW', 'BEN HILL', 'BERRIEN', 'BIBB', 'BLECKLEY', 'BRANTLEY', 'BROOKS', 'BRYAN', 'BULLOCH', 'BURKE', 'BUTTS', 'CALHOUN', 'CAMDEN', 'CANDLER', 'CARROLL', 'CATOOSA', 'CHARLTON', 'CHATHAM', 'CHATTAHOOCHEE', 'CHATTOOGA', 'CHEROKEE', 'CLARKE', 'CLAY', 'CLAYTON', 'CLINCH', 'COBB', 'COFFEE', 'COLQUITT', 'COLUMBIA', 'COOK', 'COWETA', 'CRAWFORD', 'CRISP', 'DADE', 'DAWSON', 'DECATUR', 'DEKALB', 'DODGE', 'DOOLY', 'DOUGHERTY', 'DOUGLAS', 'EARLY', 'ECHOLS', 'EFFINGHAM', 'ELBERT', 'EMANUEL', 'EVANS', 'FANNIN', 'FAYETTE', 'FLOYD', 'FORSYTH', 'FRANKLIN', 'FULTON', 'GILMER', 'GLASCOCK', 'GLYNN', 'GORDON', 'GRADY', 'GREENE', 'GWINNETT', 'HABERSHAM', 'HALL', 'HANCOCK', 'HARALSON', 'HARRIS', 'HART', 'HEARD', 'HENRY', 'HOUSTON', 'IRWIN', 'JACKSON', 'JASPER', 'JEFF DAVIS', 'JEFFERSON', 'JENKINS', 'JOHNSON', 'JONES', 'LAMAR', 'LANIER', 'LAURENS', 'LEE', 'LIBERTY', 'LINCOLN', 'LONG', 'LOWNDES', 'LUMPKIN', 'MCDUFFIE', 'MCINTOSH', 'MACON', 'MADISON', 'MARION', 'MERIWETHER', 'MILLER', 'MITCHELL', 'MONROE', 'MONTGOMERY', 'MORGAN', 'MURRAY', 'MUSCOGEE', 'NEWTON', 'OCONEE', 'OGLETHORPE', 'PAULDING', 'PEACH', 'PICKENS', 'PIERCE', 'PIKE', 'POLK', 'PULASKI', 'PUTNAM', 'QUITMAN', 'RABUN', 'RANDOLPH', 'RICHMOND', 'ROCKDALE', 'SCHLEY', 'SCREVEN', 'SEMINOLE', 'SPALDING', 'STEPHENS', 'STEWART', 'SUMTER', 'TALBOT', 'TALIAFERRO', 'TATTNALL', 'TAYLOR', 'TELFAIR', 'TERRELL', 'THOMAS', 'TIFT', 'TOOMBS', 'TOWNS', 'TREUTLEN', 'TROUP', 'TURNER', 'TWIGGS', 'UNION', 'UPSON', 'WALKER', 'WALTON', 'WARE', 'WARREN', 'WASHINGTON', 'WAYNE', 'WEBSTER', 'WHEELER', 'WHITE', 'WHITFIELD', 'WILCOX', 'WILKES', 'WILKINSON', 'WORTH','TOTAL']]			
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Statewide/Inter_year_vs_counties_percent_voted.csv',index=False)				

def precinct_vs_inter_year(county,years={'2018':['General']}):
	
	df_year_names = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_vs_race_percent_voted.csv'.format('2018','General',county))		
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR']+list(df_year_names['PRECINCT NAME'].unique()))
	
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_vs_race_percent_voted.csv'.format(year,election_type,county))		
				df_combined = df_combined.append(df_year.loc[df_year['PRECINCT NAME']=='TOTAL'],ignore_index=True)
				df_year = df_year[['PRECINCT NAME','TOTAL']].T
				df_year.columns = df_year.iloc[0]
				df_year = df_year.reindex(df_year.index.drop('PRECINCT NAME'))
				df_year.index = ['{} {}'.format(year,election_type)]
				df_year.reset_index(inplace=True)
				df_year.rename(columns={'index':'ELECTION TYPE/YEAR'},inplace=True)
				df_combined = df_year

	df_combined = df_combined[['ELECTION TYPE/YEAR']+list(df_year_names['PRECINCT NAME'].unique())]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/County/Inter_year_vs_{}_precincts_percent_voted.csv'.format(county),index=False)				

def congressional_vs_inter_year(years={'2018':['General']}):
		
	df_combined = pd.DataFrame(columns=['Congressional District 1', 'Congressional District 2', 'Congressional District 3', 'Congressional District 4', 'Congressional District 5', 'Congressional District 6', 'Congressional District 7', 'Congressional District 8', 'Congressional District 9', 'Congressional District 10', 'Congressional District 11', 'Congressional District 12', 'Congressional District 13', 'Congressional District 14'])
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_percent_voted.csv'.format(year,election_type))		
				df_year = df_year[['CONGRESSIONAL DISTRICT','TOTAL']].T
				df_year.columns = df_year.iloc[0]
				df_year = df_year.reindex(df_year.index.drop('CONGRESSIONAL DISTRICT'))
				df_year.index = ['{} {}'.format(year,election_type)]
				df_year.reset_index(inplace=True)
				df_year.rename(columns={'index':'ELECTION TYPE/YEAR'},inplace=True)
				df_combined = df_year

	df_combined = df_combined[['ELECTION TYPE/YEAR','Congressional District 1', 'Congressional District 2', 'Congressional District 3', 'Congressional District 4', 'Congressional District 5', 'Congressional District 6', 'Congressional District 7', 'Congressional District 8', 'Congressional District 9', 'Congressional District 10', 'Congressional District 11', 'Congressional District 12', 'Congressional District 13', 'Congressional District 14']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Statewide/Inter_year_vs_congressional_districts_percent_voted.csv',index=False)				


def race_vs_inter_year_precinct(county,precinct,years={'2018':['General']}):
	
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','ASIA-PI','BLACK','HISP-LT','NATIVE-AM','OTHER','WHITE','UNKNOWN','TOTAL'])
	if os.path.exists('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Precinct/{}'.format(county)) == False:
		os.mkdir('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Precinct/{}'.format(county))
	
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_{}_gender_vs_race_percent_voted.csv'.format(year,election_type,county,str(precinct).upper()))		
				df_year = df_year[['RACE','TOTAL']].T
				df_year.columns = df_year.iloc[0]
				df_year = df_year.reindex(df_year.index.drop('RACE'))
				df_year.index = ['{} {}'.format(year,election_type)]
				df_year.reset_index(inplace=True)
				df_year.rename(columns={'index':'ELECTION TYPE/YEAR'},inplace=True)
				df_combined = df_year

	df_combined = df_combined[['ELECTION TYPE/YEAR','ASIA-PI','BLACK','HISP-LT','NATIVE-AM','OTHER','WHITE','UNKNOWN','TOTAL']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Precinct/{}/{}_inter_year_vs_race_percent_voted.csv'.format(county,precinct),index=False)	

def gender_vs_inter_year_precinct(county,precinct,years={'2018':['General']}):
	
	df_combined = pd.DataFrame(columns=['ELECTION TYPE/YEAR','MALE','FEMALE','UNKNOWN','TOTAL'])
	if os.path.exists('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Precinct/{}'.format(county)) == False:
		os.mkdir('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Precinct/{}'.format(county))
	
	for year in years.keys():
		if any(years[year]):
			for election_type in years[year]:
				df_year = pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_{}_gender_vs_race_percent_voted.csv'.format(year,election_type,county,str(precinct).upper()))		
				df_combined = df_combined.append(df_year.loc[df_year['RACE']=='TOTAL'],ignore_index=True)
				df_combined['ELECTION TYPE/YEAR'][len(df_combined)-1] = '{} {}'.format(year,election_type)

	df_combined = df_combined[['ELECTION TYPE/YEAR','MALE','FEMALE','UNKNOWN','TOTAL']]
	zero_filler(df_combined).to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/Inter_Year/Precinct/{}/{}_inter_year_vs_gender_percent_voted.csv'.format(county,precinct),index=False)	

def table_calculator(election_type,election_year):

	year = election_year
	#month = str(election_date.split('_')[0])[:len(str(election_date.split('_')[0]))-1]
	month_to_election_type_dict = {'March':'Presidential_Primary','May':'Primary','July':'Primary_Runoff','November':'General'}
	election_type_to_month_dict = {'Presidential_Primary':'March','Primary':'May','Primary_Runoff':'July','General':'November'}
	month = election_type_to_month_dict[election_type]

	ga_counties = ['APPLING', 'ATKINSON', 'BACON', 'BAKER', 'BALDWIN', 'BANKS', 'BARROW', 'BARTOW', 'BEN HILL', 'BERRIEN', 'BIBB', 'BLECKLEY', 'BRANTLEY', 'BROOKS', 'BRYAN', 'BULLOCH', 'BURKE', 'BUTTS', 'CALHOUN', 'CAMDEN', 'CANDLER', 'CARROLL', 'CATOOSA', 'CHARLTON', 'CHATHAM', 'CHATTAHOOCHEE', 'CHATTOOGA', 'CHEROKEE', 'CLARKE', 'CLAY', 'CLAYTON', 'CLINCH', 'COBB', 'COFFEE', 'COLQUITT', 'COLUMBIA', 'COOK', 'COWETA', 'CRAWFORD', 'CRISP', 'DADE', 'DAWSON', 'DECATUR', 'DEKALB', 'DODGE', 'DOOLY', 'DOUGHERTY', 'DOUGLAS', 'EARLY', 'ECHOLS', 'EFFINGHAM', 'ELBERT', 'EMANUEL', 'EVANS', 'FANNIN', 'FAYETTE', 'FLOYD', 'FORSYTH', 'FRANKLIN', 'FULTON', 'GILMER', 'GLASCOCK', 'GLYNN', 'GORDON', 'GRADY', 'GREENE', 'GWINNETT', 'HABERSHAM', 'HALL', 'HANCOCK', 'HARALSON', 'HARRIS', 'HART', 'HEARD', 'HENRY', 'HOUSTON', 'IRWIN', 'JACKSON', 'JASPER', 'JEFF DAVIS', 'JEFFERSON', 'JENKINS', 'JOHNSON', 'JONES', 'LAMAR', 'LANIER', 'LAURENS', 'LEE', 'LIBERTY', 'LINCOLN', 'LONG', 'LOWNDES', 'LUMPKIN', 'MCDUFFIE', 'MCINTOSH', 'MACON', 'MADISON', 'MARION', 'MERIWETHER', 'MILLER', 'MITCHELL', 'MONROE', 'MONTGOMERY', 'MORGAN', 'MURRAY', 'MUSCOGEE', 'NEWTON', 'OCONEE', 'OGLETHORPE', 'PAULDING', 'PEACH', 'PICKENS', 'PIERCE', 'PIKE', 'POLK', 'PULASKI', 'PUTNAM', 'QUITMAN', 'RABUN', 'RANDOLPH', 'RICHMOND', 'ROCKDALE', 'SCHLEY', 'SCREVEN', 'SEMINOLE', 'SPALDING', 'STEPHENS', 'STEWART', 'SUMTER', 'TALBOT', 'TALIAFERRO', 'TATTNALL', 'TAYLOR', 'TELFAIR', 'TERRELL', 'THOMAS', 'TIFT', 'TOOMBS', 'TOWNS', 'TREUTLEN', 'TROUP', 'TURNER', 'TWIGGS', 'UNION', 'UPSON', 'WALKER', 'WALTON', 'WARE', 'WARREN', 'WASHINGTON', 'WAYNE', 'WEBSTER', 'WHEELER', 'WHITE', 'WHITFIELD', 'WILCOX', 'WILKES', 'WILKINSON', 'WORTH']

	race_vs_inter_year_statewide()
	gender_vs_inter_year_statewide()
	age_vs_inter_year_statewide()
	gender_vs_race_statewide(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_registered.csv'.format(year,election_type)),'general')
	age_vs_gender_combiner_statewide(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Age_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Age_total_registered.csv'.format(year,election_type)),'general')
	age_vs_race_combiner_statewide(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Age_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Age_total_registered.csv'.format(year,election_type)),'general')
	race_combiner_congressional(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_total_registered.csv'.format(year,election_type)),'general')
	gender_combiner_congressional(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/Congressional_total_registered.csv'.format(year,election_type)),'general')
	race_combiner_statewide(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_registered.csv'.format(year,election_type)),'general')
	gender_combiner_statewide(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_voted.csv'.format(year,election_type)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Statewide/County_total_registered.csv'.format(year,election_type)),'general')
	ga_precincts = {'Union': ['Trackrock', 'Total', 'Suches', 'Pat Colwell', 'Owltown', 'Jones Creek', 'Ivy Log', 'Gumlog', 'Dooley', 'Coosa', 'Choestoe'], 'Paulding': [99999, 88888, 'West Ridge Church', 'Watson Govt Complex', 'Total', 'Taylor Farm Park', 'Sara Ragsdale Elem', 'Paulding Co High', 'Nebo Elem School', 'Moses Middle School', 'Hiram High School', 'Carl Scoggins Middle', 'Burnt Hickory Park', 'Austin Middle School'], 'Montgomery': ['Uvalda', 'Total', 'Tarrytown', 'Mount Vernon', 'Kibbee', 'Higgston', 'Alston'], 'Wayne': ['Vfw', 'Unity', 'Total', 'Screven', 'Red Hill', 'Rec Center', 'Pine Street', 'Oglethorpe', 'Madray Springs', 'Gardi', 'Empire', 'Altamaha'], 'Screven': [88888, 'Total', 'Sr Citizens Center', 'Screven Rec. Dept.', 'Rocky Ford', 'Newington', 'Jenk Hill Fire Sta', 'Jackson Fire Station', 'Hunters', 'Hiltonia', 'Greenhill Church', "Foy'S Store", 'Bay Branch'], 'Pickens': ['Total', 'Tate', 'Talking Rock', 'Sharptop', 'Refuge', 'Nelson', 'Ludville', 'Jerusalem', 'Jasper', 'Hinton', 'Hill', 'Appalachian'], 'Wilkinson': ['Turkey Creek', 'Total', 'Ramah', 'Midway', 'Lord', 'Ivey', 'Irwinton', 'High Hill', 'Griffin'], 'Ben Hill': [88888, 'West', 'Total'], 'Worth': [88888, 'Warwick', 'Total', 'Sylvester East', 'Sumner', 'Shingler', 'Scooterville', 'Red Rock', 'Poulan', 'Piney Woods', 'Oakfield', 'Minton', 'Isabella', 'Doles', 'County Line', 'Bridgeboro'], 'Appling': ['Total', '5B', '5A', '4D', '4B', '3C', '3A1', '2', '1C'], 'McDuffie': [99999, 88888, 'Total', '139', '137', '136', '135', '134', '133B', '133A', '132'], 'Dodge': ['Yonke', 'Vilul', 'Total', 'Rawli', 'Pondt', 'Plain', 'Mulli', 'Mitch', 'Milan', 'Mccra', 'Lee', 'Jones', 'Jaybi', 'Empir', 'Eddin', 'Clark'], 'Columbia': [99999, 'Woodlawn Bapt', 'Westside Bapt Church', 'West Acres Baptist', 'Wesley Methodist', 'Warren Baptist', 'Trinity Bapt Church', 'Total', 'Stevens Creek Elem', 'Stevens Creek', 'Second Mt. Carmel', 'Riverside Elementary', 'Redeemer Church', 'Philadelphia Church', 'Patriots Park', 'New Life Church', 'Mtz Col Fire Hdqtr.', 'Mtz Col Fire Dept #4', 'Marvin Methodist', 'Martinez Baptist', 'Liberty Park -', 'Lewis Methodist', 'Lakeside Middle', 'Journey Comm.', 'Harlem Branch', 'Grovetown Middle', 'Grovetown Methodist', 'Greenbrier High', 'Grace Baptist Church', 'Gospel Water Branch', 'Gold Cross Ems', 'Genesis Church', 'G A Apostolic Church', 'Eubank-Blanchard Ctr', 'Damascus Bapt', 'Col Cty Main Library', 'Col Cty Board Of Edu', 'Church Of Our Savior', 'Christ The King Ch', 'Christ Sanctified', 'Christ Church,', 'Blueridge Elementary', 'Blanchard Park', 'Bessie Thomas Center', 'Belair Baptist Church', 'Augusta Christian', 'Abilene Baptist'], 'Bibb': [99999, 'Warrior 2', 'Warrior 1', 'Vineville 6', 'Vineville 5', 'Vineville 4', 'Vineville 3', 'Vineville 2', 'Vineville 1', 'Total', 'Rutland 2', 'Rutland 1', 'Howard 7', 'Howard 6', 'Howard 5', 'Howard 4', 'Howard 3', 'Howard 2', 'Howard 1', 'Hazzard 4', 'Hazzard 3', 'Hazzard 2', 'Hazzard 1', 'Godfrey 5', 'Godfrey 4', 'Godfrey 3', 'Godfrey 2', 'Godfrey 1', 'East Macon 5', 'East Macon 4', 'East Macon 3', 'East Macon 2', 'East Macon 1'], 'Brooks': [99999, 88888, 'Total', 'Quitman', 'Pavo', 'Nankin', 'Morven', 'Dixie', 'Briggs', 'Barwick'], 'Cherokee': [88888, 'Woodstock', 'Woodlands', 'Wildcat', 'Waleska', 'Victoria', 'Univeter', 'Union Hill', 'Total', 'Toonigh', 'Teasley', 'Sutallee', 'Sixes', 'Salacoa', 'Rosecreek', 'R T Jones', 'R M Moore', 'Oak Grove', 'Neese', 'Mountain Road', 'Macedonia', 'Little River', 'Liberty', 'Kellogg', 'Holly Springs', 'Hillside', 'Hightower', 'Hickory Flat', 'Freehome', 'Dixie', 'Deer Run', 'Conns Creek', 'Clayton', 'Carmel', 'Canton', 'Bridgemill', 'Bradshaw', 'Booth', 'Bells', 'Bascomb', 'Ball Ground', 'Avery', 'Arnold Mill'], 'Harris': [88888, 'Whitesville', 'Waverly Hall', 'Valley Plains', 'Upper 19Th', 'Total', 'Skinner', 'Pine Mountain Valley', 'Mulberry Grove', 'Lower 19Th', 'Hamilton', 'Goodman', 'Ellerslie', 'Cataula'], 'Chattooga': [99999, 'Trion', 'Total', 'Teloga', 'Summerville', 'Subligna', 'Seminole', 'Pennville', 'Lyerly', 'Haywood', 'Dirttown', 'Dirtseller', 'Cloudland', 'Alpine'], 'Coweta': [99999, 88888, 'White Oak', 'Westside', 'Welcome', 'Turin', 'Total', 'Thomas Crossroads', 'Smokey Road', 'Sharpsburg', 'Raymond', 'Pine Road', 'Panther Creek', 'Northside', 'Newnan', 'Moreland', 'Madras', 'Jefferson Parkway', 'Haralson', 'Greentop', 'Grantville', 'Fischer Road', 'Expo Center', 'Dresden', 'Coweta Central', 'Central', 'Cedar Creek', 'Cannongate', 'Arts Centre'], 'Dougherty': [99999, 88888, 'Westtown Elem', 'Westover High', 'Turner Elem School', 'Total', 'Shiloh Baptist Churc', 'Sherwood Elem', 'Radium Middle School', 'Putney 1St Bapt Chur', 'Pine Bluff Bapt Chur', 'Phoebe Healthworks', 'Phoebe East', 'Mt Zion Center', 'Merry Acres Middle', 'Lovett Hall', 'Litman Cathedral', 'Lamar Reese Elem Sch', 'Jackson Heights Elem', 'International Studie', 'Greenbriar Church', 'Darton College', 'Covenant Church', 'Christ Church', 'Carver Teen Center', 'Bill Miller Center', 'Alice Coachman Elem', 'Albany Middle School', '2Nd Mt Zion Church', '1St Christian Church'], 'Wilcox': [99999, 88888, 'Total', 'Rochelle South #4', 'Pitts #3', 'Pineview #2', 'Abbeville South #5', 'Abbeville North #2'], 'Meriwether': ['Upper 9Th -Alvaton', 'Total', 'Third-Durand', 'Raleigh', 'Middle 9Th-Gay', 'Luthersville', 'Lower 9Th-Woodbury', 'Lone Oak', 'Gill Ii', 'Gill I', 'Cove', '8Th-Greenville', '7Th-Odessadale', '2Nd-Warm Springs'], 'Cook': ['Total', 'Sparks', 'Riverbend', 'New Life Baptist Ch.', 'Massee', 'Lenox', 'Elm Pine', 'Delle Beamguard'], 'Gordon': ['Total', 'Sonoraville', 'Resaca', 'Red Bud', 'Plainville', 'Pine Chapel', 'Oostanaula', 'Oakman', 'Lily Pond', 'Gordon County', 'Fairmount', 'Calhoun City'], 'Henry': [99999, 88888, 'Westside', 'Wesley Lakes', 'Unity Grove', 'Tussahaw', 'Total', 'Timberridge', 'Swan Lake', 'Stockbridge East-', 'Stockbridge Central', 'Stagecoach', 'South Hampton', 'Shiloh', 'Shakerag', 'Sandy Ridge', 'Red Oak', 'Pleasant Grove', 'Pates Creek', 'Oakland', 'North Hampton', 'Mt. Bethel', 'Mount Carmel', 'Mcmullen', 'Mcdonough Central', 'Mcdonough', 'Lowes', 'Locust Grove', 'Lighthouse', 'Lake Haven', 'Lake Dow', 'Kelleytown', 'Hickory Flat', 'Grove Park', 'Flippen', 'Ellenwood', 'East Lake', 'Dutchtown', 'Cotton Indian', 'Austin Road'], 'Webster': ['Total', 'Preston 1'], 'Wilkes': [99999, "Young Farmer'S Bldg", 'Total', 'Tignall Sch Lunch Rm', 'Rayle City Hall', 'Metasville Fire Sta', 'Edward B Pope Center', 'Courthouse'], 'Thomas': [99999, 88888, 'Total', 'Scott', 'Resource Center', 'Remington Esc', 'Pavo', 'Patten', 'Ochlocknee', 'New Covenant', 'Metcalfe', 'Merrilville', 'Meigs', 'Jerger', 'Harper', 'Gatlin Creek', 'Fire Station #2', 'Ellabelle', 'Douglass', 'Coolidge', 'Central', 'Boston'], 'Chatham': [99999, 88888, 'Woodville-Tompkins', 'Woodlawn Baptist', 'Windsor Hall', 'Windsor Forest', 'Wilmington Island', 'Williams Court Apts', 'White Bluff', 'West Broad Street', 'W W Law Center', 'Tybee Is Sch Cafe', 'Trinity Lutheran', 'Total', 'Tompkins Recreation', 'Thunderbolt Mun', 'The Sanctuary', 'The Light Church', 'Stillwell Towers', 'St. Thomas Episcopal', 'St Peters Episcopal', 'St Luke Church', 'Southside Fire', 'Southside Baptist Ch', 'Skidaway Island Stat', 'Skid Methodist Ch', 'Skid Is Pres Church', 'Silk Hope Baptist', 'Seventh Day Adv Chr', 'Senior Citizen Center', 'Seed Church', 'Savannah Primitive', 'Savannah Holy', 'Savannah High School', 'Savannah Commons', 'Savannah Christian S', 'Salvation Army', 'Saint Francis', 'Rothwell Baptist', 'Rose Of Sharon', 'Rice Creek School', 'Resurrection Of Our', 'Progressive Rec Ctr', 'Pooler City Hall', 'Pooler Church', 'Pb Edwards', 'Old Courthouse', 'Oglethorpe Charter', 'New Cov 7 Day Adv Ch', 'Moses Jackson', 'Lighthouse Baptist', 'Liberty City', 'Largo-Tibet Elementa', 'Lake Shore Community', 'Jonesville Bapt Ch', 'Jenkins High School', 'J E A', 'Isle Of Hope Baptist', 'Islands Christian Ch', 'Immanuel Baptist', 'Holy Spirit Lutheran', 'Hellenic Center', 'Guard House Comm', 'Grace United', 'Georgetown', 'Garden City Senior', 'Garden City Rec Ctr', 'Frank Murray', 'First Baptist Church', 'First African Baptist', 'Ferguson Ave Baptist', 'Fellowship Of Love', 'Elks Lodge', 'Eli Whitney Complex', 'Crusader Community', 'Cokesbury Methodist', 'Coastal Cathedral', 'Civic Center', 'Christ Community', 'Central Church Of', 'Carver Heights Comm', 'Butler Presbyterian', 'Butler Elementary Sc', 'Bloomingdale', 'Blackshear', 'Bible Baptist Church', 'Beach High School', 'Bartlett Middle', 'Bamboo Farms', 'Aldersgate Youth'], 'Stephens': ['Total', 'Senior Center'], 'Newton': [99999, 'Town', 'Total', 'Stansells', 'Rocky Plains', 'Oxford', 'Newborn', 'Mansfield', 'Livingston', 'Leguinn', 'Hub', 'Gum Creek', 'Fairview', 'Downs', 'Crowell', 'Covington Mills', 'Cedar Shoals', 'Buck Creek', 'Brick Store', 'Brewers', 'Beaverdam', 'Almon', 'Alcovy'], 'Bacon': ['Total', 'Douglas'], 'Hall': [88888, 'Whelchel', 'West Whelchel', 'Total', 'Tadmore', 'Roberts', 'Quillians', 'Oakwood Ii', 'Oakwood I', 'Morgan Ii', 'Morgan I', 'Lula', 'Glade', 'Gillsville', 'Gainesville V', 'Gainesville Iv', 'Gainesville Iii', 'Gainesville Ii', 'Gainesville I', 'Friendship Iv', 'Friendship Iii', 'Friendship Ii', 'Friendship I', 'Fork', 'Flowery Branch Ii', 'Flowery Branch I', 'Clermont', 'Chicopee', 'Chestatee', 'Candler', 'Big Hickory', 'Bark Camp'], 'Heard': ['Total', 'Southwest', 'Franklin', 'Ephesus', 'Enon Grove', 'Cooksville - Corinth', 'Centralhatchee'], 'Camden': [99999, 88888, 'Woodbine', 'West Saint Marys', 'West Kingsland', 'Waverly', 'Total', 'South St Marys', 'North St Marys', 'North Kingsland', 'Mush Bluff', 'Mary Lee Clark', 'Kingsland', 'Harrietts Bluff', 'East Kingsland', 'Browntown'], 'Jasper': [88888, 'Total', 'Monticello', 'Martin & Burney'], 'Effingham': [99999, 'Total', '5C', '5B', '5A', '4C', '4B', '4A', '3D', '3C', '3B', '3A', '2C', '2B', '2A', '1D', '1C', '1B'], 'Lowndes': [99999, 88888, 'Trinity', 'Total', 'S Lowndes', 'Rainwater', 'Northside', 'Naylor', 'Mildred', 'Dasher', 'Clyattville'], 'Polk': [99999, 88888, 'Youngs Grove', 'Total', 'Rockmart', 'Lake Creek', 'Fish Creek', 'Cedartown', 'Blooming Grove'], 'Warren': ['Total'], 'Jackson': [88888, 'West Jackson', 'Total', 'South Jackson', 'North Jackson'], 'McIntosh': [99999, 88888, 'Townsend', 'Total', 'South Newport', 'North Darien', 'Darien', 'Crescent'], 'Washington': [88888, 'Warthen', 'Total', 'Tennille', 'Sandersville', 'Oconee', 'Harrison', 'Deepstep', 'Davisboro'], 'Liberty': [99999, 88888, 'Walthourville', 'Town Of Allenhurst', 'Total', 'Memorial Dr. East', 'Lyman Hall School', 'Liberty County', 'Lewis Frasier School', 'Hinesville Lodge 271', 'Hinesville', 'Gum Branch', 'Fleming West', 'Fleming East', 'Button Gwinnett'], 'Lee': [99999, 'Total', '#9 Century Fire Stat', '#8 Sovereign Grace', '#7 Sda Church', '#6 First Baptist', '#5 Friendship Bapt.', '#4 Leesburg', '#3 Cjc', '#2 Smithville', '#10 Redbone', '#1 Chokee'], 'Jefferson': [99999, 88888, 'Wrens', 'Wadley', 'Total', 'Stapleton', 'Matthews', 'Louisville', 'Bartow', 'Avera'], 'Seminole': [88888, 'Total', 'Precinct 5', 'Precinct 4', 'Precinct 3', 'Precinct 2'], 'Jenkins': [99999, 88888, 'Total', 'Senior Citizens Bld', 'Perkins', 'Four Points', 'Court House'], 'White': [99999, 88888, 'White Creek', 'Town Creek', 'Total', 'Tesnatee', 'Shoal Creek', 'Robertstown', 'Nacoochee', 'Mt Yonah', 'Mossy Creek', 'Helen', 'Blue Ridge'], 'Burke': [88888, 'Vidette', 'Total', 'Telfair', 'St. Clair', 'South Waynesboro', 'Scotts Crossroads', 'Sardis', 'North Waynesboro', 'Munnerlyn', 'Midville', 'Keysville', 'Greenscut', 'Gough', 'Girard', 'Four Points', 'Blakeney'], 'Putnam': ['Total', '107', '106', '105', '104'], 'Coffee': [88888, 'West Green', 'Total', 'Nicholls', 'Douglas', 'Broxton', 'Bridgetown', 'Ambrose'], 'Glynn': [99999, 88888, 'Total', 'The Chapel', 'Sterling Ch. Of God', 'St Williams Church', 'Selden Park', 'Se Baptist Bldg', 'Satilla Marsh School', 'Oglethorpe Point', 'Northside Church', 'Marshes Of Glynn', 'Jekyll Island', 'Howard Coffin Park', 'First Baptist', 'College Place', 'Christian Renewal', 'Career Academy', 'C B Greer School', 'Burroughs Molette', 'Blythe Island Baptist', 'Ballard Community'], 'Dooly': [99999, 88888, 'Vienna', 'Unadilla', 'Total', 'Pinehurst', 'Byromville'], 'Catoosa': [99999, 'Woodstation', 'Westside', 'Total', 'Ringgold', 'Poplar Springs', 'Lakeview', 'Graysville', 'Ft Oglethorpe', 'Chambers', 'Catoosa Keith', 'Boynton', 'Blackstock'], 'Butts': [99999, 'Total', 'Butts County Admin'], 'Oconee': ['Total', 'North Oconee', 'Malcom Bridge', 'High Shoals', 'Farmington', 'Dark Corner', 'Colham Ferry', 'Civic Center', 'City Hall', 'Bogart', 'Bishop', 'Athens Academy', 'Antioch'], 'Jeff Davis': ['Whitehead 2', 'Whitehead 1', 'Total', 'Ocmulgee 2', 'Ocmulgee 1', 'Blackburn 2', 'Blackburn 1', 'Altamaha 2', 'Altamaha 1'], 'Toombs': [88888, 'Total', '514 S.T.I.A.L.C.', '513 V.P.D.', '43 Cedar Crossing', '39 Newbranch'], 'Marion': [99999, 88888, 'Total', 'Tazewell', 'Fort Perry', 'Buena Vista', 'Brantley'], 'Ware': [88888, 'Total', '409', '408', '407', '406', '405', '404', '400', '304', '300', '200B', '200A'], 'Colquitt': ['Warrior', 'Tyty', 'Total', 'Thigpen', 'Robinson', 'Norman Park', 'Murphy', 'Moultrie', 'Monk', 'Millcreek', 'Lee', 'Hopewell', 'Hartsfield', 'Hamilton', 'Funston', 'Doerun', 'Crosland', 'Bridgecreek', 'Autreyville'], 'Barrow': [99999, 88888, 'Winder-Barrow High', 'Winder Community', 'Westside Middle', 'Total', 'The Church At Winder', 'Statham Elementary', 'Midway United', 'Lions Club', 'Leisure Services', 'First Baptist Church', 'Fire Station 1', 'County Line', 'Cedar Creek Baptist', 'Bramlett Elementary', 'Bethlehem Church -', 'Apalachee High'], 'Upson': ['Town', 'Total', 'Salem', 'Redbone'], 'Schley': ['Total'], 'Johnson': ['Total', 'Smith', 'Kite', 'Bray'], 'Candler': ['Total', 'Candler - 1736'], 'Baker': ['Total', 'Newton', 'Milford', 'Hoggards Mill', 'Elmodel', 'Anna'], 'Oglethorpe': ['Total', 'Lexington', 'Crawford'], 'Irwin': [99999, 88888, 'Total', 'Ocilla', 'Holt'], 'Greene': [99999, 'White Plains', 'Union Point', 'Total', 'Siloam', 'Old Salem'], 'Bartow': [99999, 88888, 'Zena Drive', 'Woodland', 'White', 'Total', 'Taylorsville', 'Pine Log', 'Mission Road', 'Kingston', 'Folsom', 'Euharlee', 'Emerson', 'Center', 'Cassville', 'Cartersville West', 'Cartersville East', 'Allatoona'], 'Forsyth': [88888, 'Total', '29 Polo', '27 Concord', '25 Windermere', '21 South Forsyth', '19 Old Atlanta', '16 Otwell', '15 Heardsville', '10 Midway', '08 Mashburn', '07 Cumming', '06 Crossroads', '05 Coal Mountain', '04 Chestatee', '03 Browns Bridge', '02 Brandywine'], 'Clay': [99999, 88888, 'Zetto', 'Total', 'Old Head Start', 'Days Cross Road', 'Court House'], 'Fulton': [99999, 88888, 'Uc032', 'Uc031', 'Uc02B', 'Uc02A', 'Uc01E', 'Uc01D', 'Uc01B', 'Uc01A', 'Total', 'Ss31', 'Ss29A', 'Ss26', 'Ss22', 'Ss20', 'Ss19B', 'Ss19A', 'Ss18B', 'Ss18A', 'Ss17', 'Ss16', 'Ss15B', 'Ss15A', 'Ss14', 'Ss13B', 'Ss13A', 'Ss12', 'Ss11D', 'Ss11C', 'Ss11B', 'Ss11A', 'Ss09B', 'Ss09A', 'Ss08D', 'Ss08C', 'Ss08B', 'Ss08A', 'Ss07C', 'Ss07B', 'Ss07A', 'Ss06', 'Ss05', 'Ss04', 'Ss03', 'Ss02B', 'Ss02A', 'Ss01', 'Sc30B', 'Sc30A', 'Sc29A', 'Sc27', 'Sc23C', 'Sc23B', 'Sc23A', 'Sc212', 'Sc211', 'Sc20', 'Sc19B', 'Sc19A', 'Sc18C', 'Sc18B', 'Sc18A', 'Sc17C', 'Sc17B', 'Sc17A', 'Sc16B', 'Sc16A', 'Sc15', 'Sc14B', 'Sc14A', 'Sc13', 'Sc11B', 'Sc11A', 'Sc10', 'Sc09C', 'Sc09B', 'Sc09A', 'Sc08H', 'Sc08G', 'Sc08F', 'Sc08E', 'Sc08D', 'Sc08C', 'Sc08B', 'Sc07C', 'Sc07A', 'Sc05E', 'Sc05D', 'Sc05B', 'Sc05A', 'Sc04', 'Sc02', 'Sc01D', 'Sc01C', 'Sc01B', 'Sc01A', 'Rw22A', 'Rw21', 'Rw20', 'Rw19', 'Rw17', 'Rw16', 'Rw13', 'Rw12', 'Rw11A', 'Rw10', 'Rw09', 'Rw08', 'Rw07B', 'Rw07A', 'Rw06', 'Rw05', 'Rw04', 'Rw03', 'Rw02', 'Rw01', 'Pa01', 'Mp01', 'Ml07A', 'Ml072', 'Ml071', 'Ml06B', 'Ml06A', 'Ml05C', 'Ml05B', 'Ml05A', 'Ml04C', 'Ml04B', 'Ml04A', 'Ml03', 'Ml024', 'Ml023', 'Ml022', 'Ml021', 'Ml01B', 'Ml012', 'Ml011', 'Jc19', 'Jc18', 'Jc16', 'Jc15', 'Jc14', 'Jc13B', 'Jc13A', 'Jc12', 'Jc11', 'Jc10', 'Jc09', 'Jc08', 'Jc07', 'Jc06', 'Jc05', 'Jc04B', 'Jc04A', 'Jc03B', 'Jc03A', 'Jc02', 'Jc01', 'Hp01', 'Fa01C', 'Fa01B', 'Fa01A', 'Ep04B', 'Ep04A', 'Ep03B', 'Ep03A', 'Ep02E', 'Ep02D', 'Ep02C', 'Ep02B', 'Ep02A', 'Ep01B', 'Ep01A', 'Cp08A', 'Cp084', 'Cp083', 'Cp081', 'Cp07F', 'Cp07E', 'Cp07D', 'Cp07C', 'Cp07B', 'Cp06A', 'Cp05B', 'Cp051', 'Cp04B', 'Cp04A', 'Cp02', 'Cp01B', 'Cp012', 'Cp011', 'Ch05', 'Ch04A', 'Ch03', 'Ch02', 'Ch01', 'Ap14', 'Ap12C', 'Ap12B', 'Ap12A', 'Ap10', 'Ap09B', 'Ap09A', 'Ap07B', 'Ap07A', 'Ap06', 'Ap05', 'Ap04B', 'Ap04A', 'Ap03', 'Ap02B', 'Ap022', 'Ap021', 'Ap01D', 'Ap01C', 'Ap01B', 'Ap01A', '12S', '12N', '12M', '12L', '12K', '12J', '12I', '12H2', '12H1', '12G', '12F', '12E1', '12D', '12A', '11R', '11P', '11N', '11M', '11K', '11J', '11H', '11G', '11E3', '11E2', '11E1', '11C', '11B', '10R', '10P', '10M', '10K', '10J', '10I', '10H2', '10H1', '10G', '10F', '10E', '10D', '10C', '10B', '10A', '09M', '09K', '09I', '09H', '09G', '09F', '09E', '09D', '09C', '09B', '09A', '08P', '08N2', '08N1', '08M', '08L', '08K', '08J', '08H', '08G', '08F1', '08E', '08D', '08C', '08B', '08A', '07N', '07M', '07J', '07H', '07F', '07E', '07D', '07C', '07B', '07A', '06R', '06Q', '06N', '06L2', '06L1', '06J', '06I', '06G', '06F', '06E', '06D', '06B', '05K', '05J', '05F', '05D', '05C', '05B', '05A2', '05A1', '04X2', '04X1', '04W', '04V', '04T', '04S', '04M', '04L', '04K', '04J', '04I', '04G', '04F', '04D', '04C', '04B', '04A', '03T', '03S', '03P2', '03P1A', '03N', '03M', '03L', '03I', '03H', '03G', '03F', '03E', '03D', '03C', '03B', '03A', '02W', '02S', '02L2', '02L1', '02K', '02J', '02G', '02F2', '02F1', '02E', '02D', '02C', '02B', '02A', '01T', '01S', '01R', '01P', '01J', '01I', '01H', '01G', '01F', '01E', '01D', '01C', '01B', '01A'], 'Macon': [88888, 'Total', 'Oglethorpe', 'Montezuma #5', 'Montezuma #4', 'Marshallville'], 'Madison': ['Total', 'Poca', 'Pittman', 'Paoli', 'Mill', 'Ila', 'Hull', 'Harrison', 'Fork', 'Danielsville', 'Comer', 'Collins'], 'Taylor': [88888, 'Total', 'Precinct 6', 'Precinct 5'], 'Evans': [99999, 'Total'], 'Clinch': ['Total', 'Homerville', 'Fargo', 'Dupont', 'Argyle', 'Arabia'], 'Charlton': ['Winokur', 'Total', 'St. George', 'Racepond', 'Homeland', 'Ga Bend', 'Folkston Fire', 'American Legion'], 'Echols': [99999, 88888, 'Total'], 'Grady': ['Woodland', 'Whigham', 'Total', 'Spring Hill', 'Spence', 'Ragan', 'Pine Park', 'Midway', 'Limesink', 'Higdon', 'Duncanville', 'Cairo 5Th Distr', 'Cairo 4Th Distr'], 'Dawson': [99999, 'Total', 'East', 'Central'], 'Hart': ['Total', 'Shoal Creek', 'Reed Creek', 'Goldmine', 'Cokesbury', 'Bowersville', 'Bio'], 'Baldwin': [88888, 'West Hardwick', 'West Baldwin', 'Total', 'South Milledgeville', 'North Milledgeville', 'North Baldwin', 'Meriweather', 'Fire Dept', 'East Hardwick', 'East Baldwin', 'Courthouse', 'Coopers', 'City Hall Annex', 'Boddie'], 'Lumpkin': ['Total', 'Dahlonega'], 'Lanier': [88888, 'Total'], 'Haralson': ['Waco', 'Twentieth', 'Total', 'Tallapoosa', 'Seventh', 'Mt View', 'Little Creek', 'Felton', 'Corinth', 'Buncombe', 'Buchanan', 'Berea-Steadman'], 'Rockdale': ['Total', 'St', 'Sp', 'Sm', 'Ro', 'Ot', 'Mi', 'Ma', 'Lo', 'La', 'Hi', 'Hc', 'Fs', 'Fi', 'Co', 'Bt', 'Ba'], 'Elbert': ['Wyche', 'Webbsboro', 'Total', 'Pike', 'Petersburg', 'Moss-Ruckersville', 'Longstreet', 'Goshen', 'Gaines', 'Eliam', 'Centerville'], 'Decatur': ['West Bainbridge', 'Total', 'Recovery', 'Kendrick', 'Climax', 'Brinson', 'Bdge-Fairgrounds', 'Bainbridge-Coliseum', 'Attapulgus'], 'Clarke': [99999, 88888, 'Total', '8C', '8B', '8A', '7C', '7B', '7A', '6D', '6C', '6B', '6A', '5D', '5C', '5B', '5A', '4B', '4A', '3B', '3A', '2B', '2A', '1D', '1C', '1B'], 'Richmond': [99999, 88888, 'Total', '810', '809', '808', '807', '806', '805', '804H', '804', '803', '802', '801B', '801', '709', '708', '707', '706', '705', '703', '702', '701', '608', '607', '605', '604', '603', '601', '509', '507', '506', '504', '503', '502', '501', '406', '405', '404', '402', '401', '310', '309', '308', '307', '306', '305', '304', '303', '302', '301', '210', '208', '207', '204', '203', '202', '201', '115', '114', '112', '111', '109', '108', '107', '106', '105', '104', '103', '102'], 'Lamar': [88888, 'Total', 'Senior Citizen Bldg', 'Redbone', 'Milner', 'L C S C', 'Chappell Mill V. Fd'], 'Cobb': [88888, 'Willeo 01', 'Wade Green 02', 'Vinings 04', 'Vinings 03', 'Vinings 02', 'Vinings 01', 'Vaughan 01', 'Total', 'Timber Ridge 01', 'Terrell Mill 01', 'Sweetwater 02', 'Sweetwater 01', 'Sope Creek 03', 'Sope Creek 02', 'Sope Creek 01', 'Smyrna 7A', 'Smyrna 6A', 'Smyrna 5A', 'Smyrna 4A', 'Smyrna 3A', 'Smyrna 2A', 'Smyrna 1A', 'Simpson 01', 'Shallowford Falls 01', 'Sewell Mill 03', 'Sewell Mill 01', 'Sandy Plains 01', 'Roswell 02', 'Roswell 01', 'Rocky Mount 01', 'Riverside 01', 'Powers Ferry 01', 'Powder Springs 3A', 'Powder Springs 2A', 'Powder Springs 1A', 'Post Oak 01', 'Pope 01', 'Pitner 01', 'Pine Mountain 02', 'Pine Mountain 01', 'Pebblebrook 01', 'Palmer 01', 'Oregon 05', 'Oregon 04', 'Oregon 03', 'Oregon 02', 'Oregon 01', 'Oakdale 01', 'Norton Park 01', 'North Cobb 01', 'Nickajack 01', 'Nicholson 01', 'Murdock 01', 'Mt Bethel 04', 'Mt Bethel 03', 'Mt Bethel 01', 'Mceachern 01', 'Mcclure 01', 'Mccleskey 01', 'Mars Hill 02', 'Mars Hill 01', 'Marietta 7A', 'Marietta 6B', 'Marietta 6A', 'Marietta 5B', 'Marietta 5A', 'Marietta 4C', 'Marietta 4B', 'Marietta 4A', 'Marietta 3A', 'Marietta 2B', 'Marietta 2A', 'Marietta 1A', 'Macland 01', 'Mabry 01', 'Mableton 04', 'Mableton 03', 'Mableton 02', 'Mableton 01', 'Lost Mountain 04', 'Lost Mountain 03', 'Lost Mountain 02', 'Lost Mountain 01', 'Lindley 01', 'Lassiter 01', 'Kennesaw 5A', 'Kennesaw 4A', 'Kennesaw 3A', 'Kennesaw 2A', 'Kennesaw 1A', 'Kemp 03', 'Kemp 02', 'Kemp 01', 'Kell 01', 'Hightower 01', 'Hayes 01', 'Harrison 01', 'Harmony-Leland 01', 'Gritters 01', 'Garrison Mill 01', 'Fullers Park 01', 'Frey 01', 'Ford 01', 'Fair Oaks 04', 'Fair Oaks 02', 'Elizabeth 05', 'Elizabeth 04', 'Elizabeth 03', 'Elizabeth 02', 'Elizabeth 01', 'Eastside 02', 'Eastside 01', 'East Piedmont 01', 'Durham 01', 'Dowell 01', 'Dodgen 01', 'Dobbins 01', 'Dickerson 01', 'Davis 01', 'Cooper 01', 'Clarkdale 02', 'Clarkdale 01', 'Chestnut Ridge 01', 'Cheatham Hill 03', 'Cheatham Hill 02', 'Chattahoochee 01', 'Chalker 01', 'Bryant 02', 'Bryant 01', 'Blackwell 01', 'Birney 02', 'Birney 01', 'Big Shanty 02', 'Big Shanty 01', 'Bells Ferry 03', 'Bells Ferry 02', 'Baker 01', 'Austell 1A', 'Addison 01', 'Acworth 1C', 'Acworth 1B', 'Acworth 1A'], 'Morgan': [99999, 88888, 'Total', '7. North Morgan', '6. West Morgan', '5. Clacks Chapel', '4. Central Morgan', '3. Beth-Springfield', '2. East Morgan'], 'Glascock': ['Total', 'Mitchell', 'Mill', 'Gibson', 'Edgehill'], 'Treutlen': [99999, 'Total', 'Soperton', 'Annex'], 'Walton': [99999, 'Whatley', 'West Walton', 'Walnut Grove', 'Walker Park', 'W Monroe', 'Total', 'Tara', 'South Monroe', 'Social Circle', 'North Monroe', 'Mountain', 'Loganville South', 'Loganville North', 'Jersey', 'Gratis', 'Good Hope', 'E Monroe', 'Broken Arrow', 'Bold Springs', 'Blasingame', 'Between', 'Bay Creek'], 'Muscogee': [99999, 88888, 'Wynnbrook', 'Total', 'St. Peter', 'St Paul-Clubview', 'St Mark-Heiferhorn', 'St John-Belvedere', 'St Andrews-Midland', 'Salvation Army', 'Rothschild', 'Psalmond-Mathews', 'Our Lady Of Lourdes', 'Mt Pilgrim', 'Moon-Morningside', 'Marianna Gallops', 'Gentian-Reese @Lds', 'Fort-Waddell', 'First African', 'Faith Tabernacle', 'Epworth Umc', 'Edgewood Baptist', 'Cusseta Rd', 'Cornerstone', 'Columbus Tech', 'Carver-Mack', 'Britt David'], 'Wheeler': [88888, 'Total', 'Glenwood'], 'Fayette': [88888, 'Woolsey', 'Windgate', 'Willowbend', 'Willow Pond', 'Whitewater', 'Total', 'Starrsmill', 'Spring Hill', 'Shakerag West', 'Shakerag East', 'Sandy Creek', 'Rising Star', 'Rareover', 'Oak Ridge', 'Oak Grove', 'Murphy', 'Morning Creek', 'Mcintosh', 'Kenwood', 'Kedron', 'Jeff Davis', 'Hopeful', 'Harps Crossing', 'Flint', 'Flat Creek', 'Fielding Ridge', 'Fayetteville West', 'Fayetteville East', 'Europe', 'Dogwood', 'Camp Creek', 'Brooks', 'Braelinn', 'Banks', 'Antioch', 'Aberdeen'], 'Early': ['Urquhart', 'Total', 'Cuba', 'Cedar Springs', 'Blakely', 'Arlington'], 'Floyd': [88888, 'West Lindale', 'Watters', 'Vanns Valley', 'Town Rome', 'Total', 'Texas Valley', 'South Rome', 'Riverside', 'North Rome', 'North Carolina', 'Mt Alto South', 'Mt Alto North', 'Howell', 'Glenwood', 'Garden Lakes', "Foster'S Mill", 'Floyd Springs', 'Everett Springs', 'Etowah', 'East Rome', 'East Lindale', 'Chulio', 'Cave Spring', 'Barkers', 'Armuchee'], 'Chattahoochee': [99999, 88888, 'Total'], 'Towns': [99999, 88888, 'Total', 'Tate City', 'Macedonia', 'Hiawassee'], 'Bryan': [88888, 'Ways Station', 'Total', 'Rh Recreation Compx', 'Public Safety Compx', 'Keller', 'J.F.Gregory Park', 'Hwy 144 East', 'Ellabell', 'Danielsiding', 'Black Creek'], 'Lincoln': [88888, 'Total', 'Tabernacle', 'Martins Crossroad', 'Lincoln Club House', 'Lincoln Center', 'Faith Temple Of Linc', 'Bethany Church'], 'Dade': [99999, 88888, 'West Brow', 'Trenton', 'Total', 'North Dade', 'New Salem', 'New Home', 'Davis'], 'Franklin': [99999, 'West Franklin', 'Total', 'Southwest Franklin', 'Royston', 'Northeast Franklin', 'Lavonia', 'Canon'], 'Walker': [99999, 'Walnut Grove', 'Total', 'Rossville', 'Rock Spring', 'Mountain', 'Kensington', 'Fairyland', 'Fairview', 'Chickamauga', 'Chattanooga Valley', 'Armuchee Valley'], 'Terrell': ['Total', 'Sasser', 'Parrott', 'Herod-Dover', 'Graves', 'Bronwood'], 'Carroll': [99999, 88888, 'Whitesburg', 'West Carrollton', 'Villa Rica City', 'V R County South', 'V R County North', 'University Of W. Ga', 'Tyus', 'Total', 'Temple County', 'Temple City', 'Tabernacle Church', 'Sandhill', 'Roopville', 'Old Camp Church', 'Oak Grove', 'Mt Zion', 'Lakeshore Rec Center', 'Hulett', 'Fairfield', 'County Admin Bldg', 'Clem', 'Center Point', 'Burwell', 'Burson Center', 'Bowdon Junction', 'Bowdon', 'Bonner', 'Bethany'], 'Murray': [88888, 'Town', 'Total', 'Spring Place', 'Southwest', 'Shuck Pen', 'North', 'Carters-Doolittle'], 'Talbot': ['Valley', 'Total', 'Talbotton', 'Junction City', 'Geneva', 'Flint Hill', 'Box Springs'], 'Tift': [99999, 'Ty Ty', 'Total', 'Tifton South', 'Tifton Northwest', 'Tifton Lodge', 'Omega', 'Mott-Litman Gym', 'Eldorado', 'Docia', 'Chula', 'Brookfield', 'Brighton'], 'Peach': [99999, 'Total', 'Powersville', 'Fort Valley #3', 'Fort Valley #2', 'Fort Valley #1', 'Claude', 'Byron #2', 'Byron #1'], 'Pike': [88888, 'Zebulon', 'Williamson', 'Total', 'Second District', 'Molena', 'Meansville', 'Lifsey Springs', 'Hollonville'], 'Sumter': [88888, 'Total', 'Thomson', 'Rees Park', 'Rec Dept', 'Plains', 'Gsw Conf Center', 'Concord', 'Chambliss', 'Andersonville', 'Airport', 'Ag Center'], 'Calhoun': ['Total', 'Morgan', 'Edison-Arlington', 'Edison', 'Arlington'], 'Douglas': [99999, 88888, 'Winston', 'Turner', 'Total', 'Stewart', 'St Julians Episcopal', 'Prays Mill Gym', 'Old Courthouse', 'Lutheran Church - Gs', 'Lithia Springs High', 'Golden Methodist Ch', 'First Baptist Lithia', 'First Baptist', 'Factory Shoals', 'Ephesus Baptist Chur', 'Dorsett Shoals', 'Dog River Library', 'Deer Lick', 'Colonial Hills', 'Church At Chapel Hill', 'Chestnut Log', 'Chapel Hill', 'Bright Star', 'Boundary Waters', 'Beulah Baptist', 'Arbor Station'], 'Pulaski': ['Total', 'Courthouse Annex'], 'Atkinson': [99999, 88888, 'Willacoochee', 'Total', 'Pearson City', 'Axson'], 'DeKalb': [99999, 'Young Road', 'Wynbrooke Elem', 'Woodward', 'Woodrow Road', 'Woodridge Elem', 'Winters Chapel', 'Winnona Park', 'White Oak', 'Wesley Chapel', 'Warren Tech', 'Wadsworth', 'Valley Brook', 'Tucker Library', 'Tucker', 'Total', 'Toney Elem', 'Tilly Mill Road', 'Terry Mill', 'Stoneview Elem', 'Stonecrest Library', 'Stone Mtn Champion', 'Stone Mtn', 'Stone Mountain Elem', 'Stone Mill Elem', 'Stn Mtn Middle', 'Stephenson Middle', 'Stephenson High', 'South Hairston', 'South Deshon', 'Snapfinger Road S', 'Snapfinger Road N', 'Snapfinger Elem', 'Smoke Rise', 'Skyland', 'Silver Lake', 'Shaw-Robert Shaw', 'Shamrock', 'Shadow Rock Elem', 'Scott', 'Salem Middle', 'Sagamore Hills Elem', 'Rowland Road', 'Rowland Elem', 'Rockbridge Road', 'Rockbridge Elem', 'Rock Chapel Road', 'Rock Chapel Elem', 'Renfroe', 'Rehoboth', 'Redan-Trotti Library', 'Redan Road', 'Redan Middle', 'Redan Elem', 'Rainbow Elem', 'Princeton Elem', 'Ponce De Leon', 'Pleasantdale Road', 'Piney Grove', 'Pine Lake', 'Peachtree Middle', 'Peachcrest', 'Panola Way Elem', 'Panola Road', 'Panola', 'Oakhurst', 'Oakcliff Elem', 'Oak View Elem', 'Oak Grove Elem', 'Northlake', 'North Peachtree', 'North Hairston', 'North Decatur', 'Narvie J Harris Elem', 'Mount Vernon West', 'Mount Vernon East', 'Montreal', 'Montgomery Elem', 'Montclair Elem', 'Miller-Eldridge L', 'Miller Grove Road', 'Miller Grove High', 'Miller Grove', 'Midway', 'Midvale Road', 'Midvale Elem', 'Metropolitan', 'Memorial South', 'Medlock', 'Meadowview', 'Mcwilliams', 'Mcnair High', 'Mcnair Academy', 'Mcnair', 'Mclendon', 'Mathis-Bob Mathis', 'Marbut Elem', 'Livsey Elem', 'Lithonia High', 'Lithonia', 'Lin-Mary Lin Elem', 'Lavista Road', 'Lavista', 'Lakeside High', 'Knollwood', 'Kittredge Elem', 'Kingsley Elem', 'King-Ml King Jr High', 'Kelley Lake Elem', 'Kelley Chapel Road', 'Jolly Elem', 'Johnson Estates', 'Indian Creek', 'Idlewood Elem', 'Huntley Hills Elem', 'Hugh Howell', 'Henderson Mill', 'Hawthorne Elem', 'Harris-Margaret', 'Hambrick Elem', 'Gresham Road', 'Glenwood Road', 'Glennwood', 'Glenhaven', 'Georgetown Sq', 'Freedom Middle', 'Flat Shoals Parkway', 'Flat Shoals Library', 'Flat Shoals Elem', 'Flat Shoals', 'Flat Rock Elem', 'Flakes Mill Fire', 'Fernbank Elem', 'Fairington Elem', 'Evansdale Elem', 'Epworth', 'Emory South', 'Emory Road', 'Embry Hills', 'East Lake', 'Dunwoody Library', 'Dunwoody 2', 'Dunwoody', 'Dunaire Elem', 'Druid Hills High', 'Dresden Elem', 'Doraville South', 'Doraville North', 'Crossroads', 'Cross Keys High', 'Covington Hwy', 'Covington', 'Coralwood', 'Columbia Middle', 'Columbia Elem', 'Columbia Drive', 'Coan Recreation', 'Clifton', 'Clarkston', 'Clairmont Road', 'Clairemont West', 'Clairemont East', 'Chesnut Elem', 'Chapel Hill Elem', 'Chamblee 2', 'Chamblee', 'Cedar Grove South', 'Cedar Grove Middle', 'Cedar Grove Elem', 'Candler-Murphey', 'Candler', 'Canby Lane Elem', 'Burgess Elem', 'Browns Mill Elem', 'Brookhaven', 'Brockett Elem', 'Brockett', 'Briarwood', 'Briarlake Elem', 'Briarcliff', 'Briar Vista Elem', 'Boulevard', 'Bouldercrest Road', 'Bethune Middle', 'Avondale High', 'Avondale', 'Austin Drive', 'Austin', 'Ashford Parkside', 'Ashford Park Elem', 'Ashford Dunwoody Rd', 'Allgood Elem'], 'Crisp': ['Total', 'Listonia', 'Jamestown', 'Cordele', 'Coney', 'Arabi'], 'Troup': [99999, 88888, 'West Point', 'Total', 'Rosemont', 'Northside', 'Mountville', 'Mclendon', 'Long Cane', 'Hogansville', 'Highland', 'Hammett Rd', 'Griggs Center', 'Gray Hill', 'Gardner Newman', 'East Vernon', 'Administration Bldg'], 'Crawford': [88888, 'Total', 'District 5', 'District 4', 'District 3', 'District 2', 'District 1B'], 'Long': [99999, 88888, 'Total', 'Tibet', 'South Ludowici', 'Rye Patch-Oak Dale', 'North Ludowici', 'Faith Baptist Annex', 'Alma Flournoy'], 'Gilmer': [99999, 88888, 'Yukon', 'Town Creek', 'Total', 'Tails Creek', 'Mountaintown', 'Leaches', 'Ellijay Northeast', 'Ellijay North', 'East Ellijay', 'Cherry Log', 'Cartecay', 'Boardtown', 'Big Creek'], 'Bleckley': [99999, 88888, 'Total'], 'Gwinnett': [88888, 'Total', 'Suwanee H', 'Suwanee G', 'Suwanee F', 'Suwanee E', 'Suwanee D', 'Suwanee C', 'Suwanee B', 'Suwanee A', 'Sugar Hill G', 'Sugar Hill F', 'Sugar Hill E', 'Sugar Hill D', 'Sugar Hill C', 'Sugar Hill B', 'Sugar Hill A', 'Rockycreek C', 'Rockycreek B', 'Rockycreek A', 'Rockbridge G', 'Rockbridge F', 'Rockbridge E', 'Rockbridge D', 'Rockbridge C', 'Rockbridge B', 'Rockbridge A', 'Pucketts E', 'Pucketts D', 'Pucketts C', 'Pucketts B', 'Pucketts A', 'Pinkcneyville A', 'Pinckneyville Z', 'Pinckneyville Y', 'Pinckneyville X', 'Pinckneyville W', 'Pinckneyville V', 'Pinckneyville U', 'Pinckneyville T', 'Pinckneyville S', 'Pinckneyville Q', 'Pinckneyville P', 'Pinckneyville O', 'Pinckneyville N', 'Pinckneyville M', 'Pinckneyville L', 'Pinckneyville K', 'Pinckneyville J', 'Pinckneyville I', 'Pinckneyville H', 'Pinckneyville F', 'Pinckneyville E', 'Pinckneyville D', 'Pinckneyville C', 'Pinckneyville B', 'Pinckneyville A1', 'Martins K', 'Martins J', 'Martins I', 'Martins H', 'Martins G', 'Martins F', 'Martins E', 'Martins D', 'Martins C', 'Martins B', 'Martins A', 'Lawrenceville N', 'Lawrenceville M', 'Lawrenceville L', 'Lawrenceville K', 'Lawrenceville J', 'Lawrenceville I', 'Lawrenceville H', 'Lawrenceville G', 'Lawrenceville F', 'Lawrenceville E', 'Lawrenceville D', 'Lawrenceville C', 'Lawrenceville B', 'Lawrenceville A', 'Hog Mountain D', 'Hog Mountain C', 'Hog Mountain B', 'Hog Mountain A', 'Harbins C', 'Harbins B', 'Goodwins I', 'Goodwins H', 'Goodwins G', 'Goodwins F', 'Goodwins E', 'Goodwins D', 'Goodwins C', 'Goodwins B', 'Goodwins A', 'Garners F', 'Garners D', 'Garners C', 'Garners B', 'Garners A', 'Duncans D', 'Duncans C', 'Duncans B', 'Duncans A', 'Duluth K', 'Duluth I', 'Duluth H', 'Duluth G', 'Duluth F', 'Duluth E', 'Duluth D', 'Duluth C', 'Duluth B', 'Duluth A', 'Dacula', 'Cates O', 'Cates N', 'Cates M', 'Cates L', 'Cates K', 'Cates J', 'Cates I', 'Cates H', 'Cates G', 'Cates F', 'Cates E', 'Cates D', 'Cates C', 'Cates B', 'Cates A', 'Berkshire Q', 'Berkshire P', 'Berkshire O', 'Berkshire N', 'Berkshire M', 'Berkshire L', 'Berkshire J', 'Berkshire H', 'Berkshire G', 'Berkshire F', 'Berkshire E', 'Berkshire D', 'Berkshire B', 'Berkshire A', 'Baycreek K', 'Baycreek J', 'Baycreek I', 'Baycreek H', 'Baycreek G', 'Baycreek F', 'Baycreek E', 'Baycreek D', 'Baycreek C', 'Baycreek B', 'Baycreek A'], 'Clayton': [99999, 'Total', 'Riverdale 9', 'Riverdale 8', 'Riverdale 7', 'Riverdale 6', 'Riverdale 5', 'Riverdale 4', 'Riverdale 3', 'Riverdale 2', 'Riverdale 12', 'Riverdale 11', 'Riverdale 10', 'Riverdale 1', 'Panhandle 2', 'Panhandle 1', 'Oak 4', 'Oak 3', 'Oak 2', 'Oak 1', 'Morrow 9', 'Morrow 8', 'Morrow 7', 'Morrow 6', 'Morrow 5', 'Morrow 4', 'Morrow 3', 'Morrow 2', 'Morrow 1', 'Lovejoy 5', 'Lovejoy 4', 'Lovejoy 3', 'Lovejoy 2', 'Lovejoy 1', 'Lake City', 'Jonesboro 9', 'Jonesboro 8', 'Jonesboro 7', 'Jonesboro 6', 'Jonesboro 5', 'Jonesboro 4', 'Jonesboro 3', 'Jonesboro 2', 'Jonesboro 18', 'Jonesboro 17', 'Jonesboro 16', 'Jonesboro 15', 'Jonesboro 14', 'Jonesboro 13', 'Jonesboro 12', 'Jonesboro 11', 'Jonesboro 10', 'Jonesboro 1', 'Forest Park 6', 'Forest Park 5', 'Forest Park 4', 'Forest Park 3', 'Forest Park 2', 'Forest Park 1', 'Ellenwood'], 'Brantley': [88888, 'Waynesville', 'Total', 'Nahunta'], 'Quitman': ['Total', 'Morris', 'Georgetown'], 'Hancock': [99999, 88888, 'Youth Center', 'Warren Chapel', 'Total', 'St. Mark', 'Sparta 4C', 'Second Darrien', 'Second Beulah', 'Power Of God', 'Mayfield Community', 'Courthouse'], 'Jones': ['Total', 'Sanders', 'Roberts', 'Pope', 'Hawkins', 'Finney', 'Ethridge', 'Davidson', 'Clinton', 'Barron'], 'Pierce': [99999, 88888, 'Total', 'Sunset-Sweat', 'St Johns-Blackshear', 'Patterson', 'Otter Creek', 'Mershon', 'Blackshear', 'Alabaha'], 'Laurens': [99999, 88888, 'W T Adams Fire Sta #18', 'Total', 'Smith', 'Rural Fire Sta #17', 'Reedy Springs', 'Minter', 'Lcfs #10', 'Harvard', 'Hampton Mill', 'Fire Dept Sta #5', 'Dudley', 'Calhoun Park', 'Cadwell', 'Burch', 'Buckeye', 'Brewton'], 'Berrien': [88888, 'Total', 'Ray City', 'Nashville', 'Enigma', 'Alapaha'], 'Taliaferro': ['Total', 'Crawfordville'], 'Emanuel': [88888, 'Twin City', 'Total', 'Swainsboro', 'Summertown', 'Stillmore', 'Nunez', 'Garfield', 'Cross-Green', 'Canoochee', 'Blundale', 'Adrian'], 'Telfair': [99999, 'Total', 'Scotland', 'Milan', 'Mcrae', 'Lumber-City', 'Jacksonville', 'Helena'], 'Banks': [88888, 'Wilmonts', 'Washington', 'Total', 'Poplar Springs', 'Homer', 'Hollingsworth', 'Grove River', 'Golden Hill', 'Davids', 'Columbia', 'Bushville', 'Berlin', 'Baldwin'], 'Mitchell': ['Total', 'Sale City', 'Pelham', 'Pebble City', 'Lester', 'Hopeful', 'Hinsonton', 'Cotton', 'Camilla South', 'Camilla North', 'Branchville', 'Baconton'], 'Stewart': [99999, 88888, 'Total', 'Omaha', 'Lumpkin', 'Louvale'], 'Houston': [99999, 88888, 'Vhs', 'Twpk', 'Total', 'Tms', 'Rozr', 'Recr', 'Nses', 'Mcms', 'Hhpc', 'Hefs', 'Hctc', 'Hafs', 'Fmms', 'Cgtc', 'Cent', 'Bms', 'Annx'], 'Whitfield': ['Ws', 'Va', 'Ut', 'Tr', 'Total', 'Ti', 'Th', 'Pg', 'Ni', 'Mc', 'Lt', 'Gl', 'Fi', 'Es', 'Dg', 'Co', 'Ca', 'An', '6A', '5A', '4A', '3A', '2A'], 'Spalding': [99999, 88888, 'Total', '21', '20', '19', '17', '16', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '03', '02'], 'Miller': [88888, 'Total'], 'Habersham': [99999, 88888, 'Town Of Mount Airy', 'Total', 'Mud Creek', 'Habersham South', 'Demorest', 'City Of Baldwin', 'Amys Creek'], 'Rabun': ['Total'], 'Bulloch': [99999, 88888, 'Total', 'Stilson', 'Statesboro', 'Sinkhole', 'Register', 'Portal', 'Pittman Park', 'Nevils', 'Leefield', 'Hagin', 'Fair', 'Emit', 'Church', 'Brooklet', 'Blitch', 'Bay'], 'Fannin': ['Total', 'Toccoa', 'Sugar Creek', 'Skeniah', 'Noontootla', 'Morganton', 'Mobile', 'Mineral Bluff', 'Hothouse', 'Hemptown', 'Flinthill', 'Fairplay', 'Colwell'], 'Tattnall': ['Total', 'Shiloh', 'Manassas', 'East Glennville', 'District V', 'District Iv', 'District Ii', 'Collins'], 'Turner': ['Total', 'Sycamore', 'Rebecca'], 'Twiggs': [99999, 'Total', 'Shady Grove-Tarvers', 'Jeffersonville-Ware', 'Higgsville', 'Golden Isles', 'Dry Branch'], 'Randolph': ['Total', 'Springvale', 'Shellman', 'Fountain Bridge', 'Cuthbert-Courthouse', 'Cuthbert', 'Carnegie', 'Benevolence', '4Th District'], 'Monroe': [88888, 'Total', 'Russellville', 'Proctors', 'Middlebrooks', 'Kelseys', 'High Falls', 'Forsyth', 'Evers', 'Dillards', 'Culloden', 'Cox', 'Cabaniss', 'Burgays', 'Brantleys']}
	
	print 'DONE WITH STATEWIDE'

	#AYYYYYYrace_vs_gender_combiner(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,county)),county,'general')

	for county in ga_counties:
		if county.title() in ga_precincts.keys():
			for precinct in ga_precincts[county.title()]:
				#race_vs_inter_year_precinct(county,precinct)
				#gender_vs_inter_year_precinct(county,precinct)
				pass
		else:
			for precinct in ga_precincts[county[0].upper()+county[1].lower()+county[2].upper()+county[3:].lower()]:
				#race_vs_inter_year_precinct(county,precinct)
				#gender_vs_inter_year_precinct(county,precinct)
				pass

	for county in ga_counties:
		print county
		#precinct_vs_inter_year(county)
		gender_vs_race_precinct(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_registered.csv'.format(year,election_type,county)),county,'general')
		gender_vs_race_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,county)),county,'general')
		race_combiner_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_registered.csv'.format(year,election_type,county)),county,'general')
		gender_combiner_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_precincts_total_registered.csv'.format(year,election_type,county)),county,'general')
		gender_vs_age_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,county)),county,'general')
		race_vs_age_county(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_voted.csv'.format(year,election_type,county)),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,county)),county,'general')
		#race_vs_inter_year_county(county)
		#gender_vs_inter_year_county(county)
		#age_vs_inter_year_county(county)

	for congressional_district in range(1,15):
		gender_vs_race_congressional(year,election_type,pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/US{}_total_voted.csv'.format(year,election_type,str(congressional_district).zfill(2))),pd.read_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/US{}_total_registered.csv'.format(year,election_type,str(congressional_district).zfill(2))),congressional_district,'general')
		#race_vs_inter_year_congressional(congressional_district)
		#gender_vs_inter_year_congressional(congressional_district)
		pass

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
#table_calculator('Primary_Runoff','2014')
#table_calculator('Primary','2014')
#table_calculator('General','2014')
table_calculator('Primary_Runoff','2016')
table_calculator('Primary','2016')
table_calculator('General','2016')
table_calculator('Presidential_Primary','2016')
table_calculator('Primary_Runoff','2018')
#table_calculator('Primary','2018')
#table_calculator('General','2018')

#codeString = which_table_to_display(parameters.getvalue("x-axis"),parameters.getvalue("y-axis"),parameters.getvalue("z-axis"),parameters.getvalue("region_1"),parameters.getvalue("region_2"),parameters.getvalue("election_type"),parameters.getvalue("election_year"))

returnData = {
	"data": codeString
}
self.response.out.write(json.dumps(returnData))

#CONG district vs year; region vs year
#age vs county problem is selector