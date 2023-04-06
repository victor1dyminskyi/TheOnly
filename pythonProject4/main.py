# a = 'I wanna do Peter\'s HW'
#
# # сира стірчка
# # цю стрічку він сприйняв із тими символами \n \t
# ТУТ CONST - це незмінна штука, бо в неї ім'я все з великої
# CONST1 = "same\name\table"
#
# # тут комп тепер шарить, що йому потрібно ігнорувати ці штуки \n \t (бо є r)
# CONST2 = r"same\name\table"
#
# print("const1", CONST1)
# print("const2", CONST2)


# Старий спосіб виводу інфи
# name = "John"
# age = 23
# salary = 999.99
# print("%s is %d years old, Your salary is %3f " % (name, age, salary))



# Новий спосіб виводу інфи 1
# name = "John"
# age = 23
# salary = 999.99
#
# print("Hello {}, {}, {}".format(name, age, salary))

# Новий спосіб виводу інфи 2
# name = "John"
# age = 23
# salary = 999.99
#
# print("Hello {1}, {0}, {2}".format(name, age, salary))
# оскільки тут кожен елемент у format має свій індекс, то ми можемо конкретні дані вставляти

# Новий спосіб виводу інфи 3
# name = "John"
# age = 23
# salary = 999.99
# 
# print("Hello {j}, {b}, {c}".format(j = "john", b = "23", c = "999.99"))

# Новий спосіб виводу інфи 4
# name = "John"
# age = 23
# salary = 999.99
# 
# print("Hello, " + name + str(age))

# Новий спосіб виводу інфи 4
# F string – ф стрінга - 
# name = "John"
# age = 23
# salary = 999.99
#
#
# print(f"Hello {name}, {age}, {salary}")
# -----------------------------------------------------------------------------
# команди:

# a = "asdasda"
# b = len(a)
#
# print(b)

# Тут усе включно
# print("a[1] = ", a[0])
# print("a[1] = ", a[0:5])
# print("a[1] = ", a[:])
# тут з'являєтсья така штука як крок - вона позначаєтсья останньою
# print("a[1] = ", a[2:6:2])
# print("a[] = ", a[1:-1])

# -----------------------------------------------------------------------------


# a = 90
# if a:
#     print("Hello")
# тут надрукує таки hello, оскліьки 9 - це не 0, а 0 - це означає false.

a = 0
b = 9

# print("", a > 0 and a == b)
# print("", a > 0 or a < b)
# print("", a > 0 > b)

# print("result", not a)
#
# print("result", 23 or [63, 90] or "" or None)
# #  тут комп повертає першу істину - 23
#
# print("result", 23 and [63, 90] and "" and None)
# #  тут повертає першу не істину
#
# print("result", 23 and [63, 90] and "qweqwe" and [1, 8])
# # тут він повертає останню істину
#
# print("result", None or [] or "" or 23)
# Тут повертає останню істину

# a = 9999
# b = 9999
#
# print("", a is b)
# is - це те ж саме що й ==

weather = int(input("enter the temp "))

print("cold" if weather < 15 else "hot")





