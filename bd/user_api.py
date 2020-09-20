from models.models import User, PassingQuestion, ReadedTheory


class UserApi:

	def __init__(self, user_id):
		self._user_id = user_id
	
	def is_exist(self):
		users_query = User.select().where(User.user_id==self._user_id)
		users_list = list(users_query)
		count_users_with_need_id = len(users_list)
		assert count_users_with_need_id <= 1, f"Users {self._user_id} more than 1 in bd"
		return count_users_with_need_id > 0

	def give_user(self):
		user = User.get(User.user_id==self._user_id)
		return user

	def give_id(self):
		return self._user_id

	def remove(self):
		assert self.is_exist()
		user = self.give_user()
		user.delete_instance()
	
	def add(self):
		assert not self.is_exist()
		User.create(user_id=self._user_id)

	def add_readed_theory(self, theory):
		ReadedTheory.create(user=self.give_user(), theory=theory)

	def add_passed_question(self, question):
		PassingQuestion.create(user=self.give_user(), question=question)
