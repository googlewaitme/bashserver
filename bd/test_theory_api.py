import pytest
from theory_api import TheoryApi
from user_api import UserApi
from models.models import Theory, ReadedTheory

class Test_TheoryApi:

	def setup_class(self):
		self.theory_api = TheoryApi

		self.list_theories = []
		for i in range(10):
			theory = Theory.create(theme=f'test_theory_api{i}', text='test_theory_api')
			self.list_theories.append(theory)
		self.user = UserApi(user_id='vk_00')
		self.user.add()
		for i in range(5):
			self.user.add_readed_theory(self.list_theories[i])

	def teardown_class(self):
		self.user.remove()
		for theory in self.list_theories:
			theory.delete_instance()

	def test_give_theory_by_id(self):
		for theory in self.list_theories:
			theory_from_api = self.theory_api.give_theory_by_id(theory_id=theory.index)
			assert theory_from_api == theory

	def test_give_list_theories(self):
		list_from_api = self.theory_api.give_all_theories()
		set_from_api = set(list_from_api)
		set_from_test = set(self.list_theories)
		assert set_from_test.issubset(set_from_api)

	def test_give_user_readed_theories(self):
		list_from_api = self.theory_api.give_theories_that_user_has_read(user_model=self.user.give_user())
		list_from_test = self.list_theories[:5]	
		assert list_from_api == list_from_test

	def test_give_user_not_readed_theories(self):
		from_api = self.theory_api.give_theories_that_user_has_not_read(user_model=self.user.give_user())
		from_api = set(from_api)
		from_test = self.list_theories[5:]
		from_test = set(from_test)
		assert  from_test == from_api
		
	def test_give_user_readed_and_not_readed_theories_have_not_intersection(self):
		list_readed = self.theory_api.give_theories_that_user_has_read(user_model=self.user.give_user())
		list_not_readed = self.theory_api.give_theories_that_user_has_not_read(user_model=self.user.give_user())
		set_readed = set(list_readed)
		set_not_readed = set(list_not_readed)
		set_intersection = set_readed.intersection(set_not_readed)
		assert len(set_intersection) == 0
