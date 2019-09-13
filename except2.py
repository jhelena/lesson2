
def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            print('Слишком большая скидка!')
            raise ValueError
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (TypeError,ValueError):
        print("Некорректные исходные данные!")
        return price


print(discounted(100, 10.5))
print(discounted(100, 'price','price'))
print(discounted('100', 'price'))
# Почему boolen-аргументы не попадают в exception по TypeError?
print(discounted(True, False))
print(discounted(10, 5, 1000))
