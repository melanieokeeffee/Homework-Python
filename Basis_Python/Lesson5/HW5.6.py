# -*- coding: utf8 -*-
# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не
# обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# решение преподавателя
result = {}
with open('HW56.2.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        hours = 0
        for elem in data[1:]:
            if elem != '-':
                num = '0'
                for i in elem:
                    if i.isdigit():
                        num +=i
                    else:
                        break
                hours += int(num)
        result.update({data[0].strip(':'):hours})



# #import json
# subj = {}
# with open('HW56.txt', 'r') as file:
#     for line in file:
#         subject, lecture, practice, lab = line.split()
#         subj[subject] = int(lecture) + int(practice) + int(lab)
#     print(f'Общее количество часов по предмету - \n {subj}')