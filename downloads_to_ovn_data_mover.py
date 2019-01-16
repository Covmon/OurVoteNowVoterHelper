import os 
import re
import zipfile

for download in os.listdir('/Users/sammahle/Downloads'):

	if re.search(r'\D+\d{1,2}_\d{4}',download):

		with zipfile.ZipFile('/Users/sammahle/Downloads/{}'.format(download), 'r') as zip_ref:
			zip_ref.extractall('/Users/sammahle/Downloads')

		date = re.findall(r'\D+\d{1,2}_\d{4}',download)[0]
		year = re.findall(r'\d{4}',download)[0]

		if 'age' in download.lower():
			date = date + '(Age)'
		elif 'congress' in download.lower():
			date = date + '(CongressionalDistricts)'
		elif 'precinct' in download.lower():
			date = date + '(County Precinct)'
		elif 'county' in download.lower():
			date = date + '(Statewide)'


		zip_file_name = download
		file_name = zip_file_name.replace('.zip','')
		zip_file_path = '/Users/sammahle/Downloads/{}'.format(zip_file_name)

		current_file_path = '/Users/sammahle/Downloads/{}'.format(file_name)
		desired_file_path_year = '/Users/sammahle/Downloads/openelections-data-master/{}/{}'.format(year,date)

		if os.path.isdir(desired_file_path_year):
			shutil.rmtree(desired_file_path_year)
		try:
			os.rename(current_file_path_year, desired_file_path_year)
		except:
			pass

		os.remove(zip_file_path)