from itertools import zip_longest
import json, show_sale, add_sale

# Для третьего и шестого заданий


# Задание 1
with open('nginx_logs.txt') as x:
    data = []
    for line in x:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(data)

# Задание 3
dict_to_out = {}
with open('users.csv', encoding='utf-8') as users, open('hobby.csv', encoding='utf-8') as hobby:
    count_line_users = sum(1 for line in users)
    count_line_hobby = sum(1 for line in hobby)
    if count_line_users < count_line_hobby:
        exit(1)
    users.seek(0)
    hobby.seek(0)
    for users_line, line_hobby in zip_longest(users, hobby):
        dict_to_out[users_line.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby
with open('task_3.json', 'w', encoding='utf-8') as z:
    json.dump(dict_to_out, z, ensure_ascii=False)
print(dict_to_out)

# Задание 6 (show_sale.py и add_sale.py к этому заданию)
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# python show_sales.py 1 3
# python show_sales.py 3


