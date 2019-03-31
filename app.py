from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome"


@app.route("/user/<int:id>/")
def users(id):
	id += 1
	return "Your id is {}".format(id)


@app.route("/hello")
def hello():
	print(request.args)
	naam = "Nikhil"
	data = [["Ram", 9, 9],
			["Shyam", 8, 9],
			["Ravi", 10, 10]]
	colors = ["red", "green", "blue"]
	return render_template("test.html", name=naam,  
		now=datetime.now().strftime("%d %B, %Y %I:%M %p"), 
		data=data, colors=colors)


@app.route("/form", methods=['GET', 'POST'])
def submit_data():
	if request.method == 'GET':
		return render_template("form.html")
	else:
		name = request.form.get('name')
		clas = request.form.get('class')
		image = request.files.get('image')
		ext = image.filename.split('.')[-1]
		image.save("static/images/{}.{}".format(name, ext))
		return "Your name is {} and class is {}".format(name, clas)


if __name__ == "__main__":
	app.run(port=8000, use_reloader=True, debug=True)