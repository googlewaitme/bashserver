import pytest
from models.models import User
from peewee import *

class Test_ModelUser:

	def setup_class(self):
		self.user = User.create(user_id='vk_1234')

	def teardown_class(self):
		self.user.delete_instance()

	def test_user_id(self):
		assert self.user.user_id == 'vk_1234'

	def test_user_id_is_not_unique(self):
		try:
			self.user = User.create(user_id='vk_1234')
		except IntegrityError:
			assert True 
		else:
			assert False

	def test_user_id_is_null(self):
		try:
			self.user = User.create(user_id=None)
		except IntegrityError:
			assert True 
		else:
			assert False
