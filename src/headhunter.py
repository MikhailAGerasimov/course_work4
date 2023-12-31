from src.abs.vac_api import VacanciesAPI

from requests import *
import json

class HeadHunter(VacanciesAPI):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой HeadHunter,
    и класса, для работы с файлом, содержащем вакансии hh.ru"""

    _api_link = "https://api.hh.ru/vacancies"

    def __init__(self):
        pass

    def __str__(self):
        return "headhunter.ru"

    def get_vacancies(self, **kwargs):
        """
        :param kwargs:
        text - Поисковый запрос
        per_page - Количество вакансий на странице
        """

        params = {}
        for key, value in kwargs.items():
            params[key] = value
        response = get(self._api_link, params=params)

        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None

    def get_search_vacancies(self, search_data, n=10):
        return self.get_vacancies(text=search_data, per_page=n)

    def get_region_vacancies(self, region):

        return self.get_vacancies(city = region)