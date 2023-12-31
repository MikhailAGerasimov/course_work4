from src.abs.vac_api import VacanciesAPI
from requests import *
import json


class SuperJob(VacanciesAPI):

    """Класс, наследующийся от абстрактного класса,
    для работы с платформой SuperJob,
    и класса, для работы с файлом, содержащем вакансии superjob.ru"""

    __API_KEY = "v3.r.127253021.e26c9a2e287fcc53ee2e9b7707c48cbca371f507.9d915df4e26d27b87fa2066897b5442326417a2e"
    _api_link = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self):
        pass

    def __str__(self):
        return "superjob.ru"

    def get_vacancies(self, **kwargs):
        """
        :param kwargs:
        text - Поисковый запрос
        count - Количество вакансий для вывода
        """
        params = {}
        headers = {
            'X-Api-App-Id': self.__API_KEY
        }

        for key, value in kwargs.items():
            params[key] = value

        response = get(self._api_link, headers=headers, params=params)
        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print("Ошибка при выполнении запроса.")
            return []

    def get_search_vacancies(self, search_data, n=10):
        return self.get_vacancies(keyword=search_data, count=n)

    def get_region_vacancies(self, region, n=10):
        return self.get_vacancies(town=region, count=n)
