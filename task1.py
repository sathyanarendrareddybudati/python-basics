import mysql.connector
connection=mysql.connector.connect(host='stagingdb2.mycareers360.com',username='staging',password='cklp0874*&$(#%3rxv?',database='django360')
cursor=connection.cursor()
file=open('abc1.csv','r')
records=0
for row in file:
  
    cursor.execute("INSERT INTO task3(college_id,ranking_authority,ranking_year,overall_rank,overall_score,overall_total_score,parameter_id,parameter_score,rank_band) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",row.split(","))
    connection.commit()
    records+=1
connection.close()
print("\n{} records transferred".format(records))
file.close()