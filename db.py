import sqlite3
from os.path import isfile


class UrlTables:
	# Note:
	#  important to close after each transaction because same
	#  session cannot be used over multiple threads

	#  TABLE urlmap:
	#  URL   = Destination the user will be redirected too
	#  ROUTE = Part of the url ex. https://exdomain.com/ROUTE

	def __init__(self, db_name="urltables.db"):
		flag_exist = None
		self.db_name = db_name

		# check if db file already exists
		if isfile(self.db_name):
			flag_exist = True
		else:
			flag_exist = False

		# will connect and/or create db file
		try:
			self.conn = sqlite3.connect(self.db_name)
			self.cursor = self.conn.cursor()
		except:
			print("Error conencting to database!")		
		
		# if it did not exist before hand create initial tables
		if not flag_exist:
			self.cursor.execute("""CREATE TABLE urlmap
									(id integer primary key not null, 
									dest text NOT NULL, 
									route text NOT NULL UNIQUE)""")
			self.conn.commit()

	# puts a url and the according route in the same record in DB
	def add_record(self, dest, route):
		self.cursor.execute("""INSERT INTO urlmap (dest, route)
								VALUES (?,?)""", (dest, route))
		self.conn.commit()

	# only obtain records by route since they are the only value that should be unique
	def get_record(self, route):
		self.cursor.execute("""SELECT * FROM urlmap WHERE route=?""", (route, ))
		return self.cursor.fetchone()
	
	# method to pull x amount of records and return it in an array
	def get_page(self, page=0, amount=10):
		offset = int(page) * 10
		self.cursor.execute("""SELECT * FROM urlmap ORDER BY id DESC LIMIT ? OFFSET ? """, (amount, offset))
		return self.cursor.fetchall()

	# save + close DB connection
	def close(self):
		self.conn.commit()
		self.conn.close()

