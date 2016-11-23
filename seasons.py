import pandas as pd

data = pd.read_excel('movies_data.xlsx')
writer = open('seasons.txt', 'w')
for i in range(len(data)):

	# remove the year from the datetime
	# convert the datetime into a string for comparisons
	d = data['Release Date'][i]
	date = ''
	if len(str(d.month)) < 2:
		date += '0'
	date += str(d.month) + '-' 
	if len(str(d.day)) < 2:
		date += '0'
	date += str(d.day)

	# determine the season based on the date the film was released
	season = ''
	if date >= '03-20' and date < '06-21':
		season = 'Spring'
	elif date >='06-21' and date < '09-23':
		season = 'Summer'
	elif date >= '09-23' and date < '12-21':
		season = 'Autumn'
	else:
		season = 'Winter'

	writer.write(season + '\n')

writer.close()