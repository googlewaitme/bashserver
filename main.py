from flask import Flask
from logik import Logik


app = Flask(__name__)
logik = Logik()


@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/add_user/<user_id>/')
def add_user(user_id):
	json = logik.add_user(user_id)
	return json

@app.route('/user_is_exist/<user_id>/')
def user_is_exist(user_id):
	json = logik.user_is_exist(user_id)
	return json

@app.route('/remove_user/<user_id>/')
def remove_user(user_id):
	json = logik.remove_user(user_id)
	return json


@app.route('/give_theory/<user_id>/')
def give_theory(user_id):
	json = logik.give_theory(user_id)
	return json

@app.route('/set_user_read_theory/<user_id>/<theory_id>/')
def set_user_read_theory(user_id, theory_id):
	json = logik.set_user_read_theory(user_id, theory_id)
	return json


@app.route('/give_question/<user_id>/')
def give_question(user_id):
	json = logik.give_question(user_id)
	return json

@app.route('/check_user_answer/<user_id>/<question_id>/<user_answer>/')
def check_user_answer(user_id, question_id, user_answer):
	json = logik.check_user_answer(user_id, question_id, user_answer)
	return json


if __name__ == '__main__':
	app.debug = True
	app.run()