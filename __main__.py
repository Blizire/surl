#!/usr/bin/env python

# Author      : Trenton Stiles
# Name        : surl.py
# Description : A URL shortneing service that emulates the premium ones that
#               allow you to create custom URL shortned links from your domain.

from flask import Flask, render_template, request, redirect
from db import UrlTables
from urllib.parse import quote


app = Flask(__name__)


# if duplicate return true
def check_dupe(path):
    db = UrlTables("urltables.db")
    record = db.get_record(path)
    if record:
        db.close()
        return True
    else:
        db.close()
        return False


# saves url to sql db along with the mapping
def save_url_map(url, path):
    # strip / (will not route properly w/ them)
    path = path.strip("/")
    # make sure path is urlencoded
    path = quote(path)
    # make sure no duplicates get added to db
    if not check_dupe(path):
        db = UrlTables("urltables.db")
        db.add_record(url, path)
        db.close()
        return True
    return False


# pull 10 records from database at a time
def pull_page_records(pagenum, record_amount=10):
    db = UrlTables("urltables.db")
    result = db.get_page(page=pagenum, amount=record_amount)
    db.close()
    return result


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        path = request.form["route"]
        if not save_url_map(url, path):
            print("Duplicate entry input (%s, %s)" % (url, path))
    return render_template("home.html")


@app.route("/view/<int:page>", methods=["GET"])
def view(page="0"):
    records = pull_page_records(page)
    next = int(page) + 1
    # bug here ( stil goes to -1 sometimes )
    if next < 0:
        next = 0
    back = int(page) - 1
    return render_template("view.html", records=records, next=next, back=back)


@app.route("/route/<text>")
def route(text=None):
    if text:
        db = UrlTables("urltables.db")
        # must url encode, text is recv'd its not url encoded but in DB it is
        text = quote(text)
        result = db.get_record(text)
        # if None redirect back home
        if result:
            url = result[1]
            # commented out because redirect should not be urlencoded
            # url = quote(url)
            return redirect(url)
    return redirect("/")


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)