# randgen.py
#
# tool to generate random data into the database to
# test with.

import requests
import random
import string


def rand_string():
	max_size = random.randrange(5,10)
	r_str = ""
	for i in range(5, max_size):
		r_str += random.choice(string.ascii_letters)
	return r_str


if __name__ == "__main__":
	url_count = 100
	url = "https://en.wikipedia.org/wiki/Wikipedia:URLShortener"
	for i in range(url_count):
		route = rand_string()
		data = {"url": url, "route": route}
		res = requests.post("http://127.0.0.1:5000/", data=data)
		print(res.status_code)

