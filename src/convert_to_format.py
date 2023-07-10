# from headhunter import HeadHunter
# from superjob import SuperJob

def convert_result(platform, res):
    if f"{platform}" == "headhunter.ru":
        return convert_hh(res)
    elif f"{platform}" == "superjob.ru":
        return convert_sj(res)

def convert_hh(res):
    vac = []
    for item in res['items']:
        vacancy = []
        vacancy.append(item.get("id", ""))
        vacancy.append(item.get("name", ""))
        if item.get("salary", "") is not None:
            vacancy.append(f'{item.get("salary", {}).get("from", "")} '
                               f'{item.get("salary", {}).get("currency", "")}')
        elif item.get("salary", "") is not None:
            if item.get("salary", {}).get("from") is None:
                vacancy.append(f'{item.get("salary", {}).get("to", "")} '
                                   f'{item.get("salary", {}).get("currency", "")}')
        else:
            vacancy.append("Не указана")
        vacancy.append(item.get("employer", {}).get("name", ""))
        if item.get("snippet", {}).get("responsibility", "") is not None:
            vacancy.append(f'{item.get("snippet", {}).get("responsibility", "")[0:50]}...')
        else:
            vacancy.append("Не указано")
        vacancy.append(item.get("alternate_url", ""))
        vacancy.append(item.get("area", {}).get("name", ""))

        vac.append(vacancy)
    return vac

def convert_sj():
    vac = []
    return vac