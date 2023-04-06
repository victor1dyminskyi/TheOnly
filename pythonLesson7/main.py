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
