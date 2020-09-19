import pytest
from models.models import *
from peewee import *

class Tess_ModelPassingQuestion:

	def setup_class(self):
		self.user = User(user_id='vk_234')
		self.theory = Theory(theme='lala', text='rur')
		self.question = Question(theory=self.theory, text='is it test?')
		self.second_question = Question(theory=self.theory, text='some text')
		self.passing_question = PassingQuestion(user=self.user, question=self.question, is_right=False)
		self.default_passing_question = PassingQuestion(user=self.user, question=self.second_question)

	def teardown_class(self):
		objects_for_deleting = [self.user, self.theory, self.question, self.user]
		for obj in objects_for_deleting:
			obj.delete_instance()

	def test_user_in_passing_question_is_user(self):
		assert self.passing_question.user is self.user

	def test_question_in_passing_question_is_question(self):
		assert self.passing_question.question is self.question

	def test_default_position_is_right_in_question(self):
		assert self.default_passing_question.is_right == False 
