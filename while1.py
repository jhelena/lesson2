def ask_user():
    while True:
        user_say = input('Как дела?: ')
        if user_say.lower() == "хорошо":
            print('Ну и отлично!')
            break

ask_user()
   