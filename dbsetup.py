import pymysql 
import dbconfig
connection = pymysql.connect(host='localhost', user=dbconfig.db_user,passwd=dbconfig.db_passwd)
try:
	cursor =  connection.cursor()
	sql = "CREATE DATABASE IF NOT EXISTS CRIMEAPP"
	try: 
		cursor.execute(sql)
	except MySQLdb.Warning as e:
		print ("Mysql Warning ")
	except Warning as e:
		print ("Mysql Warning ")

	sql = """CREATE TABLE IF NOT EXISTS CRIMEAPP.crimes (
			id int NOT NULL AUTO_INCREMENT,
			latitude FLOAT(10,6),
			longitude FLOAT(10,6),
			date DATETIME,
			category VARCHAR(50),
			description VARCHAR(1000),
			updated_at TIMESTAMP,
			PRIMARY KEY (id)
			)"""
	cursor.execute(sql)
	connection.commit()
finally:
	cursor.close()
	connection.close()



