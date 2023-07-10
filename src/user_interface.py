from src.headhunter import HeadHunter
from src.superjob import SuperJob
from src.vacancy import Vacancy
from src.prints import print_user_1, print_user_2, print_user_3
from src.convert_to_format import convert_result

def user_interface():
    '''Функция для взаимодействия с пользователем'''
    hh = HeadHunter()
    sj = SuperJob()
    platforms = [hh,sj]
    flag = True

    print_user_1()
    while flag:
        print_user_2()
        user_input = input()
        if user_input in  ['1','2']:
            platform = platforms[int(user_input) - 1]
            print(f"Выбран сайт {platform}\n")

            while True:
                print_user_3()
                user_input_oper = input()
                if user_input_oper == '1':
                    search_text = input("Введите запрос:")
                    result = platform.get_vacancies(text=search_text)
                    vac_list=[]
                    print(convert_result(platform, result))
                break

        elif user_input == "0":
            flag = False
            print("До свидания!")

        else:
            print("Платформа выбрана неверно!")
