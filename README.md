### bashserver
Это код сервера, который обрабатывает все апи запросы и отвечает на них.
## Методы апи
user_id - во всех методах является каким-либо уникальным айди пользователя для клиента. 

# /add_user/<user_id>/
Создает нового пользователя на сервере
Параметры
  user_id 
Возвращает 
  json, в формате
{
  'boolean': true 
}
где boolean это логическая переменная, которая означает успешность добавления пользователя


# /user_is_exist/<user_id>/
Проверяет существование пользователя на сервере 
Параметры
  user_id
Возвращает
  json в формате
  {
    'boolean': True
  }
  boolean - логическая переменная, которая означает существование пользователя на сервере

# /remove_user/<user_id>/
Удаляет пользователя из базы данных на сервере
Параметры
  user_id
Возвращает
  json в формате
  {
    'boolean': True
  }
  boolean - логическая переменная, которая означает успешность удаления пользователя на сервере

# /give_theory/<user_id>/
Возвращает следующую теорию из ветки теорий для пользователя
Параметры 
  user_id
Возвращает 
  theme - тема новой теории
  text - основной материал новой темы
  id - айдишник теории в базе данных. Нужен для того, чтобы отметить позже, что пользователь изучил эту теорию.
  json в формате
  {
    'theme': 'That first theme',
    'text': 'Let's talk about me, only me... and me',
    'id': 123
  }

# /set_user_read_theory/<user_id>/<theory_id>/
Отмечает в базе данных, что пользователь изучил теорию
Параметры 
  user_id 
  theory_id - Айди теории, который мы получаем вызвав метод /give_theory/
Возвращает 
  json в формате
  {
    'boolean': True
  }
  boolean - логическая переменная, которая означает успешность отмечения прочитанности

# /give_question/<user_id>/
Возвращает следующий вопрос, для закрепления материалов уже изученных тем
Параметры
  user_id
Возвращает
  text - Это текст самого вопроса
  id - уникальный айди вопроса в базе данных. Нужен для проверки ответа пользователей
  answers - список, возможных ответов. Если список пустой, значит возможных ответов нет, и человеку нужно ввести ответ самостоятельно.
  json в формате 
  {
    'text': "Это текст вопроса???",
    'id': 123,
    'answers': [
      "Да",
      "Кажется, нет",
      "Кажется, да",
      "Нет"
    ]
  }

# /check_user_answer/<user_id>/<question_id>/<user_answer>/
Проверяет ответ пользователя на вопрос.
Параметры:
  user_id 
  question_id - Айди вопроса, который мы получаем из метода give_question
  user_answer - Текст, который ввел пользователь
Возвращает 
  user_answer_is_right - логическая переменная, правильно ли ответил пользователь или нет
  right_answer - строка, в которой записан правильный ответ, для того чтобы отобразить пользователю.
  {
		'user_answer_is_right': True/False,
		'right_answer': 'Правильный ответ'
	}	
