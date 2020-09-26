from bd.models.models import Theory, ReadedTheory


class TheoryApi:
	def give_theory_by_id(theory_id):
		return Theory.get(Theory.index==theory_id)

	def give_theories_that_user_has_read(user_model):
		query = ReadedTheory.select().where(ReadedTheory.user==user_model)
		list_theories_from_model = list()
		for readed_theory in query:
			list_theories_from_model.append(readed_theory.theory)
		return list_theories_from_model

	def give_theories_that_user_has_not_read(self, user_model):
		query_readed_theories = ReadedTheory.select().where(ReadedTheory.user==user_model)
		readed_theories = list()
		for readed_theory in query_readed_theories:
			readed_theories.append(readed_theory.theory)
		query_all_theories = Theory.select()
		all_theories = set(list(query_all_theories))
		readed_theories = set(readed_theories)
		return list(all_theories - readed_theories)

	def give_all_theories():
		query = Theory.select()
		list_theories_from_model = list(query)
		return list_theories_from_model
