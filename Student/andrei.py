# # a = 500
# # b = 200
# # print(a + b)
# # print('result')
# # print(a - b - 1000 + 200)
# # print(type(a))
# # a = 50
# # b = 200
# # result = a / b
# # result = a ** 3
# # print(result)
# # some_string = '500'
# # string2 = ' years old'
# #
# # print(some_string + str(a) + string2)
# # print(float(a))
# # print_string = '500'
# # print(type(int(some_string)))
# # print(500 + True)
# # print(500 + False)
# # a = 30
# # b = 2.5
# #
# # user_input = input('Please enter your salary: ')
# # print(user_input)
# # print(type(user_input))
# #
# # int()
# # float()
# # str()
# # bool()
#
# a = 0
# b = 2.5
# bool_var = False
# text_string = 'Hello world'
# none_var = None
#
# name = 'Andrei'
# age = '33'
# print('Hello ' + name + ' you are ' + age + ' old')
# print('Hello',  name,  'you are',  age,  'old')
#
# a, b, c = 10, 20, 30
# print(a)
# print(b)
# print(c)
#
# user_input = input('Please enter: ')
# a, b, c = user_input.split(', ')
# print(a)
# print(b)
# print(c)
#
# a = input('Please enter A: ')
# b = input('Please enter B: ')
# c = input('Please enter C: ')
#
# a, b, c = input('Please enter: ').split(', ')
# print(a)
# print(b)
# print(c)
# a, b, c = input('Please enter sides A, B and C. Use spase separator: ').split()
# half_perimetr = (int(a) + int(b) + int(c)) / 2
# print(half_perimetr)
#
# triangle_area = (half_perimetr * (half_perimetr - int(a)) * (half_perimetr - int(b)) *
#                 (half_perimetr - int(c))) ** 0.5

# a, b, c, d = input('Please enter sides A, B, C and D Use spase separator: ').split()
# perimetr = (int(a) + int(b)) * 2
# print(perimetr)
# rectangle_area = (int(a) * int(b))
# print(rectangle_area)


# print('trapezium_area')
# a, b, h = input('Please enter sides A, B, and height H Use spase separator: ').split()
# trapezium_area = ((int(a) + int(b)) / 2) * int(h)
# print(trapezium_area)

# print('trapezium_area')
# a, b, c, d = input('Please enter sides A, B, C and D Use spase separator: ').split()
# trapezium_area = ((int(a) + int(b)) / 2) * (((int(c) ** 2) - (((((int(b) - int(a)) ** 2) + (int(c) ** 2) -
#                                                                (int(d) ** 2)) / (2 * (int(b) - int(a)))) ** 2)) ** 0.5)
# print(trapezium_area)

print('equilateral_triangle_area')
a = input('Please enter side A: ')
equilateral_triangle_area = ((3 ** 0.5) * (int(a) ** 2)) / 4
print(equilateral_triangle_area)
