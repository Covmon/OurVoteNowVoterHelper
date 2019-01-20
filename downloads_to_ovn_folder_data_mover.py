import os 
import re
import zipfile
import shutil

for download in os.listdir('/Users/sammahle/Downloads'):

	if re.search(r'\D+\d{1,2}_\d{4}',download):

		date = re.findall(r'\D+\d{1,2}_\d{4}',download)[0]
		year = re.findall(r'\d{4}',download)[0]
		month = re.findall(r'^\D+',date)[0]

		if 'age' in download.lower():
			date = date + '(Age)'
			typee = '(Age)'
		elif 'cong' in download.lower():
			date = date + '(CongressionalDistricts)'
			typee = '(Congressional Districts)'
		elif 'precinct' in download.lower():
			date = date + '(CountyPrecinct)'
			typee = '(County Precinct)'
		elif 'county' in download.lower():
			date = date + '(Statewide)'
			typee = '(County)'

		print date

		with zipfile.ZipFile('/Users/sammahle/Downloads/{}'.format(download), 'r') as zip_ref:
			zip_ref.extractall('/Users/sammahle/Downloads/{}'.format(date))

		zip_file_name = download
		file_name = zip_file_name.replace('.zip','')
		zip_file_path = '/Users/sammahle/Downloads/{}'.format(zip_file_name)
		current_file_path = '/Users/sammahle/Downloads/{}'.format(date)
		desired_file_path_year = '/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_Source_XLSX/{}/{}'.format(year,date)

		if not os.path.exists(desired_file_path_year):
			shutil.copytree(current_file_path, desired_file_path_year)

		if os.path.isdir(desired_file_path_year):
			shutil.rmtree(desired_file_path_year)
		try:
			os.rename(current_file_path, desired_file_path_year)
		except:
			pass

		os.remove(zip_file_path)