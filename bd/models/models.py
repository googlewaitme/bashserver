from peewee import *


database = SqliteDatabase('bash.db')


def create_tables():
    with database:
        database.create_tables([User, Theory])


class BaseModel(Model):
	class Meta:
		database = database


class User(BaseModel):
	user_id = CharField(null=False, unique=True, verbose_name='User id on this server')


class Theory(BaseModel):
	theme = TextField(unique=True, null=False)
	text = TextField(null=False)
	theory_id = IntegerField(primary_key=True)


class ReadedTheory(BaseModel):
	user = ForeignKeyField(User)
	theory = ForeignKeyField(Theory)
