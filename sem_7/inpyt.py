
def import_data(data):
    with open('phone.csv', 'a+', encoding='utf-8') as file:
        sep = ','
        file.write(sep.join(data))
        file.write(f"\n")

