#Импортируем библиотеку json
import json

#Файл про звёзды
file = 'stars.json'

#Проверка существования файла с дальнейшим его созданием в случае отсутствия
try:
    with open(file, 'r') as f:
        stars = json.load(f)
except FileNotFoundError:
    #Создаём список с данными о звёздах
    data_about_stars_1 = [
        {"id": 1, "name": "Сириус", "constellation": "Большой Пёс", "is_visible": True, "radius": 1.71},
        {"id": 2, "name": "Канопус", "constellation": "Корма", "is_visible": True, "radius": 0.73},
        {"id": 3, "name": "Арктур", "constellation": "Богатырь", "is_visible": True, "radius": 1.5},
        {"id": 4, "name": "Вега", "constellation": "Лира", "is_visible": True, "radius": 2.13},
        {"id": 5, "name": "Полиус", "constellation": "Центавр", "is_visible": False, "radius": 1.3}
    ]
    stars = data_about_stars_1
    with open(file, 'w') as f:
        json.dump(stars, f)

#Создаём переменную для подсчёта кол-ва операций о записи звёзд
count_of_operations = 0

#Создаём бесконечный цикл, который будет работать до того момента, пока пользователь не захочет выйти
while True:
    #Сценарии действий
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")

    #выбор действия
    user_choice = input("Выберите пункт меню: ")
    
    #Если 1
    if user_choice == '1':
        #Открываем json файл
        with open(file, 'r') as f:
            #Загружаем данные
            stars = json.load(f)
            print("\nВсе записи:")
            for star in stars:
                print(json.dumps(star, ensure_ascii = False, indent = 4))
        
        count_of_operations += 1

    #Если 2
    elif user_choice == '2':
        try:
            #Ввод ID 
            ID = int(input("Введите ID записи для поиска: "))
        #Открываем json файл
            with open(file, 'r') as f:
                found = False
                #Перебор ID
                for index, star in enumerate(stars):
                    #Если нашли
                    if star['id'] == ID:
                        print(f"\nЗапись найдена (позиция {index + 1}):")
                        print(json.dumps(star, ensure_ascii = False, indent = 4))
                        found = True
                        break
            #Если found = false
            if not found:
                print("Запись не найдена.")
            #Счётчик операций увеличивается на 1
            count_of_operations += 1
        except ValueError:
            print("Пожалуйста, введите корректный числовой ID.")

    #Если 3
    elif user_choice == '3':
        #Создание словаря
        new_star = {
            #Ввод данных
            'id': len(stars) + 1,
            'name': input("Введите имя звезды: "),
            'constellation': input("Введите созвездие: "),
            'is_visible': input("Является ли звезда видимой (True/False): ") == 'True',
            'radius': float(input("Введите радиус звезды: "))
        }
        #Добавляем звезду в список
        stars.append(new_star)
        #Открываем json файл
        with open(file, 'w') as f:
            json.dump(stars, f)
        #Счётчик операций увеличивается на 1
        count_of_operations += 1
        print("Запись успешно добавлена.")

    #Если 4
    elif user_choice == '4':
        try:
            #ВВод ID для удаления
            ID_to_delete = int(input("Введите ID записи для удаления: "))
            stars = [star for star in stars if star['id'] != ID_to_delete]
            #Открываем json файл
            with open(file, 'w') as f:
                json.dump(stars, f)
            #Счётчик операций увеличивается на 1
            count_of_operations += 1
            print("Запись успешно удалена.")
        except ValueError:
            print("Пожалуйста, введите корректный числовой ID.")

    #Если 5
    elif user_choice == '5':
        #вывод
        print(f"Количество выполненных операций: {count_of_operations}")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 5.")