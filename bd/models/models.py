from peewee import *


database = SqliteDatabase('bash.db')


def create_tables():
	with database:
		database.create_tables([User, Theory, ReadedTheory, Question])


class BaseModel(Model):
	class Meta:
		database = database


class User(BaseModel):
	user_id = CharField(null=False, unique=True, verbose_name='User id on this server')


class Theory(BaseModel):
	theme = TextField(unique=True, null=False)
	text = TextField(null=False)
	index = AutoField()


class ReadedTheory(BaseModel):
	user = ForeignKeyField(User)
	theory = ForeignKeyField(Theory)


class Question(BaseModel):
	theory = ForeignKeyField(Theory)
	text = TextField(null=False, unique=True)
	index = AutoField()


class Answer(BaseModel):
	question = ForeignKeyField(Question)
	text = TextField(null=False, unique=True)
	index = AutoField()
	is_right = BooleanField(default=False)	


class PassingQuestion(BaseModel):
	question = ForeignKeyField(Question)
	user = ForeignKeyField(User)
	is_right = BooleanField(default=False)
