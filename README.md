# surl
a local service you can use for making shortened URLS or custom redirects.

*still a work in progress...*

- [x] submit urls to shorten and redirect too
- [x] view shortened urls from /view
- [ ] add page navigation to /view
- [ ] functionality right click to delete or modify
- [ ] popup message of shortned link user submits
- [ ] sanitize urls to make sure its FQDN
- [ ] add rate limiting if exposed to internet
- [ ] limit url and shortned url size
- [ ] unit testing on actual site rather then DB checks

**note**

The script tools/randgen.py is used to generate submissions into the database for testing.

./unit_test.py currently only tests DB creation and validation of data
submitted and pulled. 
