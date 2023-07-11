from src.convert_to_format import str_to_digit


class Vacancy:
    """
    Класс для работы с вакансиями.
    Атрибуты:
        - название вакансии;
        - зарплата;
        - работодатель;
        - краткое описание;
        - ссылка на вакансию;
        - регион.
    """
    def __init__(self, id: str, name: str, salary: str, company_name: str, description: str, link: str, region: str):
        self.id = self.validate_str(id, "id")
        self.name = self.validate_str(name, "title")
        self.salary = self.validate_str(salary, "salary")
        self.company_name = self.validate_str(company_name, "company_name")
        self.description = self.validate_str(description, "description")
        self.link = self.validate_str(link, "link")
        self.region = self.validate_str(region, "region")

    def __str__(self):
        # return (f"ID вакансии:{self.id}\nНазвание вакансии:{self.name}\nЗар. плата:{self.salary}"
        # f"\nНазвание компании:{self.company_name}\nОписание вакансии:{self.description}"
        # f"\nСсылка на вакансию: {self.link}\nМестонахождение: {self.region}")
        return (f"ID вакансии:{self.id}\nНазвание вакансии:{self.name}\nЗар. плата:{self.salary}")
    @staticmethod
    def validate_str(string_data, name_col):
        if isinstance(string_data, str):
            return string_data
        raise ValueError(f"Invalid {name_col}, {name_col} must be a string.")

    @staticmethod
    def validate_int_float(int_float, name_col):
        if isinstance(int_float, (int, float)):
            return int_float
        raise ValueError(f"Invalid {name_col}, {name_col} must be a number.")


    def __eq__(self, other):
        return str_to_digit(self.salary) == str_to_digit(other.salary)

    def __lt__(self, other):
        return str_to_digit(self.salary) < str_to_digit(other.salary)

    def __gt__(self, other):
        return str_to_digit(self.salary) > str_to_digit(other.salary)