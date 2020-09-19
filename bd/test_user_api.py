import pytest
import user_api
from user_api import UserApi
from models.models import User, Theory, Question, ReadedTheory, PassingQuestion


class Test_UserApi:
	def setup_class(self):
		self.fake_user_id = 'vk_1234'
		self.true_user_id = 'vk_00'
		self.user = User.create(user_id=self.true_user_id)

		self.theory = Theory(theme='test theme', text='test text')
		self.question = Question(text='Is it test???', theory=self.theory)

		self.fake_user = UserApi(self.fake_user_id)
		self.true_user = UserApi(self.true_user_id)

	def teardown_class(self):
		self.theory.delete_instance()
		self.question.delete_instance()
		self.user.delete_instance()

	def test_user_is_not_consist(self):
		assert self.fake_user.is_exist() == False

	def test_user_is_consist(self):
		assert self.true_user.is_exist() == True

	def test_add_user(self):
		self.fake_user.add()
		assert self.fake_user.is_exist()
		self.fake_user.remove()


	def test_remove_user(self):
		self.true_user.remove()
		assert not self.true_user.is_exist()
		self.true_user.add()

	def test_give_user_id(self):
		assert self.true_user.give_id() == self.true_user_id
		assert self.fake_user.give_id() == self.fake_user_id

	def test_add_readed_theory(self):
		try:
			self.true_user.add_readed_theory(self.theory)
		except Exception as e:
			assert False, f'{e}'
		else:
			self.delete_this_readed_theory()

	def delete_this_readed_theory(self):
		query = ReadedTheory.select().where(ReadedTheory.user==self.true_user.give_user())
		list_of_theories = list(query)
		for theory in list_of_theories:
			theory.delete_instance()

	def test_add_passed_question(self):
		try:
			self.true_user.add_passed_question(self.question)
		except Exception as e:
			assert False, f'{e}'
		else:
			self.delete_this_passed_questions()

	def delete_this_passed_questions(self):
		query = PassingQuestion.select().where(PassingQuestion.user==self.true_user.give_user())
		list_of_questions = list(query)
		for question in list_of_questions:
			question.delete_instance()

