def ask_user():
    while True:
        try:
            user_say = input('Как дела?: ')
            if user_say.lower() == "хорошо":
                print('Ну и отлично!')
                break
        except KeyboardInterrupt:
            print('\n Пока!')
            break
ask_user()
