import pytest
from models.models import Answer, Question, Theory
from peewee import *


class Test_ModelAnswer:

	def setup_class(self):
		self.theory = Theory(theme='lala', text='rur')
		self.question = Question(theory=self.theory, text='is it test?')
		self.right_answer = Answer(question=self.question, text='right', is_right=True)
		self.false_answer = Answer(question=self.question, text='false', is_right=False)
		self.default_answer = Answer(question=self.question, text='default')

	def teardown_class(self):
		self.theory.delete_instance()
		self.question.delete_instance()
		self.right_answer.delete_instance()
		self.false_answer.delete_instance()

	def test_right_answer(self):
		assert self.right_answer.is_right

	def test_fasle_answer(self):
		assert not self.false_answer.is_right

	def test_texts_answer(self):
		assert self.right_answer.text == 'right'
		assert self.false_answer.text == 'false'

	def test_question_from_answers_is_question(self):
		assert self.right_answer.question is self.question
		assert self.false_answer.question is self.question

	def test_answer_text_is_none(self):
		try:
			Answer.create(question=self.question, text=None, is_right=False)
		except IntegrityError:
			assert True 
		else:
			assert False

	def test_is_right_default_position(self):
		assert not self.default_answer.is_right
