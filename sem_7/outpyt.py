
def export_data(str_search):
    with open('phone.csv', 'r', encoding='utf-8') as file:
        data = []
        for item in file:
            if str_search in item:
                data.append(item)
    return data