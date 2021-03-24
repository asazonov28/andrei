# LIST - список
# empty_list = []
# print(type(empty_list))
#
# word = 'word'
#
# some_list = [123, 0.323, 'Hello', 'Hello', word, True, [1, 23, 0.434], None]
# print(len(some_list))
# print(some_list[::-1])
#
# print(some_list[2])
# print(some_list)
# some_list[2] = 'Planet'
# print(some_list)
# some_list[8] = 123123
# print(some_list)

# courses = ['History', 'Programming', 'Math', 'Literature', 'Physics']
# #
# # print(len(courses))
# # courses.append('Art') #метод добавления
# # print(courses[5])
# # courses.insert(1, 'English') #метод добавления на опред. позицию
# # print(courses)
#
# # courses = ['History', 'Programming', 'Match', 'Literature', 'Physics']
# # courses = ['Art', 'English']
# # print(courses)
# # print(courses[2][1])
#
# # courses2 = ['Art', 'English']
# # courses.extend(courses2) #метод расширения
# # print(courses)
#
# # courses.remove('Math')  #удаление элемента
# # print(courses)
#
# # deleted = courses.pop(2) #удаление элемента с сохранением
# # print(courses)
# # print(deleted)
#
# # print(courses)
# # courses.reverse() #выводит в обратном порядке
# # print(courses)
#
# # print(list(reversed(courses)))
# # print(courses)
# # print(courses[::-1])
# # print(courses)
#
# numbers = [1, 2, 5, 8, 4, 6]
# # courses.sort()
# # print(courses)
# #
# # numbers.sort() #сортировка
# # print(numbers)
#
# # courses.sort(reverse=True)
# # print(courses)
# #
# # numbers.sort(reverse=True)
# # print(numbers)
#
# # print(sorted(courses))
# # print(courses)
# random_list = [1, 2], [3, 4, 5], [6, 7, 8, 9]
# print(sum(numbers)) #сумма числовых списков
# print(min(courses))
# print(max(courses))

# print(min(random_list))
# print(max(random_list))

# print(courses.index('Math'))
# print(courses[courses.index('Math')])
# if 'Math' in courses:
# courses_str = str(courses) #список конвертируется в строку
# print(str(courses))
# courses_str = ', '.join(courses)
# print(courses_str)
# # separator = '*****'
# courses_str = separator.join(courses)
# print(courses_str)
#
# new_list = courses_str.split(', ')
# print(new_list)
# print(len(new_list))

# print(courses + numbers)

# courses2 = courses.copy()
# print(courses)
# print(courses2)
#
# courses[0] = 'Sports'
# courses2[1] = 'Art'
#
# print(courses)
# print(courses2)

# print(numbers.count(6)) #считает повторные элементы
#
# numbers.clear()
# print(numbers)

# TUPLE - кортеж

# empty_tuple = ()
# print(empty_tuple)

# courses = ('History', 'Programming', 'Math', 'Literature', 'Physics')
# courses2 = ('Art', 'English')
# courses.count('History')

# new_courses = courses + courses2
# print(new_courses)
#
# courses_tuple = (1, 2, 'Jungle')
# print(courses_tuple)
#
# courses = list(courses_tuple)
# courses[0] = 'Art'
# print(courses_tuple)

# empty_list = ['Art']
# print(type(empty_list))
#
# empty_tuple = (1234,) # создание кортежа с одним элементом требует запятой
# print(empty_tuple)

# SET

# courses = {'History', 'Programming', 'Math', 'Literature', 'Physics'}
# empty_set = {}
# print(type(empty_set))

# courses2 = {'Art', 'English', 'Design', 'Physics', 'History'}
# print(courses2.intersection(courses)) # элементы пересекаются
# print(courses2.difference(courses)) # выделяет особенности

# print(courses2.union(courses)) # объединяет

# print(courses.issuperset(courses2)) # являются частью или нет
# print(courses.issubset(courses))

# DICTIONARY - словарь

some_dict = {'name': 'John'}

# x = 5
# student = {'name': 'John', 'age': 32, 'courses': ['Math', 'Art', 'Programming'],
#            1: 'int key', 0.2: 'float key', x: 'variable', 'var key': x, True: 'Hello'}
# some_set = {'Art', 'Math'}
# print(student['age'])
# print(some_set)
# print(student['courses'][1])
# print(student[x])
# print(student[True])
# print(student.get('courses'))  # проверка
#
# print(student.get('job', 'Not Found'))
# print(student.get('Math', 'Not Found'))

# student['name'] = 'Mary'
# student['phone'] = '555 168 55'
# print(student)

# new_data = {'name': 'Mary', 'age': 27, 'phone': '556-377-25'}

# student.update(new_data) # метод замены данных в словаре
# print(student)

# del student ['age']
# print(student)
#
# deleted = student.pop('name')
# print(deleted)

# print(student.keys())
# print(type(student.keys())) # выводит все ключи

# print(list(student.keys())) # конвертация в список
# print(list(student.values()))
# print(list(student.items())[0])

# people = ['John', 'Mary', 'Oscar', 'Jack']
# # for <variable> in <iterable:
# for person in people:
#     print(person)
#
# print('Finished')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in numbers:
#     for num2 in numbers:
#         for num3 in numbers:
#             for num4 in numbers:
#                 print(num, num2, num3, num4)
    # print(num ** 2)

# for num1 in numbers
#     x = num1 ** 2
#     if x % 2 == 0
#         print(x, Even)
#
# print('Finished')

# x = 5
# student = {'name': 'John', 'age': 32, 'courses': ['Math', 'Art', 'Programming'],
#            1: 'int key', 0.2: 'float key', x: 'variable', 'var key': x}

# for key in student:
#     print(key)
#
# print(list(student.items()))
#
# for key, values in student.items():
#     print(str(key) +

# people = [['John', 'Moskva', 35, 'male'], ['Alex', 'Tallinn', 20, 'male'], ['Jane', 'London', 25, 'female']]
#
# for name, town, gender in people:
#     print(name, town, gender)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers2 = range(0, 10)
#
# for x in range(6, 29):
#     print(x)
#
# 0-100
# если число делится на 3 без остатка написать Fizz
# если число делится на 5 без остатка написать buzz
# если число делится на 3,5 без остатка написать Fizzbuzz

numbers = range(0, 100)
for numbers in range(0, 100):
    if numbers % 3 == 0:
        print('Fizz')
for numbers in range(0, 100):
    if numbers % 5 == 0:
        print('buzz')
for numbers in range(0, 100):
    if numbers % 3 == 0 or numbers % 5 == 0:
        print('Fizzbuzz')