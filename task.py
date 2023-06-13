# # importing required libraries
# import mysql.connector

# # dataBase = mysql.connector.connect(
# # host ="localhost",
# # user ="user",
# # passwd ="password",
# # database = "gfg"
# # )
# dataBase=mysql.connector.connect(host='stagingdb2.mycareers360.com',username='staging',password='cklp0874*&$(#%3rxv?',database='django360')

# # preparing a cursor object
# cursorObject = dataBase.cursor()

# query = "SELECT id,name,country_id from colleges LIMIT 10"
# cursorObject.execute(query)

# myresult = cursorObject.fetchall()

# for x in myresult:
# 	print(x)

# # disconnecting from server
# dataBase.close()





import mysql.connector
import csv

connection=mysql.connector.connect(host='stagingdb2.mycareers360.com',username='staging',password='cklp0874*&$(#%3rxv?',database='django360')
cursor=connection.cursor()
records=1
with open('ra.csv', mode ='r') as file:   
	file_data = csv.DictReader(file)
	
	for row in file_data:
		print('college_id:',row.get('college_id'),)
		# row.get('ranking_authority')
		# row.get('ranking_year')
		print('====>', type(row.get('overall_rank')))
		overall_rank = row.get('overall_rank')
		overall_score = row.get('overall_score')
		college_id = row.get('college_id')
		ranking_authority = row.get('ranking_authority')
		ranking_year = row.get('ranking_year')
		overall_total_score = row.get('overall_total_score')
		parameter_id = row.get('parameter_id')
		parameter_score = row.get('parameter_score')
		rank_band = row.get('rank_band')
		country = row.get('country')
		if overall_rank == '':
			overall_rank = 'null'
		if overall_score == '':
			overall_score = 'null'
		if college_id == '':
			college_id = 'null'
		if ranking_authority == '':
			ranking_authority = 'null'
		if ranking_year == '':
			ranking_year = 'null'
		if overall_total_score == '':
			overall_total_score = 'null'
		if parameter_id == '':
			parameter_id = 'null'
		if parameter_score == '':
			parameter_score = 'null'
		if rank_band == '':
			rank_band = 'null'
		if country == '':
			country = 'null'
		# row.get('overall_score')
		# row.get('overall_total_score')
		# row.get('parameter_id')
		# row.get('parameter_score')
		# row.get('rank_band')
		print('country==',row.get('country'))
		print("""INSERT INTO task(college_id,ranking_authority,ranking_year,overall_rank,overall_score,overall_total_score,parameter_id,parameter_score,rank_band,country) VALUES(%s,%s,%s,%s,'%s',%s,%s,'%s','%s','%s')""" %(row.get('college_id'),row.get('ranking_authority'),row.get('ranking_year'),row.get('overall_rank', None),str(row.get('overall_score')),row.get('overall_total_score'), row.get('parameter_id'), row.get('parameter_score'), row.get('rank_band'),row.get('country')))
		cursor.execute("""INSERT INTO task(college_id,ranking_authority,ranking_year,overall_rank,overall_score,overall_total_score,parameter_id,parameter_score,rank_band,country) VALUES(%s,%s,%s,%s,'%s',%s,%s,'%s','%s','%s')""" %(college_id,ranking_authority,ranking_year,overall_rank,overall_score,overall_total_score,parameter_id, parameter_score, rank_band),country'))
		# cursor.execute("""INSERT INTO task(college_id,ranking_authority,ranking_year,overall_rank,overall_score,overall_total_score,parameter_id,parameter_score,rank_band,Country) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" %(row.get('college_id'),row.get('college_id'),row.get('college_id'),row.get('college_id'),row.get('college_id'),row.get('college_id'),row.get('college_id'),row.get('college_id'),row.get('college_id'),row.get('college_id')))
		connection.commit()
connection.close()
print("\n{} records transferred".format(records))

