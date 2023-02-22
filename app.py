from flask import Flask, render_template, request
import sqlite3
from vc import text_to_speech
from datetime import datetime
import requests


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')

connect = sqlite3.connect('users.db')
connect.execute('CREATE TABLE IF NOT EXISTS USERS (name TEXT, surname TEXT, phone TEXT, debt INTEGER,valute TEXT)')

@app.route('/join', methods=['GET', 'POST'])
def join():
	if request.method == 'POST':
		name = request.form['name']
		surname = request.form['surname']
		phone = request.form['phone']
		debt = request.form['debt']
		valute = request.form['valute']
		with sqlite3.connect("users.db") as users:
			cursor = users.cursor()
			cursor.execute("INSERT INTO USERS (name,surname,phone,debt,valute) VALUES (?,?,?,?,?)",(name, surname, phone, debt, valute))
			users.commit()
		return render_template("index.html")
	else:
		return render_template('join.html')
	
@app.route('/search', methods=['GET', 'POST'])
def search():
	t =0

	if request.method == 'POST':
		name = request.form['search_usr']
		with sqlite3.connect("users.db") as users:
			cursor = users.cursor()
			cursor.execute("SELECT * FROM USERS WHERE name=?", (name,))
			data = cursor.fetchall()
			if not data:
				text_to_speech('user not found')
				return render_template("search.html", not_found=True)
			else:	
				text_to_speech(f"{data[0][0]} has a debt of {data[0][3]} {data[0][4]} ")
				x = f"{data[0][0]} აქვს {data[0][3]}  {data[0][4]} ვალი" 
				return render_template("search.html", data=data, not_found=False, x=x,y=data[0][3],z=data[0][4])
	else:
		return render_template('search.html', not_found=None)

# show all data
@app.route('/participants')
def participants():
	connect = sqlite3.connect('users.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM USERS')
	data = cursor.fetchall()
	x = sorted(data)

	return render_template("participants.html", data=x)
# delete user from database
@app.route('/delete/<name>')
def delete(name):
	with sqlite3.connect("users.db") as users:
		cursor = users.cursor()
		cursor.execute("DELETE FROM USERS WHERE name=?", (name,))
		users.commit()
	return render_template("participants.html", data=cursor.fetchall())


if __name__ == '__main__':
	app.run(debug=True)
 