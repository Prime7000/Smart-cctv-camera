from flask import Flask
from flask import render_template, request,redirect, jsonify

app = Flask(__name__)

@app.route('/')
def home():

	return render_template('home.html')

@app.route('/live_preview')
def live_preview():

	return render_template('live_preview.html')

@app.route('/settings')
def settings():

	return render_template('settings.html')

@app.route('/records')
def records():

	return render_template('records.html')

if __name__ == '__main__':
	app.run(debug=True, port=8000)