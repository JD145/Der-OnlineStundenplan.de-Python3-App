#!/usr/bin/python3

# ---------- 'Der-Onlinestundenplan.de - Python3 commandline tool' ---------- 

import json
import urllib.request
from pprint import pprint
import argparse

APP_VERSION = 1.0

def main():

	# parse Arguments
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-ls','--schools', action='store_true', help='Lists all available schools.')
	parser.add_argument('-s','--school', help='Selects a school. If not class is selected, the schoolinfo will be shown.')
	parser.add_argument('-lc','--classes', action='store_true', help='Lists all classes of a school. Requires a selection if a school.')
	parser.add_argument('-c','--schoolClass', help='Selects a class. If a school is also selected the timetable will be shown.')
	parser.add_argument('-rw','--relativeWeek', help='Selects a relative week for timetable, if school and class are selected.')

	args = parser.parse_args()

	if args.schools: 
		GetSchools()
	else:
		if args.school is not None:
			if args.schoolClass is not None:
				if args.relativeWeek is not None:
					GetTimetable(args.school,args.schoolClass,args.relativeWeek)
				else:
					GetTimetable(args.school,args.schoolClass,0)
			else:
				if args.classes:
					GetClasses(args.school)
				else:
					GetSchoolInfo(args.school)
		else:
			print('Der-OnlineStundenplan.de - Python3 App\n')
			parser.print_help()

	return


# Function for printing a simple table
def printTable(table):
    col_width = [max(len(x) for x in col) for col in zip(*table)]
        
    for line in table:
        print('| ' + ' | '.join('{:{}}'.format(x, col_width[i])
                for i, x in enumerate(line)) + ' |')
    return


def GetSchools():
	fineJson = GetJson('http://der-onlinestundenplan.de/api/v1/school')

	print('Available schools:\n')
	table =  [('Name','City')] # ,'Website,
	table += [('--')]
	table += [(key[u'name'], key[u'city']) # , key[u'website']
			for key in fineJson[u'schools']]
	printTable(table)
	return 

def GetSchoolInfo(school):
	fineJson = GetJson('http://der-onlinestundenplan.de/api/v1/school/' + school + '/')

	print('Schoolinfo for \'' + school + '\':\n')
	table =  [('Name','City','Website')]
	table += [('---')]
	table += [(fineJson[u'name'], fineJson[u'city'], fineJson[u'website'])]
	printTable(table)
	return	

def GetClasses(school):
	fineJson = GetJson('http://der-onlinestundenplan.de/api/v1/school/' + school + '/class')

	print('Classes for \'' + school + '\':\n')
	table =  [('Class')]
	table += [('-')]

	for key in fineJson[u'classes']:
		table += [(key)]

	printTable(table)
	return

def GetTimetable(school,schoolClass,relativeWeek):
	fineJson = GetJson('http://der-onlinestundenplan.de/api/v1/school/' + school + '/class/' + schoolClass + '/' + str(relativeWeek))

	print('Timetable for class \'' + schoolClass + '\' of school \'' + school + '\':\n')
	print('Week: ' + str(fineJson[u'week']))
	print('Last updated: ' + fineJson[u'last_updated'] + '\n')

	headline = [(key[u'name']) for key in fineJson[u'timeTable'][u'days']]
	lessons = [(key[u'data']) for key in fineJson[u'timeTable'][u'days']]
	times = [(key) for key in fineJson[u'timeTable'][u'times']]

	cols = len(headline) + 1
	rows = len(times) + 2

	timetable = [['' for i in range(cols)] for j in range(rows)]

	# j = Zeile ; i = Spalte
	for i in range(cols):
		if (i > 0):
			timetable[0][i] = str(headline[i-1])

		for j in range(rows):
			if (j == 1):
				timetable[j][i] = '-' # '---' als Füllzeichen in Funktion printTable implementieren, damit ganze Zeile befüllt wird

			if (j > 1):
				timetable[j][0] = str(times[j-2])

				if (len(lessons[i-1]) > j-2):
					timetable[j][i] = FormatLessonForTimetable(lessons[i-1][j-2])
			
	printTable(timetable)
	return

# Function for formatting a lesson 
# Parameter: lessonDescription -> dynamic array of dynamic array of strings
def FormatLessonForTimetable(lessonDescription):
	formattedLesson = ''

	for i in range(len(lessonDescription)):
		if (formattedLesson == ''):
			
			for j in range(len(lessonDescription[i])):
				formattedLesson += str(lessonDescription[i][j])

				if (j+1 < len(lessonDescription[i])):
					formattedLesson += ' | '

		else:
			formattedLesson += ' , '

			for j in range(len(lessonDescription[i])):
				formattedLesson += str(lessonDescription[i][j])

				if (j+1 < len(lessonDescription[i])):
					formattedLesson += ' | '

	return formattedLesson

def GetJson(url):
	
	req = urllib.request.Request(
	    url, 
	    data=None, 
	    headers={'User-Agent': 'Der-OnlineStundenplan.de (Python3 / Version ' + APP_VERSION + ' )'}
		)

	rawJson = urllib.request.urlopen(req).read()
	fineJson = json.loads(str(rawJson,'utf-8'))	
	return fineJson


main()
