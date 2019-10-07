# flask_pymongo_example.py
# https://flask-pymongo.readthedocs.io/en/latest/

from flask import Flask, jsonify, abort
from flask_pymongo import PyMongo

# import your main app if this is not your main app. I generally just use app.py or /app/__init__.py as my main app file
# from app import app

app = Flask(__name__)  # used if this is your main app. I prefer to include this file as a utility

database = 'myDatabase'
app.config['MONGO_DBNAME'] = database
app.config["MONGO_URI"] = "mongodb://localhost:27017/" + database
mongo = PyMongo(app)


def find(collection, query):
	results = ''
	rows = mongo.db[collection]
	for row in rows.find(query):
		# do something with the column values from the current row
		print(jsonify(row))
		results += jsonify(row)
	return results


def find_one(collection, query):
	rows = mongo.db[collection]
	row = rows.find_one(query)

	# return 404 if not found, useful if you have a default error catcher
	# row = rows.find_one_or_404(query)

	# do something with the column values from the found row
	if row:
		print(jsonify(row))
		return row
	abort(418)  # do your error catching


# test method
@app.route('/')
def test():
	find('testCollection', {"_id": "1"})
	find_one('testCollection', {"_id": "1"})


# used if this is your main app. I prefer to include this file as a utility
if __name__ == '__main__':
	app.run()
