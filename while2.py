answ={
    "Как дела?":"Хорошо!",
    "Что делаешь?":"Программирую",
    "Какая погода сегодня?":"Теплая"}

def ask_user(answer_dictionary):
    while True:
        user_say = input('Ваш вопрос: ')

        for key in answer_dictionary.keys():
            if user_say == key:
                print(answer_dictionary[key]) 

ask_user(answ)
  