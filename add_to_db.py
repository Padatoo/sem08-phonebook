# Сергей К
def add_to_txt(data):
    with open('phone_book.txt', 'a') as book:
        data_str = str.join(', ', data)
        book.write(data_str)

def add_to_csv(data):
    with open('phone_book.csv', 'a') as book:
        data_str = str.join(';', data)
        book.write(data_str)
