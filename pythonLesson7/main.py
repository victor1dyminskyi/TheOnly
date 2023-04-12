# def printer_func(a : int, b : int) -> int:
#     print("hello")
#     """
#     Doc string: that is fun
#     """
#     return a+b
# print(printer_func(4, 7))
#
# print(printer_func.__doc__)


# def print_info(name: str, age: int) -> None:
#     print("Name: ", name)
#     print("Age: ", age)
#
# print_info("Alex", 18)
# print("-" * 10)
# print_info("Ogi", 25)
# print("-" * 10)
# print_info(age = 67, name = "Sam")

# def print_numbers(number, *args):
#     print("argument: ", number)
#     print("vartuple: ")
#     print(type(args))
#     for var in args:
#         print(var)
#
# print_numbers(10)
# print("-" * 10)
# print_numbers(70, 60, 50, 40)


# def adding(*args):
#     sum = 0
#     length = len(args)
#     for var in args:
#         sum = var + sum
#     return sum / length
#
# print(adding(10,5,5))
#
# def adding(*args):
#     return sum(args) / len(args)
#
# print(adding(10,5,5))
# total = 0
#
# def my_sum(arg1, arg2):
#     global total
#     total = arg1 + arg2
#     return total
#     # print(total)
#
# a = my_sum(1,2)
# print(a)
# print(total)
# --------------------------------------------------------!!!!!!!!!!!!!!!!
# LESSON 8

# def rec(in_param):
#     if in_param < 5:
#         print(in_param)
#         """РЕКУРСІЯ - навантаження стеку, оперативки, оперативної пам'яті)"""
#         rec(in_param + 1)
#         print(in_param)
#
# rec(1)


# def factorial(in_data):
#     """РЕКУРСІЯ - навантаження стеку, оперативки, оперативної пам'яті)"""
#     if in_data == 1:
#        return 1
#     return factorial(in_data-1)*in_data
# print(factorial(3))

# p = lambda x,y: x+y
# print(p(5,8))

# list = [1, 2]
# list.insert(2, 5)
# print(list)
#
#
# b = [6, 7, 8]
# list.extend(b)
# print(list)
#
# list.append(b)
# print(list)
#
# list.pop()
# print(list)


# list1 = ["key1", "key2", "key3"]
# a = enumerate(list1)
# print(list(a))

# list = [x * 2 for x in range(10)]
# print(list)
# ---------------------------------------------------------------------------
# 1 TASK
#
# list_even = []
# list_odd = []
# list_else = []
# for i in range(101):
#     if i % 2 == 0:
#         list_even.append(i)
#     elif i % 3 == 0:
#         list_odd.append(i)
#     else:
#         list_else.append(i)
#
# print("Here is the list of even numbers that are divisible by 2 ", list_even)
# print("Here is the list of odd numbers that are divisible by 3: {}".format(list_odd))
# print(f"Here is the list of all left numbers: {list_else}")

#
# # ---------------------------------------------------------------------------
# # 2 TASK
#
# login = 0
# login_try = "First"
# def function_check():
#     global login
#     while login != login_try:
#         login = input("Enter your login: ")
#         if login == login_try:
#             print("Nice, you passed ")
#         else:
#             print("Try again ")
#
# function_check()
#
# def add_indexes(lst):
#     # 	my_list = []
#     list1 = []
#     my_list = list(enumerate(lst))
#     for i in my_list:
#        element = i[1] + i[0]
#        list1.append(element)
#     return list1
# print(add_indexes([5, 4, 3, 2, 1]))

# def probability(lst, num):
#     length = len(lst)
#     list = []
#     for i in lst:
#         if i >= num:
#             add = list.append(i)
#         else:
#             continue
#     length_of_list = len(list)
#     result = round(100 * (length_of_list/length), 1)
#     return result
#
# print(probability([1,2, 3, 1, 1, 2,4, 6, 1], 2))


# def find_odd(lst):
#     list = []
#     for i in lst:
#         if type(i) is int:
#             if i not in list:
#                 counter = lst.count(i)
#                 if counter % 2 != 0:
#                     list.append(i)
#             else:
#                 continue
#     return list
#
#
# print(find_odd([20, 1, 1, 2, 1, 2, 3, 3, 5, 5, 4, 20, 4, 5]))


# def nth_smallest(lst, n):
#     length = len(lst)
#     if length >= n:
#         list = sorted(lst)
#         return list[n-1]
#     else:
#         return None
#
#
# print(nth_smallest([1, 3, 5, 7], 5))

# my_list = ["Hello", "Python"]
# print("-".join(my_list))

# dict_login = {}
# login_first_only = input("Enter your login: ")
# dict_login["login"] = login_first_only
# def function_login():
#     """This function is about loggining people in"""
#     login_next = 0
#     while login_next != login_first_only:
#         login_next = input("enter your login again ")
#         print("Try again")
#
#
# # print(function_login.__doc__)
# function_login()
# print()
#

# ----------------------------------------------------------------------


# list1 =  [1, 2, 3, 4]
#
# new_list = list(map(lambda x: x * 2, list1))
# print(new_list)

# -------------------------------------------------------
# 1 TASK
# def biggest_number(num1, num2):
#     if num1 > num2:
#         print("{} is bigger".format(num1))
#     elif num1 < num2:
#         print("{} is bigger".format(num2))
#     else:
#         print(f"{num1} and {num2} are equal")
#
#
# print(biggest_number(num2 = 25,num1 =24))

# -------------------------------------------------------
# 2 TASK
# desire = input("choose your figure: ")
#
# def rectangle():
#     a = int(input("One side: "))
#     b = int(input("The other side: "))
#     square = a * b
#     print(square)
#     return square
#
# def triangle():
#     a = int(input("The basis: "))
#     h = int(input("The height: "))
#     square = (1/2) * a * h
#     print(square)
#     return square
#
# def circle():
#     r = int(input("The radius: "))
#     square = float(3.14 * (r ** 2))
#     print(square)
#     return square
#
# if desire == "rectangle":
#     rectangle()
#
# elif desire == "triangle":
#     triangle()
#
# elif desire == "circle":
#     circle()
#
# else:
#     print("error")
# -------------------------------------------------------
# 3 TASK
#
# word = input("Enter a word: ")
# def calculator():
#     global word
#     add = 0
#     enumeration = enumerate(word)
#     list_word = list(enumeration)
#     length = len(list_word)
#     print(list_word, f"the number of cheracters: {length}")
# calculator()

# -------------------------------------------------------
# from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

# owm = OWM('774fd4821d373562413df19f7f051235')
# mgr = owm.weather_manager()
#
#
# # Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather
#
# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75
#
# # Will it be clear tomorrow at this time in Milan (Italy) ?
# forecast = mgr.forecast_at_place('Milan,IT', 'daily')
# answer = forecast.will_be_clear_at(timestamps.tomorrow())
#


