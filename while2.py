answ={
    "Как дела?":"Хорошо!",
    "Что делаешь?":"Программирую",
    "Какая погода сегодня?":"Теплая"}

def ask_user(answer_dictionary):
    while True:
        user_say = input('Ваш вопрос: ')
        print(answer_dictionary.get(user_say, 'Я не знаю ответа'))

ask_user(answ)
  