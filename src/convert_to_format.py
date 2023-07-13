# from headhunter import HeadHunter
# from superjob import SuperJob

def convert_result(platform, res):
    '''
    Данные с платформ конвертируются в едный формат данных
    :param platform:
    :param res:
    :return:
    '''
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
        else:
            vacancy.append("0")
        vacancy.append(item.get("employer", {}).get("name", ""))
        if item.get("snippet", {}).get("responsibility", "") is not None:
            vacancy.append(item.get("snippet", {}).get("responsibility", ""))
        else:
            vacancy.append("0")
        vacancy.append(item.get("alternate_url", ""))
        vacancy.append(item.get("area", {}).get("name", ""))
        vac.append(vacancy)
    return vac

def convert_sj(res):
    vac = []
    for item in res["objects"]:
        vacancy = []
        vacancy.append(str(item.get("id", "")))
        vacancy.append(item.get("profession", "")[:100])
        if item.get("payment_from", "") is not None:
            vacancy.append(f'{item.get("payment_from", "")} {item.get("currency", "")}')
        else:
            vacancy.append("0")
        vacancy.append(item.get("firm_name", ""))
        vacancy.append(item.get('candidat', ''))
        vacancy.append(item.get("link", ""))
        vacancy.append(item.get("town", {}).get("title", ""))
        vac.append(vacancy)
    return vac

def str_to_digit(input_str):
    return int(input_str.split(" ")[0])