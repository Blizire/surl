from os import remove
from os.path import isfile
import sqlite3

import db


# test if we can successfully create db then remove
def db_creation():
	db_name = "test.db"
	db.UrlTables(db_name=db_name)
	if(isfile(db_name)):
		return True
	else:
		return False


# check to see if we can add to DB
def db_add_record():
	db_name = "test.db"
	try:
		testdb = db.UrlTables(db_name=db_name)
		testdb.add_record("https://example.com", "ts2")
		return True
	except:
		return False


# 2 in 1 check for add_record and see if we can retrieve the record it submitted
def db_get_record():
	try:
		db_name = "test.db"
		testdb = db.UrlTables(db_name=db_name)
		res = testdb.get_record("ts2")
		if(res == ("https://example.com", "ts2")):
			return True
		else:
			return False
	except:
		return False


# see if we can pull x amount of records per y page
def db_get_page():
	db_name = "test.db"
	testdb = None
	try:
		testdb = db.UrlTables(db_name=db_name)
	except:
		return False
	
	# push in 30 records to test the page pull
	for i in range(30):
		url = "https://www.website.com/%d" % i
		site = "a%d" % i
		testdb.add_record(url, site)
	# should pull 15 records ( rows 9 - 23)
	page_results = testdb.get_page(page=0, amount=15)
	print(page_results)
	if(len(page_results) == 15):
		return True
	else:
		return False


def test(test_name, routine):
	print("Testing : %s" % test_name)
	if (routine()):
		print("passed.")
	else:
		print("failed.")


if __name__ == "__main__":
	# ensure clean start
	if isfile("test.db"):
		remove("test.db")

	test("db_creation", db_creation)
	test("db_add_record", db_add_record)
	test("db_get_record", db_get_record)
	test("db_get_page", db_get_page)