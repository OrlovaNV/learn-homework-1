"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    try:
      while True:
        ask_user = input('Как дела? ')
        if ask_user == 'Хорошо':
          print('Чудненько!')
          break
        else: 
          print('А подробнее?')
    except KeyboardInterrupt:
      print('Пока!')
    
if __name__ == "__main__":
    ask_user()
