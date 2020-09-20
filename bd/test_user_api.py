import pytest
import user_api
from user_api import UserApi
from models.models import User, Theory, Question, PassingQuestion, ReadedTheory


class Test_UserApi:
	def setup_class(self):
		self.fake_user_id = 'vk_1234'
		self.true_user_id = 'vk_00'
		self.user = User.create(user_id=self.true_user_id)

		self.theory = Theory.create(theme='test theme', text='test text')
		self.question = Question.create(text='Is it test???', theory=self.theory)

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


	def test_starting_add_readed_theory(self):
		try:
			self.true_user.add_readed_theory(self.theory)
		except Exception as e:
			assert False, f'{e}'
		else:
			self.delete_this_readed_theory()

	def test_add_readed_theory(self):
		list_of_theories = self.give_list_readed_theory()
		len_prefer_add_theory = len(list_of_theories)
		self.true_user.add_readed_theory(self.theory)
		list_of_theories = self.give_list_readed_theory()
		len_after_add_theory = len(list_of_theories)

		assert len_after_add_theory - len_prefer_add_theory == 1

		self.delete_this_readed_theory()

	def give_list_readed_theory(self):
		query = ReadedTheory.select().where(ReadedTheory.user==self.true_user.give_user())
		list_of_theories = list(query)
		return list_of_theories

	def delete_this_readed_theory(self):
		list_of_theories = self.give_list_readed_theory()
		for theory in list_of_theories:
			theory.delete_instance()

	
	def test_starting_add_passed_question(self):
		try:
			self.true_user.add_passed_question(self.question)
		except Exception as e:
			assert False, f'{e}'
		else:
			self.delete_this_passed_questions()

	def test_add_passed_question(self):
		list_of_questions = self.give_list_passed_questions()
		len_prefer_add_question = len(list_of_questions)
		self.true_user.add_passed_question(self.question)
		list_of_questions = self.give_list_passed_questions()
		len_after_add_question = len(list_of_questions)

		assert len_after_add_question - len_prefer_add_question == 1

		self.delete_this_passed_questions()

	def give_list_passed_questions(self):
		query = PassingQuestion.select().where(PassingQuestion.user==self.true_user.give_user())
		list_of_questions = list(query)
		return list_of_questions

	def delete_this_passed_questions(self):
		list_of_questions = self.give_list_passed_questions()
		for question in list_of_questions:
			question.delete_instance()

