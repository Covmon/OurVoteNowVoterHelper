import pandas as pd

import pandas as pd
df = pd.read_excel('/Users/sammahle/Downloads/Congressional/001.xlsx')
df = df.iloc[1:]
df_total_registered = df[['GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: NOVEMBER 06, 2018 ', 'Unnamed: 65', 'Unnamed: 62', 'Unnamed: 59', 'Unnamed: 56', 'Unnamed: 53', 'Unnamed: 50', 'Unnamed: 47', 'Unnamed: 44', 'Unnamed: 41', 'Unnamed: 38', 'Unnamed: 35', 'Unnamed: 32', 'Unnamed: 29', 'Unnamed: 26', 'Unnamed: 23', 'Unnamed: 20', 'Unnamed: 17', 'Unnamed: 14', 'Unnamed: 11', 'Unnamed: 8', 'Unnamed: 5', 'Unnamed: 2']]
df_percentage_voted = df[['GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: NOVEMBER 06, 2018 ', 'Unnamed: 67', 'Unnamed: 64', 'Unnamed: 61', 'Unnamed: 58', 'Unnamed: 55', 'Unnamed: 52', 'Unnamed: 49', 'Unnamed: 46', 'Unnamed: 43', 'Unnamed: 40', 'Unnamed: 37', 'Unnamed: 34', 'Unnamed: 31', 'Unnamed: 28', 'Unnamed: 25', 'Unnamed: 22', 'Unnamed: 19', 'Unnamed: 16', 'Unnamed: 13', 'Unnamed: 10', 'Unnamed: 7', 'Unnamed: 4', 'Unnamed: 1']]
df_voted = df[['GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: NOVEMBER 06, 2018 ', 'Unnamed: 66', 'Unnamed: 63', 'Unnamed: 60', 'Unnamed: 57', 'Unnamed: 54', 'Unnamed: 51', 'Unnamed: 48', 'Unnamed: 45', 'Unnamed: 42', 'Unnamed: 39', 'Unnamed: 36', 'Unnamed: 33', 'Unnamed: 30', 'Unnamed: 27', 'Unnamed: 24', 'Unnamed: 21', 'Unnamed: 18', 'Unnamed: 15', 'Unnamed: 12', 'Unnamed: 9', 'Unnamed: 6', 'Unnamed: 3']]
df_total_registered = df_total_registered.loc[df_total_registered['Unnamed: 65']!='Reg #']
df_voted = df_voted.loc[df_voted['Unnamed: 66']!='Voted']
df_percentage_voted = df_percentage_voted.loc[df_percentage_voted['Unnamed: 67']!='%']

df_total_registered.to_csv('/Users/sammahle/Downloads/Congressional/tr.csv',header=None,index=None)
df_voted.to_csv('/Users/sammahle/Downloads/Congressional/tv.csv',header=None,index=None)
df_percentage_voted.to_csv('/Users/sammahle/Downloads/Congressional/pv.csv',header=None,index=None)

new_columns = [u'COUNTY NAME', u'TOTAL VOTERS', u'UNKNOWN', u'UNKNOWN FEMALE',
       u'UNKNOWN MALE', u'OTHER UNKNOWN', u'OTHER FEMALE', u'OTHER MALE',
       u'NATIVE-AM UNKNOWN', u'NATIVE-AM FEMALE', u'NATIVE-AM MALE',
       u'HISP-LT UNKNOWN', u'HISP-LT FEMALE', u'HISP-LT MALE',
       u'ASIA-PI UNKNOWN', u'ASIA-PI FEMALE', u'ASIA-PI MALE',
       u'WHITE UNKNOWN', u'WHITE FEMALE', u'WHITE MALE', u'BLACK UNKNOWN',
       u'BLACK FEMALE', u'BLACK MALE']


