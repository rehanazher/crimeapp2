import dbconfig
import pymysql

class DBHelper:

	def connect (self, database:'crimeapp'):
		return pymysql.connect(host="localhsot",user=dbconfig.db_user, password = dbconfig.db_passwd, db=database)
	
	def get_all_inputs(self):
		connection = self.connect()
		try:
			query = "SELECT description FROM crimes;"
			with connection.cursor() as cursor:
				cursor.execute(query)
				return cursor.fetchall()
		finally:
			connection.close()
	
	def add_input(self,data):
		connection = self.connect()
		try:
			query = "INSERT INTO CRIPMES (description) VALUES ('{}');".format(data)
			with connection.cursor as cursor:
				cursor.execute(query)
				connection.commit()
		finally:
			connection.close()

	def clear_all(self):
		connection = self.connect()
		try:
			query = "DELETE FROM crimes;"
			with connection.cursor as cursor:
				cursor.execute(query)
				connection.commit()
		finally:
			connection.close()
