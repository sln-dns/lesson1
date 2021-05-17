def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'
actual_price = format_price(56.24)
print(actual_price)