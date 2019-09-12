
def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (TypeError,ValueError):
        print("Некорректные исходные данные!")


print(discounted(100, 10.5))
print(discounted(100, 'price'))
print(discounted('100', 'price'))
# Почему boolen-аргументы не попадают в exception по TypeError?
print(discounted(True, False))
