# li = [1, 2, 3, 4]
# li.append()

# a = "asdasda"
# li12 = {1, 2, 3, 4}
# li12.append(0)

# print(id(li12), li12, type(li12) is set)

# another way of printing values:---------------------------------------------
# a = "aserty"
# sallap = 43

# fl = 123.423131231
# print("your value is {0} and in binary system it is {0:b}".format(12))
# :b - binary system

# print("{0:.3f} is rounded".format(fl))
# :.3f - rounding of

# another way of printing values:---------------------------------------------

# b = "asdasewqwe"
#
# print("%s is a string and %s is also one" %(a, b))

# print(dir(b))
# -----------------------------------------------------------------1111
# def is_isogram(word):
#     for char in word:
#         if word.count(char) > 1:
#             continue
#         return True
#     else:
#         return False
#
# print(is_isogram("qwertyy"))

# def mean(number):
#     a = list(number)
#     length = len(a)
#     print(a)
# number = 123
# a = str(number)
# list = list(a)
# length1 = len(list)
# print(length1)
# print(list)

# def mean(number):
#     string = str(number)
#     list = list(string)
#     print(list)
#     list2 = [0]
#     for i in list:
#         integer = int(i)
#         result = list2[-1] + integer
#         add = list2.append(result)
#
# def mean(number):
#     list1 = []
#     string = str(number)
#     list1 = list(string)
#     list2 = [0]
#     for i in list1:
#         integer = int(i)
#         result = list2[-1] + integer
#         add = list2.append(result)
#     final_result = round(list2[-1]/len(list1))
#     return final_result
#
# print(mean(1024))

# def is_isogram(word):
#     neww = word.lower()
#     print(neww)
#     for char in neww:
#         print(char)
#         if neww.count(char) > 1:
#             return False
#         continue
#     else:
#         return True
#
# print(is_isogram("ONHhh"))

#
# word = "aweawe"
# def count_vowels(word):
#         list = ["a", "e", "i", "o", "u"]
#         sum = 0
#         for vowel in list:
#             counter = word.count(vowel)
#             # print(vowel)
#             sum = counter + sum
#             # continue
#         return sum
#
#
#
# print(count_vowels("aeiouuu"))



# neww = "PasSword"
# ferty = neww.lower()
# a = ferty.count("s")
# print(a)


# def binary(decimal):
#     if int(decimal) > 0:
#         list = []
#         binary_result = []
#         length = len(decimal)
#         for inte in decimal:
#             for i in range(length):
#                 result = int(inte) * (10 ** (length - (i + 1)))
#                 print(inte)
#                 add = list.append(result)
#                 binary = bin(list[i])
#                 save = binary_result.append(binary[2:])
#                 # continue
#             # continue
#
#         return binary_result
#     else:
#         print(0)
#
# print(binary("300"))

# def binary(decimal):
#     if int(decimal) > 0:
#         binary_result = bin(int(decimal))
#         return binary_result[2:]
#     else:
#         print(0)
#
# print(binary("200"))

# num = "200"
# inte = 2
# length = len(num)
# a = inte * (10 ** (length -  1))
# print(a)
# def integer_boolean(binary_number):
#     list = []
#     for i in binary_number:
#         print(i)
#         if int(i) == 1:
#             add = list.append(True)
#         else:
#             add_extra = list.append(False)
#         continue
#     return list
#
# print(integer_boolean("010101"))

# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             # print(var)
#             continue
#             var += 1
#     var+=1
#     print(var)
# else:
#     var+=1
# print(var)

# ---------------------------------