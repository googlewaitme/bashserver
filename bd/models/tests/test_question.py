import pytest
from models.models import Question, Theory
from peewee import *


class Test_ModelQuestion:
	def setup_class(self):
		self.theory = Theory(theme='test text', text='test text')
		self.question = Question(theory=self.theory, text='That is text')

	def teardown_class(self):
		self.theory.delete_instance()
		self.question.delete_instance()
	
	def test_theory_in_question_is_theory(self):
		assert self.theory is self.question.theory
	
	def test_question_text(self):
		assert self.question.text == 'That is text'

	def test_question_text_not_null(self):
		try:
			Question.create(theory=self.theory, text=None)
		except IntegrityError:
			assert True
		else:
			assert False