df_voted.rename(columns={'Unnamed: 45': u'NATIVE-AM UNKNOWN', 'Unnamed: 54': u'OTHER UNKNOWN', 'Unnamed: 6': u'BLACK FEMALE', 'Unnamed: 3': u'BLACK MALE', 'Unnamed: 9': u'BLACK UNKNOWN', 'Unnamed: 27': u'ASIA-PI UNKNOWN', 'Unnamed: 24': u'ASIA-PI FEMALE', 'Unnamed: 21': u'ASIA-PI MALE', 'Unnamed: 63': u'UNKNOWN', 'Unnamed: 60': u'UNKNOWN FEMALE', 'Unnamed: 66': u'TOTAL VOTERS', 'Unnamed: 42': u'NATIVE-AM FEMALE', 'Unnamed: 48': u'OTHER MALE', 'GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: NOVEMBER 06, 2018 ': u'COUNTY NAME', 'Unnamed: 15': u'WHITE FEMALE', 'Unnamed: 12': u'WHITE MALE', 'Unnamed: 39': u'NATIVE-AM MALE', 'Unnamed: 36': u'HISP-LT UNKNOWN', 'Unnamed: 51': u'OTHER FEMALE', 'Unnamed: 30': u'HISP-LT MALE', 'Unnamed: 57': u'UNKNOWN MALE', 'Unnamed: 18': u'WHITE UNKNOWN', 'Unnamed: 33': u'HISP-LT FEMALE'},inplace=True)
df_voted = df_voted.iloc[1:]
df_percentage_voted.rename(columns={'Unnamed: 4': u'BLACK MALE', 'Unnamed: 7': u'BLACK FEMALE', 'Unnamed: 28': u'ASIA-PI UNKNOWN', 'Unnamed: 25': u'ASIA-PI FEMALE', 'Unnamed: 22': u'ASIA-PI MALE', 'Unnamed: 61': u'UNKNOWN FEMALE', 'Unnamed: 46': u'NATIVE-AM UNKNOWN', 'Unnamed: 67': u'TOTAL VOTERS', 'Unnamed: 40': u'NATIVE-AM MALE', 'Unnamed: 43': u'NATIVE-AM FEMALE', 'Unnamed: 64': u'UNKNOWN', 'Unnamed: 49': u'OTHER MALE', 'Unnamed: 34': u'HISP-LT FEMALE', 'Unnamed: 55': u'OTHER UNKNOWN', 'GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: NOVEMBER 06, 2018 ': u'COUNTY NAME', 'Unnamed: 16': u'WHITE FEMALE', 'Unnamed: 58': u'UNKNOWN MALE', 'Unnamed: 13': u'WHITE MALE', 'Unnamed: 10': u'BLACK UNKNOWN', 'Unnamed: 52': u'OTHER FEMALE', 'Unnamed: 37': u'HISP-LT UNKNOWN', 'Unnamed: 31': u'HISP-LT MALE', 'Unnamed: 19': u'WHITE UNKNOWN'},inplace=True)
df_percentage_voted = df_percentage_voted.iloc[1:]
df_total_registered.rename(columns={'Unnamed: 44': u'NATIVE-AM UNKNOWN', 'Unnamed: 5': u'BLACK FEMALE', 'Unnamed: 2': u'BLACK MALE', 'Unnamed: 8': u'BLACK UNKNOWN', 'Unnamed: 29': u'HISP-LT MALE', 'Unnamed: 26': u'ASIA-PI UNKNOWN', 'Unnamed: 23': u'ASIA-PI FEMALE', 'Unnamed: 20': u'ASIA-PI MALE', 'Unnamed: 62': u'UNKNOWN', 'Unnamed: 47': u'OTHER MALE', 'Unnamed: 41': u'NATIVE-AM FEMALE', 'Unnamed: 65': u'TOTAL VOTERS', 'Unnamed: 53': u'OTHER UNKNOWN', 'GEORGIA SECRETARY OF STATE\nSSVRZ517 VOTER REGISTRATION SYSTEM SECRETARY OF STATE\nACTIVE/INACTIVE VOTERS BY RACE/GENDER/DISTRICT\nGENERAL ELECTION VOTING HISTORY SUMMARY\nELECTION DATE: NOVEMBER 06, 2018 ': u'COUNTY NAME', 'Unnamed: 17': u'WHITE UNKNOWN', 'Unnamed: 14': u'WHITE FEMALE', 'Unnamed: 59': u'UNKNOWN FEMALE', 'Unnamed: 38': u'NATIVE-AM MALE', 'Unnamed: 11': u'WHITE MALE', 'Unnamed: 35': u'HISP-LT UNKNOWN', 'Unnamed: 50': u'OTHER FEMALE', 'Unnamed: 56': u'UNKNOWN MALE', 'Unnamed: 32': u'HISP-LT FEMALE'},inplace=True)
df_total_registered = df_percentage_voted.iloc[1:]

df_total_registered.to_csv('/Users/sammahle/Downloads/Congressional/tr.csv',index=None)
df_voted.to_csv('/Users/sammahle/Downloads/Congressional/tv.csv',index=None)
df_percentage_voted.to_csv('/Users/sammahle/Downloads/Congressional/pv.csv',index=None)
