import pytest
from models import Theory
from peewee import *

class Test_ModelTheory:

	def setup_class(self):
		self.theory = Theory.create(text='That test text', theme='That test theme')

	def teardown_class(self):
		self.theory.delete_instance()

	def test_give_theme(self):
		assert self.theory.theme == 'That test theme'

	def test_give_text(self):
		assert self.theory.text == 'That test text'

	def test_theme_is_unique(self):
		try:
			Theory.create(text='That test text', theme='That test theme')
		except IntegrityError:
			assert True 
		else:
			assert False

	def test_values_is_null(self):
		try:
			self.theory = Theory.create(theme=None, text='text')
			self.theory = Theory.create(theme='theme', text=None)
		except IntegrityError:
			assert True 
		else:
			assert False
