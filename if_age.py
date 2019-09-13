age = int(input("Введите Ваш возраст: "))
def age_learn(age):
    if age < 7:
        return 'Вам пока только в детсад!'
    elif 7 <= age <= 17:
        return "Ваше место в школе!"
    elif 18 <= age <= 24:
        return "Вы можете учиться в ВУЗе!"
    else:
        return "Начните уже работать!"

res = age_learn(age)
print(res)