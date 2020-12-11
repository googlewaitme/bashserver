from bd.models.models import Question, PassingQuestion, Answer, ReadedTheory


class QuestionApi:
	def __init__(self, user_api):
		self.question = None
		self.user_api = user_api

	def set_user(self, user_api):
		self.user_api = user_api

	def set_question(self, question):
		self.question = question

	def set_question_by_id(self, question_id):
		question = Question.get(Question.index==question_id)
		self.question = question 

	def give_question(self):
		assert self.question
		return self.question

	def give_question_model(self):
		return self.question

	def give_all_questions(self):
		query = Question.select()
		list_questions = list(query)
		return list_questions

	def give_avaible_questions(self):
		list_questions = self.give_all_questions()
		query_readed_theories =  ReadedTheory.select().where(ReadedTheory.user==self.user_api.give_user_model())
		readed_theories = [el.theory for el in query_readed_theories]
		avaible_questoins = list()
		for question in list_questions:
			if question.theory in readed_theories:
				avaible_questoins.append(question)
		return avaible_questoins 

	def give_passed_questions(self):
		query = PassingQuestion.select().where((PassingQuestion.user==self.user_api.give_user()) & (PassingQuestion.is_right==True))
		passed_questions = list()
		for passed_question in query:
			passed_questions.append(passed_question.question)
		return passed_questions 

	def give_not_passed_questions(self):
		all_questions = set(self.give_avaible_questions())
		passed_questions = set(self.give_passed_questions())
		not_passed_questions = all_questions  - passed_questions
		print(not_passed_questions)
		return list(not_passed_questions)

	def all_tests_are_passed(self):
		return len(self.give_not_passed_questions) == 0

	def set_new_question(self):
		list_questions = self.give_not_passed_questions()
		if len(list_questions) > 0:
			self.set_question(list_questions[0])
			return True
		else:
			return False

	def give_all_answer_models_for_question(self, question):
		query = Answer.select().where(Answer.question==self.question)
		answers = list(query)
		return answers

	def give_right_answer_model(self, question_id):
		self.set_question_by_id(question_id)
		right_answer = Answer.get(Answer.question==self.question, Answer.is_right==True)
		return right_answer

	def check_user_answer(self, question_id, user_answer):
		right_answer = self.give_right_answer_model(question_id)
		is_right = right_answer.text.lower() == user_answer.lower()
		if self.user_passed_question(question_id):
			passing_question = self.give_passing_question_by_id(question_id)
			passing_question.is_right = is_right
			passing_question.save()
		else:
			PassingQuestion.create(question=self.question, user=self.user_api.give_user(), is_right=is_right)
		return is_right

	def user_passed_question(self, question_id):
		query = PassingQuestion.select().where(
			(PassingQuestion.question==question_id) & (PassingQuestion.user==self.user_api.give_user_model())
		)
		questions = list(query)
		assert len(questions) <= 1
		return len(questions) == 1

	def give_passing_question_by_id(self, question_id):
		passed_question = PassingQuestion.get(
			(PassingQuestion.question==question_id) & (PassingQuestion.user==self.user_api.give_user_model())
		)
		return passed_question
