# -*- coding: utf8 -*-
# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

# решение преподавателя


import json
companies = {}
pos_count, pos_sum = 0, 0
with open('HW57.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        companies.update({data[0]: profit})
        if profit > 0:
            pos_count += 1
            pos_sum += profit
average_profit = pos_sum / pos_count
result = [companies, {'average_profit': average_profit}]

with open('result7.json', 'w') as file:
    json.dump(result,file)
# import json
# profit = {}
# profit2 = {}
# profit3 = 0
# prof_aver = 0
# i = 0
# with open('HW57.txt', 'r') as file:
#     for line in file:
#         name, firm, earning, damage = line.split()
#         profit[name] = int(earning) - int(damage)
#         if profit.setdefault(name) >= 0:
#             prof = profit3 + profit.setdefault(name)
#             i += 1
#     if i != 0:
#         prof_aver = profit3 / i
#         print(f'Прибыль средняя - {prof_aver:.2f}')
#     else:
#         print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
#     pr = {'средняя прибыль': round(prof_aver)}
#     profit.update(profit2)
#     print(f'Прибыль каждой компании - {profit}')
#
# with open('file_7.json', 'w') as write_js:
#     json.dump(profit, write_js)
#
#     js_str = json.dumps(profit)
#     print(f'Создан файл с расширением json со следующим содержимым: \n '
#           f' {js_str}')