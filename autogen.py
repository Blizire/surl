# automatically generates data for the main
# website to test visual functionality

import db
import string

# writes records to db
def db_add_record(db_name, url, customurl):
	try:
		testdb = db.UrlTables(db_name=db_name)
		testdb.add_record(url, customurl)
		return True
	except:
		return False


if __name__ == "__main__":
    for character in string.ascii_uppercase:
        for i in range(20):
            db_name = 'urltables.db'
            custom_url = f'{character}{i}'
            url = f'https://127.0.0.1:5000/{character}{i}'
            db_add_record(db_name, url, custom_url)
            print(f'{url}', f'{custom_url}')