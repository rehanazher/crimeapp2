import pymysql
import datetime
import dbconfig

class DBHelper:
	def __init__(self):
		print ("DBHelper initialized")

	def connect (self, database='CRIMEAPP'):
		return pymysql.connect(host='localhost',port=3306,user=dbconfig.db_user,passwd=dbconfig.db_passwd,db='CRIMEAPP')
	
	def get_all_inputs(self):
		connection = self.connect()
		try:
			query = "SELECT description FROM crimes;"
			with connection.cursor() as cursor:
				cursor.execute(query)
				print ("ROW COUNT %d " % cursor.rowcount)
				return cursor.fetchall()
		finally:
			connection.close()
	
	def add_input(self,data):
		connection = self.connect()
		try:
			query = "INSERT INTO crimes (description) VALUES (%s);"
			cursor = connection.cursor()
			cursor.execute(query,data)
			connection.commit()
		finally:
			cursor.close()
			connection.close()

	def clear_all(self):
		connection = self.connect()
		try:
			query = "DELETE FROM crimes;"
			cursor = connection.cursor()
			cursor.execute(query)
			connection.commit()
		finally:
			cursor.close()
			connection.close()

	def add_crime(self, category, date, latitude, longitude,description):
		connection = self.connect()
		try:
			query = "INSERT INTO crimes (category, date, latitude,longitude, description) VALUES (%s, %s, %s, %s, %s)"
			cursor = connection.cursor()
			cursor.execute(query, (category, date, latitude, longitude,description))
			connection.commit()
		except Exception as e:
			print(e)
		finally:
			cursor.close()
			connection.close()

	def get_all_crimes(self):
		connection = self.connect()
		try:
			query = "SELECT latitude, longitude, date, category,description FROM crimes;"
			with connection.cursor() as cursor:
				cursor.execute(query)
				named_crimes = []
				for crime in cursor:
					named_crime = {
					'latitude': crime[0],
					'longitude': crime[1],
					'date': datetime.datetime.strftime(crime[2], '%Y-%m-%d'),
					'category': crime[3],
					'description': crime[4]
					}
					named_crimes.append(named_crime)
					return named_crimes
		finally:
			connection.close()