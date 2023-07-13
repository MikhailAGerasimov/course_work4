import json
import os
from src.abs.vac_to_file import VacFile
from src.vacancy import Vacancy


class VacFileJSON(VacFile):
    def __init__(self, filename):
        self.filename = filename

        folder_path = os.path.abspath("data")
        self.file_path = os.path.join(folder_path, filename)

    def add_vacancy(self, vacancy_data):
        data = {}
        data['items'] = []
        for item in vacancy_data:
            data['items'].append({
                'id':item.id,
                'title':item.name,
                'salary':item.salary,
                'company_name':item.company_name,
                'description':item.description,
                'link':item.link,
                'region':item.region
            })
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False,indent=4)
        return self.file_path

    def get_vacancies(self):

        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data = data['items']
        vac_list = []
        for item in data:
            vacancy = Vacancy(item['id'], item['title'], item['salary'], item['company_name'], item['description'], item['link'], item['region'])
            vac_list.append(vacancy)
        return vac_list

    def remove_vacancy(self, vacancy_id):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data = data['items']
        for item in data:
            if item['id'] == vacancy_id:
                data.remove(item)
        data_json = {}
        data_json['items'] = data
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data_json, file, ensure_ascii=False,indent=4)
