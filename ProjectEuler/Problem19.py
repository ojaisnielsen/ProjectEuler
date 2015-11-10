

def is_leap(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

month_durations = [
	lambda leap: 31, # Jan
	lambda leap: 29 if leap else 28, # Feb
	lambda leap: 31, # Mar
	lambda leap: 30, # Apr
	lambda leap: 31, # May
	lambda leap: 30, # Jun
	lambda leap: 31, # Jul
	lambda leap: 31, # Au
	lambda leap: 30, # Sep
	lambda leap: 31, # Oct
	lambda leap: 30, # Nov
	lambda leap: 31 # Dec
]

i = 0
day_of_year = 1
day_of_month = 1
year = 1900
month = 1
counter = 0
while True:
	leap = is_leap(year)
	if year >= 1901 and year <= 2000 and i % 7 == 6 and day_of_month == 1:
		counter = counter + 1
		print year, month, day_of_month, day_of_year

	if year > 2000:
		break

	i = i + 1
	day_of_year = day_of_year + 1
	day_of_month = day_of_month + 1

	if (leap and day_of_year > 366) or (not leap and day_of_year > 365):
		year = year + 1
		month = 1
		day_of_year = 1
		day_of_month = 1
	elif day_of_month > month_durations[month - 1](leap):
		month = month + 1
		day_of_month = 1



print counter


