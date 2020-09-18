import pytest
from models import ReadedTheory, Theory, User
from peewee import *


class Test_ModelReadedTheory:
	def setup_class(self):
		self.user = User.create(user_id='id_1234')
		self.theory = Theory.create(text='lala', theme='lala')
		self.readed_theory = ReadedTheory(user=self.user, theory=self.theory)

	def teardown_class(self):
		self.theory.delete_instance()
		self.user.delete_instance()
		self.readed_theory.delete_instance()
	# TODO me
