# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения
# на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
class Numbers:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                meaning = int(input('write a number and push Enter'))
                self.my_list.append(meaning)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"wrong input: it has to be number")
                yes_no = input(f'try again')
                if yes_no == 'Yes' or yes_no == 'yes':
                    print(try_except.my_input())
                elif yes_no == 'No' or yes_no == 'no':
                    return f'end'
                else:
                    return f'end'
try_except = Numbers(1)
print(try_except.my_input())

# list = [1, 3, 4, 56]
# list2 = [1, 3, 'cat', 4, 56]

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.

# Подсказка: для данного задания примем, что пользователь может вводить
# только числа и строки. При вводе пользователем очередного элемента необходимо
# реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.