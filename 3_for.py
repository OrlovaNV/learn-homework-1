school_scores = [{'school_class': '4', 'scores': [3,4,4,5,2]}, {'school_class': '3', 'scores': [3,5,4,5,3]}, 
{'school_class': '2', 'scores': [4,5,4,5,3]}, 
{'school_class': '1', 'scores': [4,5,4,5,5]}
]
"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sum_school = 0
    value_school = 0
    for i in range(len(school_scores)):
        sum_class = 0
        
        for score in school_scores[i]['scores']:
            sum_class += score
        average_value = sum_class/len(school_scores[i]['scores'])
        class_number = school_scores[i]['school_class']
        print(f'Средний балл {class_number} класса: {average_value}')
            
        sum_school += sum_class
        value_school += len(school_scores[i]['scores'])
            
    average_value_school  =  sum_school/value_school
    print(f'Средняя оценка по школе: {average_value_school}')


if __name__ == "__main__":
    main()
