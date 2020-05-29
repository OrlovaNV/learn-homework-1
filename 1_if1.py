
def employment(age):
    if 0 <= age <= 6:
        return "Вы учитесь в детском саду?"
    elif 7 <= age <= 17:
        return "Вы учитесь в школе?"
    elif 18 <= age <= 22:
        return "Вы учитесь в ВУЗе?"
    else:
        return "Вы работаете?"

def main():
    a = input("Введите ваш возраст:")
    age = int(a) 
    print(employment(age))

if __name__ == "__main__":
    main()