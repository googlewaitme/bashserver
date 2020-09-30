from bd import user_api, theory_api, question_api
from formation import *

class Logik:
	def __init__(self):
		self.theory = theory_api.TheoryApi()
		self.user = user_api.UserApi()
		self.question = question_api.QuestionApi(self.user)

	def update_user_id(self, user_id):
		self.user.set_user_id(user_id)
		self.question.set_user(self.user)

	def add_user(self, user_id):
		self.update_user_id(user_id)
		self.user.add()
		return JSON_TRUE

	def remove_user(self, user_id):
		self.update_user_id(user_id)
		self.user.remove()
		return JSON_TRUE

	def give_theory(self, user_id):
		self.update_user_id(user_id)
		user_model = self.user.give_user_model()
		theories = self.theory.give_theories_that_user_has_not_read(user_model)
		if len(theories) == 0:
			dict_answer = {
				'id': 1,
				'theme': 'Поздравляю! Вы прошли всю теорию',
				'text': 'Ты можешь показать данное сообщение учителю'
			}
		else:
			dict_answer = theory_to_dict(theories[0])
		json_answer = make_json(dict_answer)
		return json_answer
				
	def give_question(self, user_id):
		self.update_user_id(user_id)
		if self.question.set_new_question():
			question = self.question.give_question_model()
			dict_answer = question_to_dict(question)
			answers_list = self.question.give_all_answer_models_for_question(question)
			answers_list = answers_to_list(answers_list)
			dict_answer['answers'] = answers_list
		else:
			dict_answer = {
				'id': 1,
				'text': 'Вы прошли все тесты из этой темы!'
			}
		json_answer = make_json(dict_answer)
		return json_answer

	def check_user_answer(self, user_id, question_id, user_answer):
		self.update_user_id(user_id)
		right_answer = self.question.give_right_answer_model(question_id).text
		answer_is_right = self.question.check_user_answer(question_id, user_answer)
		dict_answer = {
			'user_answer_is_right': answer_is_right,
			'right_answer': right_answer
		}	
		json_answer = make_json(dict_answer)
		return json_answer	

	def user_is_exist(self, user_id):
		self.update_user_id(user_id)
		if self.user.is_exist():
			return JSON_TRUE
		else:
			return JSON_FALSE 

	def set_user_read_theory(self, user_id, theory_id):
		self.update_user_id(user_id)
		self.user.add_readed_theory(theory_id)
		return JSON_TRUE
