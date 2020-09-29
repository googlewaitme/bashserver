import json

def make_json(dictionary):
	return json.dumps(dictionary)

def theory_to_dict(model):
	answer = {
		'theme': model.theme,
		'id': model.index,
		'text': model.text
	}
	return answer

def question_to_dict(model):
	answer = {
		'text': model.text,
		'id': model.index
	}
	return answer

def answer_to_dict(model):
	answer = {
		'text': model.text
	}
	return answer

def answers_to_list(answers):
	answer = [model.text for model in answers]
	return answer 


JSON_TRUE = make_json({'boolean': True})
JSON_FALSE = make_json({'boolean': False})
