import requests
import csv

region_cod = str(input("Введіть код регіона: "))
list_region_cod_1 = ['01', '05', '07', 12, 14, 18, 21, 23, 26, 32, 35, 44]
list_region_cod_2 = [46, 48, 51, 53, 56, 59, 61, 63, 65, 68, 71, 73, 74, 80, 85]
find_region_1 = int(region_cod) in list_region_cod_1
find_region_2 = int(region_cod) in list_region_cod_2
if find_region_1 is False:
    if find_region_2 is False:
        print("Цей код регіона недоступний або його неіснує!")
        print("Введіть інший код!")
        exit(0)

r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc='+region_cod+'&exp=json')

print("Ректор, директор, виконуюча обов'язки директора, Президент, Начальник, В.о.ректора, В.о. директора")
value_name_post = str(input("Виберіть назву та впишіть сюди >: "))

universities: list = r.json()
filtered_data = [{k: row[k] for k in ['university_id', 'post_index']} for row in universities]
filtered_data_contact = [{k: row[k] for k in ['university_name', 'university_email', "university_phone",
                                              'university_director_post', 'university_director_fio']}
                         for k in ['university_director_post'] for row in universities if row[k] == value_name_post]

with open('universities_'+region_cod+'.csv', mode='w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

with open('contacts.csv', mode='w', encoding='UTF-8') as f_contacts:
    writer = csv.DictWriter(f_contacts, fieldnames=filtered_data_contact[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data_contact)
