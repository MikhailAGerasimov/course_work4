from abc import ABC, abstractmethod
import json


class VacanciesAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


    @abstractmethod
    def get_vacancies(self):
        """Подключение к API и получение вакансий"""
        pass



