import pandas as pd
from collections import OrderedDict
def xlsx_to_csv(election_date,election_type_filler):

	year = election_date[len(election_date)-4:]
	date = str(election_date.split('_')[0])[-1]
	month = str(election_date.split('_')[0])[:len(str(election_date.split('_')[0]))-1]
	month_to_election_type_dict = {'March':'Presidential_Primary','May':'Primary','July':'Primary_Runoff','November':'General'}
	election_type = month_to_election_type_dict[month]
	formatted_date = '{} {}, {}'.format(month.upper(),date.zfill(2),year)
	ga_counties = ['APPLING', 'ATKINSON', 'BACON', 'BAKER', 'BALDWIN', 'BANKS', 'BARROW', 'BARTOW', 'BEN HILL', 'BERRIEN', 'BIBB', 'BLECKLEY', 'BRANTLEY', 'BROOKS', 'BRYAN', 'BULLOCH', 'BURKE', 'BUTTS', 'CALHOUN', 'CAMDEN', 'CANDLER', 'CARROLL', 'CATOOSA', 'CHARLTON', 'CHATHAM', 'CHATTAHOOCHEE', 'CHATTOOGA', 'CHEROKEE', 'CLARKE', 'CLAY', 'CLAYTON', 'CLINCH', 'COBB', 'COFFEE', 'COLQUITT', 'COLUMBIA', 'COOK', 'COWETA', 'CRAWFORD', 'CRISP', 'DADE', 'DAWSON', 'DECATUR', 'DEKALB', 'DODGE', 'DOOLY', 'DOUGHERTY', 'DOUGLAS', 'EARLY', 'ECHOLS', 'EFFINGHAM', 'ELBERT', 'EMANUEL', 'EVANS', 'FANNIN', 'FAYETTE', 'FLOYD', 'FORSYTH', 'FRANKLIN', 'FULTON', 'GILMER', 'GLASCOCK', 'GLYNN', 'GORDON', 'GRADY', 'GREENE', 'GWINNETT', 'HABERSHAM', 'HALL', 'HANCOCK', 'HARALSON', 'HARRIS', 'HART', 'HEARD', 'HENRY', 'HOUSTON', 'IRWIN', 'JACKSON', 'JASPER', 'JEFF DAVIS', 'JEFFERSON', 'JENKINS', 'JOHNSON', 'JONES', 'LAMAR', 'LANIER', 'LAURENS', 'LEE', 'LIBERTY', 'LINCOLN', 'LONG', 'LOWNDES', 'LUMPKIN', 'MCDUFFIE', 'MCINTOSH', 'MACON', 'MADISON', 'MARION', 'MERIWETHER', 'MILLER', 'MITCHELL', 'MONROE', 'MONTGOMERY', 'MORGAN', 'MURRAY', 'MUSCOGEE', 'NEWTON', 'OCONEE', 'OGLETHORPE', 'PAULDING', 'PEACH', 'PICKENS', 'PIERCE', 'PIKE', 'POLK', 'PULASKI', 'PUTNAM', 'QUITMAN', 'RABUN', 'RANDOLPH', 'RICHMOND', 'ROCKDALE', 'SCHLEY', 'SCREVEN', 'SEMINOLE', 'SPALDING', 'STEPHENS', 'STEWART', 'SUMTER', 'TALBOT', 'TALIAFERRO', 'TATTNALL', 'TAYLOR', 'TELFAIR', 'TERRELL', 'THOMAS', 'TIFT', 'TOOMBS', 'TOWNS', 'TREUTLEN', 'TROUP', 'TURNER', 'TWIGGS', 'UNION', 'UPSON', 'WALKER', 'WALTON', 'WARE', 'WARREN', 'WASHINGTON', 'WAYNE', 'WEBSTER', 'WHEELER', 'WHITE', 'WHITFIELD', 'WILCOX', 'WILKES', 'WILKINSON', 'WORTH']

	"""overall_total_registered_dataframe = pd.DataFrame(columns=[u'COUNTY NAME', u'TOTAL VOTERS', u'UNKNOWN', u'UNKNOWN FEMALE',
	       u'UNKNOWN MALE', u'OTHER UNKNOWN', u'OTHER FEMALE', u'OTHER MALE',
	       u'NATIVE-AM UNKNOWN', u'NATIVE-AM FEMALE', u'NATIVE-AM MALE',
	       u'HISP-LT UNKNOWN', u'HISP-LT FEMALE', u'HISP-LT MALE',
	       u'ASIA-PI UNKNOWN', u'ASIA-PI FEMALE', u'ASIA-PI MALE',
	       u'WHITE UNKNOWN', u'WHITE FEMALE', u'WHITE MALE', u'BLACK UNKNOWN',
	       u'BLACK FEMALE', u'BLACK MALE'])
	overall_total_voted_dataframe = pd.DataFrame(columns=[u'COUNTY NAME', u'TOTAL VOTERS', u'UNKNOWN', u'UNKNOWN FEMALE',
	       u'UNKNOWN MALE', u'OTHER UNKNOWN', u'OTHER FEMALE', u'OTHER MALE',
	       u'NATIVE-AM UNKNOWN', u'NATIVE-AM FEMALE', u'NATIVE-AM MALE',
	       u'HISP-LT UNKNOWN', u'HISP-LT FEMALE', u'HISP-LT MALE',
	       u'ASIA-PI UNKNOWN', u'ASIA-PI FEMALE', u'ASIA-PI MALE',
	       u'WHITE UNKNOWN', u'WHITE FEMALE', u'WHITE MALE', u'BLACK UNKNOWN',
	       u'BLACK FEMALE', u'BLACK MALE'])
	overall_percent_voted_dataframe = pd.DataFrame(columns=[u'COUNTY NAME', u'TOTAL VOTERS', u'UNKNOWN', u'UNKNOWN FEMALE',
	       u'UNKNOWN MALE', u'OTHER UNKNOWN', u'OTHER FEMALE', u'OTHER MALE',
	       u'NATIVE-AM UNKNOWN', u'NATIVE-AM FEMALE', u'NATIVE-AM MALE',
	       u'HISP-LT UNKNOWN', u'HISP-LT FEMALE', u'HISP-LT MALE',
	       u'ASIA-PI UNKNOWN', u'ASIA-PI FEMALE', u'ASIA-PI MALE',
	       u'WHITE UNKNOWN', u'WHITE FEMALE', u'WHITE MALE', u'BLACK UNKNOWN',
	       u'BLACK FEMALE', u'BLACK MALE'])

	for district in range(1,15):

		district = str(district).zfill(2)

		df = pd.read_excel('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_Source_XLSX/{}/{}{}(CongressionalDistricts)/0{}.xlsx'.format(year,election_date,election_type_filler,district))
		df = df.iloc[1:]

		df_total_registered = df[['GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''), 'Unnamed: 65', 'Unnamed: 62', 'Unnamed: 59', 'Unnamed: 56', 'Unnamed: 53', 'Unnamed: 50', 'Unnamed: 47', 'Unnamed: 44', 'Unnamed: 41', 'Unnamed: 38', 'Unnamed: 35', 'Unnamed: 32', 'Unnamed: 29', 'Unnamed: 26', 'Unnamed: 23', 'Unnamed: 20', 'Unnamed: 17', 'Unnamed: 14', 'Unnamed: 11', 'Unnamed: 8', 'Unnamed: 5', 'Unnamed: 2']]
		df_percentage_voted = df[['GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''), 'Unnamed: 67', 'Unnamed: 64', 'Unnamed: 61', 'Unnamed: 58', 'Unnamed: 55', 'Unnamed: 52', 'Unnamed: 49', 'Unnamed: 46', 'Unnamed: 43', 'Unnamed: 40', 'Unnamed: 37', 'Unnamed: 34', 'Unnamed: 31', 'Unnamed: 28', 'Unnamed: 25', 'Unnamed: 22', 'Unnamed: 19', 'Unnamed: 16', 'Unnamed: 13', 'Unnamed: 10', 'Unnamed: 7', 'Unnamed: 4']]
		df_voted = df[['GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''), 'Unnamed: 66', 'Unnamed: 63', 'Unnamed: 60', 'Unnamed: 57', 'Unnamed: 54', 'Unnamed: 51', 'Unnamed: 48', 'Unnamed: 45', 'Unnamed: 42', 'Unnamed: 39', 'Unnamed: 36', 'Unnamed: 33', 'Unnamed: 30', 'Unnamed: 27', 'Unnamed: 24', 'Unnamed: 21', 'Unnamed: 18', 'Unnamed: 15', 'Unnamed: 12', 'Unnamed: 9', 'Unnamed: 6', 'Unnamed: 3']]
		df_total_registered = df_total_registered.loc[df_total_registered['Unnamed: 65']!='Reg #']
		df_voted = df_voted.loc[df_voted['Unnamed: 66']!='Voted']
		df_percentage_voted = df_percentage_voted.loc[df_percentage_voted['Unnamed: 67']!='%']
		new_columns = [u'COUNTY NAME', u'TOTAL VOTERS', u'UNKNOWN', u'UNKNOWN FEMALE',
		       u'UNKNOWN MALE', u'OTHER UNKNOWN', u'OTHER FEMALE', u'OTHER MALE',
		       u'NATIVE-AM UNKNOWN', u'NATIVE-AM FEMALE', u'NATIVE-AM MALE',
		       u'HISP-LT UNKNOWN', u'HISP-LT FEMALE', u'HISP-LT MALE',
		       u'ASIA-PI UNKNOWN', u'ASIA-PI FEMALE', u'ASIA-PI MALE',
		       u'WHITE UNKNOWN', u'WHITE FEMALE', u'WHITE MALE', u'BLACK UNKNOWN',
		       u'BLACK FEMALE', u'BLACK MALE']

		df_voted.rename(columns={'Unnamed: 45': u'NATIVE-AM UNKNOWN', 'Unnamed: 54': u'OTHER UNKNOWN', 'Unnamed: 6': u'BLACK FEMALE', 'Unnamed: 3': u'BLACK MALE', 'Unnamed: 9': u'BLACK UNKNOWN', 'Unnamed: 27': u'ASIA-PI UNKNOWN', 'Unnamed: 24': u'ASIA-PI FEMALE', 'Unnamed: 21': u'ASIA-PI MALE', 'Unnamed: 63': u'UNKNOWN', 'Unnamed: 60': u'UNKNOWN FEMALE', 'Unnamed: 66': u'TOTAL VOTERS', 'Unnamed: 42': u'NATIVE-AM FEMALE', 'Unnamed: 48': u'OTHER MALE', 'GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''): u'COUNTY NAME', 'Unnamed: 15': u'WHITE FEMALE', 'Unnamed: 12': u'WHITE MALE', 'Unnamed: 39': u'NATIVE-AM MALE', 'Unnamed: 36': u'HISP-LT UNKNOWN', 'Unnamed: 51': u'OTHER FEMALE', 'Unnamed: 30': u'HISP-LT MALE', 'Unnamed: 57': u'UNKNOWN MALE', 'Unnamed: 18': u'WHITE UNKNOWN', 'Unnamed: 33': u'HISP-LT FEMALE'},inplace=True)
		df_voted = df_voted.iloc[1:]
		df_percentage_voted.rename(columns={'Unnamed: 4': u'BLACK MALE', 'Unnamed: 7': u'BLACK FEMALE', 'Unnamed: 28': u'ASIA-PI UNKNOWN', 'Unnamed: 25': u'ASIA-PI FEMALE', 'Unnamed: 22': u'ASIA-PI MALE', 'Unnamed: 61': u'UNKNOWN FEMALE', 'Unnamed: 46': u'NATIVE-AM UNKNOWN', 'Unnamed: 67': u'TOTAL VOTERS', 'Unnamed: 40': u'NATIVE-AM MALE', 'Unnamed: 43': u'NATIVE-AM FEMALE', 'Unnamed: 64': u'UNKNOWN', 'Unnamed: 49': u'OTHER MALE', 'Unnamed: 34': u'HISP-LT FEMALE', 'Unnamed: 55': u'OTHER UNKNOWN', 'GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''): u'COUNTY NAME', 'Unnamed: 16': u'WHITE FEMALE', 'Unnamed: 58': u'UNKNOWN MALE', 'Unnamed: 13': u'WHITE MALE', 'Unnamed: 10': u'BLACK UNKNOWN', 'Unnamed: 52': u'OTHER FEMALE', 'Unnamed: 37': u'HISP-LT UNKNOWN', 'Unnamed: 31': u'HISP-LT MALE', 'Unnamed: 19': u'WHITE UNKNOWN'},inplace=True)
		df_percentage_voted = df_percentage_voted.iloc[1:]
		df_total_registered.rename(columns={'Unnamed: 44': u'NATIVE-AM UNKNOWN', 'Unnamed: 5': u'BLACK FEMALE', 'Unnamed: 2': u'BLACK MALE', 'Unnamed: 8': u'BLACK UNKNOWN', 'Unnamed: 29': u'HISP-LT MALE', 'Unnamed: 26': u'ASIA-PI UNKNOWN', 'Unnamed: 23': u'ASIA-PI FEMALE', 'Unnamed: 20': u'ASIA-PI MALE', 'Unnamed: 62': u'UNKNOWN', 'Unnamed: 47': u'OTHER MALE', 'Unnamed: 41': u'NATIVE-AM FEMALE', 'Unnamed: 65': u'TOTAL VOTERS', 'Unnamed: 53': u'OTHER UNKNOWN', 'GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''): u'COUNTY NAME', 'Unnamed: 17': u'WHITE UNKNOWN', 'Unnamed: 14': u'WHITE FEMALE', 'Unnamed: 59': u'UNKNOWN FEMALE', 'Unnamed: 38': u'NATIVE-AM MALE', 'Unnamed: 11': u'WHITE MALE', 'Unnamed: 35': u'HISP-LT UNKNOWN', 'Unnamed: 50': u'OTHER FEMALE', 'Unnamed: 56': u'UNKNOWN MALE', 'Unnamed: 32': u'HISP-LT FEMALE'},inplace=True)
		df_total_registered = df_total_registered.iloc[1:]

		df_percentage_voted.fillna(0,inplace=True)
		df_total_registered.fillna(0,inplace=True)
		df_voted.fillna(0,inplace=True)

		for column in df_total_registered.columns:
			if column != 'COUNTY NAME':
				df_total_registered[column] = df_total_registered[column].apply(float)
		
		for column in df_voted.columns:
			if column != 'COUNTY NAME':
				df_voted[column] = df_voted[column].apply(float)

		df_total_registered = df_total_registered.append(df_total_registered.sum(axis=0),ignore_index=True)
		df_total_registered['COUNTY NAME'][len(df_total_registered)-1] = 'TOTAL'
		df_voted = df_voted.append(df_voted.sum(axis=0),ignore_index=True)
		df_voted['COUNTY NAME'][len(df_voted)-1] = 'TOTAL'

		df_divided = df_voted.loc[:,df_voted.columns!='COUNTY NAME'] / df_total_registered.loc[:,df_total_registered.columns!='COUNTY NAME']
		pd_seires = pd.Series(df_divided.iloc[-1])
		pd_seires = (pd_seires*100).round(2)
		pd_seires['COUNTY NAME'] = 'TOTAL'
		df_percentage_voted.loc[len(df_total_registered)+1] = pd_seires

		df_total_registered.rename(columns={'AGE GROUP':'AGE GROUP', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL':'TOTAL'},inplace=True)
		df_total_registered = df_total_registered[['AGE GROUP','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]
		df_percentage_voted.rename(columns={'AGE GROUP':'AGE GROUP', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL':'TOTAL'},inplace=True)
		df_percentage_voted = df_percentage_voted[['AGE GROUP','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]
		df_voted.rename(columns={'AGE GROUP':'AGE GROUP', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL':'TOTAL'},inplace=True)
		df_voted = df_voted[['AGE GROUP','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]

		df_total_registered.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/US{}_total_registered.csv'.format(year,election_type,district),index=None)
		df_voted.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/US{}_total_voted.csv'.format(year,election_type,district),index=None)
		df_percentage_voted.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/US{}_percent_voted.csv'.format(year,election_type,district),index=None)

		df_total_registered = df_total_registered.loc[df_total_registered['COUNTY NAME']=='TOTAL']
		df_voted = df_voted.loc[df_voted['COUNTY NAME']=='TOTAL']
		df_percentage_voted = df_percentage_voted.loc[df_percentage_voted['COUNTY NAME']=='TOTAL']

		df_total_registered.loc[df_total_registered['COUNTY NAME']=='TOTAL',['COUNTY NAME']] = 'Congressional District {}'.format(str(int(district)))
		df_voted.loc[df_voted['COUNTY NAME']=='TOTAL',['COUNTY NAME']] = 'Congressional District {}'.format(str(int(district)))
		df_percentage_voted.loc[df_percentage_voted['COUNTY NAME']=='TOTAL',['COUNTY NAME']] = 'Congressional District {}'.format(str(int(district)))

		overall_total_registered_dataframe = overall_total_registered_dataframe.append(df_total_registered)
		overall_total_voted_dataframe = overall_total_voted_dataframe.append(df_voted)
		overall_percent_voted_dataframe = overall_percent_voted_dataframe.append(df_percentage_voted)

	overall_percent_voted_dataframe.fillna(0,inplace=True)

	overall_total_registered_dataframe.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/Congressional_total_registered.csv'.format(year,election_type,district),index=None)
	overall_total_voted_dataframe.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/Congressional_total_voted.csv'.format(year,election_type,district),index=None)
	overall_percent_voted_dataframe.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Congressional/Congressional_percent_voted.csv'.format(year,election_type,district),index=None)"""

	for county in ga_counties:

		district = county

		df = pd.read_excel('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_Source_XLSX/{}/{}{}(CountyPrecinct)/{}.xlsx'.format(year,election_date,election_type_filler,district))
		df = df.iloc[1:]
		df.rename(columns={[col for col in df if col.startswith('GEORGIA')][0]:'GEORGIA'},inplace=True)
		df_total_registered = df[['Unnamed: 1', 'Unnamed: 65', 'Unnamed: 62', 'Unnamed: 59', 'Unnamed: 56', 'Unnamed: 53', 'Unnamed: 50', 'Unnamed: 47', 'Unnamed: 44', 'Unnamed: 41', 'Unnamed: 38', 'Unnamed: 35', 'Unnamed: 32', 'Unnamed: 29', 'Unnamed: 26', 'Unnamed: 23', 'Unnamed: 20', 'Unnamed: 17', 'Unnamed: 14', 'Unnamed: 11', 'Unnamed: 8', 'Unnamed: 5', 'Unnamed: 2']]
		df_percentage_voted = df[['Unnamed: 1', 'Unnamed: 67', 'Unnamed: 64', 'Unnamed: 61', 'Unnamed: 58', 'Unnamed: 55', 'Unnamed: 52', 'Unnamed: 49', 'Unnamed: 46', 'Unnamed: 43', 'Unnamed: 40', 'Unnamed: 37', 'Unnamed: 34', 'Unnamed: 31', 'Unnamed: 28', 'Unnamed: 25', 'Unnamed: 22', 'Unnamed: 19', 'Unnamed: 16', 'Unnamed: 13', 'Unnamed: 10', 'Unnamed: 7', 'Unnamed: 4']]
		df_voted = df[['Unnamed: 1', 'Unnamed: 66', 'Unnamed: 63', 'Unnamed: 60', 'Unnamed: 57', 'Unnamed: 54', 'Unnamed: 51', 'Unnamed: 48', 'Unnamed: 45', 'Unnamed: 42', 'Unnamed: 39', 'Unnamed: 36', 'Unnamed: 33', 'Unnamed: 30', 'Unnamed: 27', 'Unnamed: 24', 'Unnamed: 21', 'Unnamed: 18', 'Unnamed: 15', 'Unnamed: 12', 'Unnamed: 9', 'Unnamed: 6', 'Unnamed: 3']]
		df_total_registered = df_total_registered.loc[df_total_registered['Unnamed: 65']!='Reg #']
		df_voted = df_voted.loc[df_voted['Unnamed: 66']!='Voted']
		df_percentage_voted = df_percentage_voted.loc[df_percentage_voted['Unnamed: 67']!='%']
		new_columns = [u'COUNTY NAME', u'TOTAL VOTERS', u'UNKNOWN', u'UNKNOWN FEMALE',
		       u'UNKNOWN MALE', u'OTHER UNKNOWN', u'OTHER FEMALE', u'OTHER MALE',
		       u'NATIVE-AM UNKNOWN', u'NATIVE-AM FEMALE', u'NATIVE-AM MALE',
		       u'HISP-LT UNKNOWN', u'HISP-LT FEMALE', u'HISP-LT MALE',
		       u'ASIA-PI UNKNOWN', u'ASIA-PI FEMALE', u'ASIA-PI MALE',
		       u'WHITE UNKNOWN', u'WHITE FEMALE', u'WHITE MALE', u'BLACK UNKNOWN',
		       u'BLACK FEMALE', u'BLACK MALE']

		df_voted.rename(columns={'Unnamed: 45': u'NATIVE-AM UNKNOWN', 'Unnamed: 54': u'OTHER UNKNOWN', 'Unnamed: 6': u'BLACK FEMALE', 'Unnamed: 3': u'BLACK MALE', 'Unnamed: 9': u'BLACK UNKNOWN', 'Unnamed: 27': u'ASIA-PI UNKNOWN', 'Unnamed: 24': u'ASIA-PI FEMALE', 'Unnamed: 21': u'ASIA-PI MALE', 'Unnamed: 63': u'UNKNOWN', 'Unnamed: 60': u'UNKNOWN FEMALE', 'Unnamed: 66': u'TOTAL VOTERS', 'Unnamed: 42': u'NATIVE-AM FEMALE', 'Unnamed: 48': u'OTHER MALE', 'Unnamed: 1': u'PRECINCT NAME', 'Unnamed: 15': u'WHITE FEMALE', 'Unnamed: 12': u'WHITE MALE', 'Unnamed: 39': u'NATIVE-AM MALE', 'Unnamed: 36': u'HISP-LT UNKNOWN', 'Unnamed: 51': u'OTHER FEMALE', 'Unnamed: 30': u'HISP-LT MALE', 'Unnamed: 57': u'UNKNOWN MALE', 'Unnamed: 18': u'WHITE UNKNOWN', 'Unnamed: 33': u'HISP-LT FEMALE'},inplace=True)
		df_voted = df_voted.iloc[1:]
		df_percentage_voted.rename(columns={'Unnamed: 4': u'BLACK MALE', 'Unnamed: 7': u'BLACK FEMALE', 'Unnamed: 28': u'ASIA-PI UNKNOWN', 'Unnamed: 25': u'ASIA-PI FEMALE', 'Unnamed: 22': u'ASIA-PI MALE', 'Unnamed: 61': u'UNKNOWN FEMALE', 'Unnamed: 46': u'NATIVE-AM UNKNOWN', 'Unnamed: 67': u'TOTAL VOTERS', 'Unnamed: 40': u'NATIVE-AM MALE', 'Unnamed: 43': u'NATIVE-AM FEMALE', 'Unnamed: 64': u'UNKNOWN', 'Unnamed: 49': u'OTHER MALE', 'Unnamed: 34': u'HISP-LT FEMALE', 'Unnamed: 55': u'OTHER UNKNOWN', 'Unnamed: 1': u'PRECINCT NAME', 'Unnamed: 16': u'WHITE FEMALE', 'Unnamed: 58': u'UNKNOWN MALE', 'Unnamed: 13': u'WHITE MALE', 'Unnamed: 10': u'BLACK UNKNOWN', 'Unnamed: 52': u'OTHER FEMALE', 'Unnamed: 37': u'HISP-LT UNKNOWN', 'Unnamed: 31': u'HISP-LT MALE', 'Unnamed: 19': u'WHITE UNKNOWN'},inplace=True)
		df_percentage_voted = df_percentage_voted.iloc[1:]
		df_total_registered.rename(columns={'Unnamed: 44': u'NATIVE-AM UNKNOWN', 'Unnamed: 5': u'BLACK FEMALE', 'Unnamed: 2': u'BLACK MALE', 'Unnamed: 8': u'BLACK UNKNOWN', 'Unnamed: 29': u'HISP-LT MALE', 'Unnamed: 26': u'ASIA-PI UNKNOWN', 'Unnamed: 23': u'ASIA-PI FEMALE', 'Unnamed: 20': u'ASIA-PI MALE', 'Unnamed: 62': u'UNKNOWN', 'Unnamed: 47': u'OTHER MALE', 'Unnamed: 41': u'NATIVE-AM FEMALE', 'Unnamed: 65': u'TOTAL VOTERS', 'Unnamed: 53': u'OTHER UNKNOWN', 'Unnamed: 1': u'PRECINCT NAME', 'Unnamed: 17': u'WHITE UNKNOWN', 'Unnamed: 14': u'WHITE FEMALE', 'Unnamed: 59': u'UNKNOWN FEMALE', 'Unnamed: 38': u'NATIVE-AM MALE', 'Unnamed: 11': u'WHITE MALE', 'Unnamed: 35': u'HISP-LT UNKNOWN', 'Unnamed: 50': u'OTHER FEMALE', 'Unnamed: 56': u'UNKNOWN MALE', 'Unnamed: 32': u'HISP-LT FEMALE'},inplace=True)
		df_total_registered = df_total_registered.iloc[1:]

		df_total_registered.fillna(0,inplace=True)
		df_voted.fillna(0,inplace=True)

		for column in df_total_registered.columns:
			if column != 'PRECINCT NAME':
				df_total_registered[column] = df_total_registered[column].apply(float)
		
		for column in df_voted.columns:
			if column != 'PRECINCT NAME':
				df_voted[column] = df_voted[column].apply(float)

		df_total_registered = df_total_registered.append(df_total_registered.sum(axis=0),ignore_index=True)
		df_total_registered['PRECINCT NAME'][len(df_total_registered)-1] = 'TOTAL'
		df_voted = df_voted.append(df_voted.sum(axis=0),ignore_index=True)
		df_voted['PRECINCT NAME'][len(df_voted)-1] = 'TOTAL'

		df_divided = df_voted.loc[:,df_voted.columns!='PRECINCT NAME'] / df_total_registered.loc[:,df_total_registered.columns!='PRECINCT NAME']
		pd_seires = pd.Series(df_divided.iloc[-1])
		pd_seires = (pd_seires*100).round(2)
		pd_seires['PRECINCT NAME'] = 'TOTAL'
		df_percentage_voted.loc[len(df_total_registered)+1] = pd_seires

		df_total_registered.rename(columns={'PRECINCT NAME':'PRECINCT NAME', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL VOTERS':'TOTAL'},inplace=True)
		df_total_registered = df_total_registered[['PRECINCT NAME','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]
		df_percentage_voted.rename(columns={'PRECINCT NAME':'PRECINCT NAME', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL VOTERS':'TOTAL'},inplace=True)
		df_percentage_voted = df_percentage_voted[['PRECINCT NAME','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]
		df_voted.rename(columns={'PRECINCT NAME':'PRECINCT NAME', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL VOTERS':'TOTAL'},inplace=True)
		df_voted = df_voted[['PRECINCT NAME','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]

		df_voted['PRECINCT NAME'] = df_voted['PRECINCT NAME'].str.replace(r"\(.*\)","").str.strip()
		df_percentage_voted['PRECINCT NAME'] = df_percentage_voted['PRECINCT NAME'].str.replace(r"\(.*\)","").str.strip()
		df_total_registered['PRECINCT NAME'] = df_total_registered['PRECINCT NAME'].str.replace(r"\(.*\)","").str.strip()

		df_percentage_voted.dropna(subset=['PRECINCT NAME'],inplace=True)
		df_voted.dropna(subset=['PRECINCT NAME'],inplace=True)
		df_total_registered.dropna(subset=['PRECINCT NAME'],inplace=True)

		df_total_registered.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_total_registered.csv'.format(year,election_type,district),index=None)
		df_voted.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_total_voted.csv'.format(year,election_type,district),index=None)
		df_percentage_voted = df_percentage_voted.replace(u"\u221e",100)
		df_percentage_voted.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/Precinct/{}_gender_vs_race_percent_voted.csv'.format(year,election_type,district),index=None)

	"""for county in ga_counties:

		district = county

		df = pd.read_excel('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_Source_XLSX/{}/{}{}(Age)/{}.xlsx'.format(year,election_date,election_type_filler,district))
		df = df.iloc[1:]
		df.rename(columns={'GEORGIA SECRETARY OF STATE\nSSVRZ521R1 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date):'GEORGIA SECRETARY OF STATE\nSSVRZ521R1 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE','')},inplace=True)
		df_total_registered = df[['GEORGIA SECRETARY OF STATE\nSSVRZ521R1 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''), 'Unnamed: 65', 'Unnamed: 62', 'Unnamed: 59', 'Unnamed: 56', 'Unnamed: 53', 'Unnamed: 50', 'Unnamed: 47', 'Unnamed: 44', 'Unnamed: 41', 'Unnamed: 38', 'Unnamed: 35', 'Unnamed: 32', 'Unnamed: 29', 'Unnamed: 26', 'Unnamed: 23', 'Unnamed: 20', 'Unnamed: 17', 'Unnamed: 14', 'Unnamed: 11', 'Unnamed: 8', 'Unnamed: 5', 'Unnamed: 2']]
		df_percentage_voted = df[['GEORGIA SECRETARY OF STATE\nSSVRZ521R1 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''), 'Unnamed: 67', 'Unnamed: 64', 'Unnamed: 61', 'Unnamed: 58', 'Unnamed: 55', 'Unnamed: 52', 'Unnamed: 49', 'Unnamed: 46', 'Unnamed: 43', 'Unnamed: 40', 'Unnamed: 37', 'Unnamed: 34', 'Unnamed: 31', 'Unnamed: 28', 'Unnamed: 25', 'Unnamed: 22', 'Unnamed: 19', 'Unnamed: 16', 'Unnamed: 13', 'Unnamed: 10', 'Unnamed: 7', 'Unnamed: 4']]
		df_voted = df[['GEORGIA SECRETARY OF STATE\nSSVRZ521R1 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''), 'Unnamed: 66', 'Unnamed: 63', 'Unnamed: 60', 'Unnamed: 57', 'Unnamed: 54', 'Unnamed: 51', 'Unnamed: 48', 'Unnamed: 45', 'Unnamed: 42', 'Unnamed: 39', 'Unnamed: 36', 'Unnamed: 33', 'Unnamed: 30', 'Unnamed: 27', 'Unnamed: 24', 'Unnamed: 21', 'Unnamed: 18', 'Unnamed: 15', 'Unnamed: 12', 'Unnamed: 9', 'Unnamed: 6', 'Unnamed: 3']]
		df_total_registered = df_total_registered.loc[df_total_registered['Unnamed: 65']!='Reg #']
		df_voted = df_voted.loc[df_voted['Unnamed: 66']!='Voted']
		df_percentage_voted = df_percentage_voted.loc[df_percentage_voted['Unnamed: 67']!='%']
		new_columns = [u'COUNTY NAME', u'UNKNOWN', u'UNKNOWN FEMALE',
		       u'UNKNOWN MALE', u'OTHER UNKNOWN', u'OTHER FEMALE', u'OTHER MALE',
		       u'NATIVE-AM UNKNOWN', u'NATIVE-AM FEMALE', u'NATIVE-AM MALE',
		       u'HISP-LT UNKNOWN', u'HISP-LT FEMALE', u'HISP-LT MALE',
		       u'ASIA-PI UNKNOWN', u'ASIA-PI FEMALE', u'ASIA-PI MALE',
		       u'WHITE UNKNOWN', u'WHITE FEMALE', u'WHITE MALE', u'BLACK UNKNOWN',
		       u'BLACK FEMALE', u'BLACK MALE', u'TOTAL']

		df_voted.rename(columns={'Unnamed: 45': u'NATIVE-AM UNKNOWN', 'Unnamed: 54': u'OTHER UNKNOWN', 'Unnamed: 6': u'BLACK FEMALE', 'Unnamed: 3': u'BLACK MALE', 'Unnamed: 9': u'BLACK UNKNOWN', 'Unnamed: 27': u'ASIA-PI UNKNOWN', 'Unnamed: 24': u'ASIA-PI FEMALE', 'Unnamed: 21': u'ASIA-PI MALE', 'Unnamed: 63': u'UNKNOWN', 'Unnamed: 60': u'UNKNOWN FEMALE', 'Unnamed: 66': u'TOTAL', 'Unnamed: 42': u'NATIVE-AM FEMALE', 'Unnamed: 48': u'OTHER MALE', 'GEORGIA SECRETARY OF STATE\nSSVRZ521R1 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''): u'AGE GROUP', 'Unnamed: 15': u'WHITE FEMALE', 'Unnamed: 12': u'WHITE MALE', 'Unnamed: 39': u'NATIVE-AM MALE', 'Unnamed: 36': u'HISP-LT UNKNOWN', 'Unnamed: 51': u'OTHER FEMALE', 'Unnamed: 30': u'HISP-LT MALE', 'Unnamed: 57': u'UNKNOWN MALE', 'Unnamed: 18': u'WHITE UNKNOWN', 'Unnamed: 33': u'HISP-LT FEMALE'},inplace=True)
		df_voted = df_voted.iloc[1:]
		df_percentage_voted.rename(columns={'Unnamed: 4': u'BLACK MALE', 'Unnamed: 7': u'BLACK FEMALE', 'Unnamed: 28': u'ASIA-PI UNKNOWN', 'Unnamed: 25': u'ASIA-PI FEMALE', 'Unnamed: 22': u'ASIA-PI MALE', 'Unnamed: 61': u'UNKNOWN FEMALE', 'Unnamed: 46': u'NATIVE-AM UNKNOWN', 'Unnamed: 67': u'TOTAL', 'Unnamed: 40': u'NATIVE-AM MALE', 'Unnamed: 43': u'NATIVE-AM FEMALE', 'Unnamed: 64': u'UNKNOWN', 'Unnamed: 49': u'OTHER MALE', 'Unnamed: 34': u'HISP-LT FEMALE', 'Unnamed: 55': u'OTHER UNKNOWN', 'GEORGIA SECRETARY OF STATE\nSSVRZ521R1 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''): u'AGE GROUP', 'Unnamed: 16': u'WHITE FEMALE', 'Unnamed: 58': u'UNKNOWN MALE', 'Unnamed: 13': u'WHITE MALE', 'Unnamed: 10': u'BLACK UNKNOWN', 'Unnamed: 52': u'OTHER FEMALE', 'Unnamed: 37': u'HISP-LT UNKNOWN', 'Unnamed: 31': u'HISP-LT MALE', 'Unnamed: 19': u'WHITE UNKNOWN'},inplace=True)
		df_percentage_voted = df_percentage_voted.iloc[1:]
		df_total_registered.rename(columns={'Unnamed: 44': u'NATIVE-AM UNKNOWN', 'Unnamed: 5': u'BLACK FEMALE', 'Unnamed: 2': u'BLACK MALE', 'Unnamed: 8': u'BLACK UNKNOWN', 'Unnamed: 29': u'HISP-LT MALE', 'Unnamed: 26': u'ASIA-PI UNKNOWN', 'Unnamed: 23': u'ASIA-PI FEMALE', 'Unnamed: 20': u'ASIA-PI MALE', 'Unnamed: 62': u'UNKNOWN', 'Unnamed: 47': u'OTHER MALE', 'Unnamed: 41': u'NATIVE-AM FEMALE', 'Unnamed: 65': u'TOTAL', 'Unnamed: 53': u'OTHER UNKNOWN', 'GEORGIA SECRETARY OF STATE\nSSVRZ521R1 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: {} '.format(formatted_date).replace('\\n','\n').replace('/INACTIVE',''): u'AGE GROUP', 'Unnamed: 17': u'WHITE UNKNOWN', 'Unnamed: 14': u'WHITE FEMALE', 'Unnamed: 59': u'UNKNOWN FEMALE', 'Unnamed: 38': u'NATIVE-AM MALE', 'Unnamed: 11': u'WHITE MALE', 'Unnamed: 35': u'HISP-LT UNKNOWN', 'Unnamed: 50': u'OTHER FEMALE', 'Unnamed: 56': u'UNKNOWN MALE', 'Unnamed: 32': u'HISP-LT FEMALE'},inplace=True)
		df_total_registered = df_total_registered.iloc[1:]

		df_total_registered.fillna(0,inplace=True)
		df_voted.fillna(0,inplace=True)

		for column in df_total_registered.columns:
			if column != 'AGE GROUP':
				df_total_registered[column] = df_total_registered[column].apply(float)
		
		for column in df_voted.columns:
			if column != 'AGE GROUP':
				df_voted[column] = df_voted[column].apply(float)

		df_total_registered = df_total_registered.append(df_total_registered.sum(axis=0),ignore_index=True)
		df_total_registered['AGE GROUP'][len(df_total_registered)-1] = 'TOTAL'
		df_voted = df_voted.append(df_voted.sum(axis=0),ignore_index=True)
		df_voted['AGE GROUP'][len(df_voted)-1] = 'TOTAL'

		df_divided = df_voted.loc[:,df_voted.columns!='AGE GROUP'] / df_total_registered.loc[:,df_total_registered.columns!='AGE GROUP']
		pd_seires = pd.Series(df_divided.iloc[-1])
		pd_seires = (pd_seires*100).round(2)
		pd_seires['AGE GROUP'] = 'TOTAL'
		df_percentage_voted.loc[len(df_total_registered)+1] = pd_seires

		df_total_registered.rename(columns={'AGE GROUP':'-', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL':'TOTAL'},inplace=True)
		df_total_registered = df_total_registered[['-','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]
		df_percentage_voted.rename(columns={'AGE GROUP':'-', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL':'TOTAL'},inplace=True)
		df_percentage_voted = df_percentage_voted[['-','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]
		df_voted.rename(columns={'AGE GROUP':'-', 'UNKNOWN':'UNKNOWN', 'UNKNOWN FEMALE':'UNKNOWN FEMALE', 'UNKNOWN MALE':'UNKNOWN MALE', 'OTHER UNKNOWN':'OTHER UNKNOWN', 'OTHER FEMALE':'OTHER FEMALE', 'OTHER MALE':'OTHER MALE', 'NATIVE-AM UNKNOWN':'NATIVE AMERICAN UNKNOWN', 'NATIVE-AM FEMALE':'NATIVE AMERICAN FEMALE', 'NATIVE-AM MALE':'NATIVE AMERICAN MALE', 'HISP-LT UNKNOWN':'LATINO UNKNOWN', 'HISP-LT FEMALE':'LATINO FEMALE', 'HISP-LT MALE':'LATINO MALE', 'ASIA-PI UNKNOWN':'ASIAN-PACIFIC UNKNOWN', 'ASIA-PI FEMALE':'ASIAN-PACIFIC FEMALE', 'ASIA-PI MALE':'ASIAN-PACIFIC MALE', 'WHITE UNKNOWN':'WHITE UNKNOWN', 'WHITE FEMALE':'WHITE FEMALE', 'WHITE MALE':'WHITE MALE', 'BLACK UNKNOWN':'BLACK UNKNOWN', 'BLACK FEMALE':'BLACK FEMALE', 'BLACK MALE':'BLACK MALE', 'TOTAL':'TOTAL'},inplace=True)
		df_voted = df_voted[['-','UNKNOWN','UNKNOWN FEMALE','UNKNOWN MALE','OTHER UNKNOWN','OTHER FEMALE','OTHER MALE','NATIVE AMERICAN UNKNOWN','NATIVE AMERICAN FEMALE','NATIVE AMERICAN MALE','LATINO UNKNOWN','LATINO FEMALE','LATINO MALE','ASIAN-PACIFIC UNKNOWN','ASIAN-PACIFIC FEMALE','ASIAN-PACIFIC MALE','WHITE UNKNOWN','WHITE FEMALE','WHITE MALE','BLACK UNKNOWN','BLACK FEMALE','BLACK MALE','TOTAL']]

		df_total_registered.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_registered.csv'.format(year,election_type,district),index=None)
		df_voted.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_total_voted.csv'.format(year,election_type,district),index=None)
		df_percentage_voted = df_percentage_voted.replace(u"\u221e",100)
		df_percentage_voted.fillna(0,inplace=True)
		df_percentage_voted.to_csv('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/{}/{}/County/{}_percent_voted.csv'.format(year,election_type,district),index=None)

		df_total_registered = df_total_registered.loc[df_total_registered['-']=='TOTAL']
		df_voted = df_voted.loc[df_voted['-']=='TOTAL']
		df_percentage_voted = df_percentage_voted.loc[df_percentage_voted['-']=='TOTAL']"""	

xlsx_to_csv('November6_2018','')


