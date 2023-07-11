from src.headhunter import HeadHunter
from src.superjob import SuperJob
from src.vacancy import Vacancy
from src.prints import print_user_1, print_user_2, print_user_3
from src.convert_to_format import convert_result
from src.sorting import selection_sort

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
                    result = platform.get_search_vacancies(search_text)
                    vac_list=[]
                    temp_list = convert_result(platform, result)
                    for item in temp_list:
                        vacancy = Vacancy(item[0],item[1], item[2], item[3], item[4], item[5], item[6])
                        print(30*'-')
                        print(vacancy)
                        vac_list.append(vacancy)
                    input("Нажмите ENTER, чтобы продолжить!")
                    break
                elif user_input_oper == '2':
                    search_text = input("Введите запрос:")
                    vac_num = int(input("Сколько получить вакансий по зарплате (0-99)? "))
                    result = platform.get_search_vacancies(search_text, vac_num)
                    #platform.printj(result)
                    vac_list=[]
                    temp_list = convert_result(platform, result)
                    for item in temp_list:
                        vacancy = Vacancy(item[0],item[1], item[2], item[3], item[4], item[5], item[6])
                        # print(30*'-')
                        # print(vacancy)
                        vac_list.append(vacancy)
                    sorted_list = selection_sort(vac_list)
                    for item in sorted_list:
                        print(30*'-')
                        print(item)

                    input("Нажмите ENTER, чтобы продолжить!")
                    break




        elif user_input == "0":
            flag = False
            print("До свидания!")

        else:
            print("Платформа выбрана неверно!")
