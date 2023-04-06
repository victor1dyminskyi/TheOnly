# status_code = int(input("Enter"))
#
# match status_code:
#     case 400:
#         print("bad request")
#     case 401:
#         print("qweq")
#     case 402 | 403 as error:
#         print(f" {error} si an error")


# --------------------------------------------!!!!!!!!!!!!!!!!!!
# a = "qwer~tyd~rer"
# ab = a.split("~")

# print(a)
# --------------------------------------------!!!!!!!!!!!!!!!!!!


# first_number = int(input("Enter your Dirst number "))
# Second_number = int(input("Enter your Second number "))
#
# if first_number > Second_number:
#     print(f"{first_number} is bigger than {Second_number}")
# elif first_number == Second_number:
#     print("oops, they are the same")
# elif first_number < Second_number:
#     print(f"{first_number} number is lower than the {Second_number}")


# --------------------------------------------------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# LOOOOOOPS
#   WHILE
# i = 5
# while i <= 15:
#     i = i + 1
#     print(i)

#     FOR
# for i in "hello world":
#     print(i * 2)

# d = {1: 'one', 2: 'two'}
# start = 0
# finish = 10
#
# while start < finish:
#     if start == 5:
#         start += 1
#         # continue
#         break
#     print(start)
#     start += 1
# else:
#     print("The end")

#     break - вистрибує з того циклу, у якому ти знаходився. До того ж, break ще й забирає літерал, який ти зазначив у if (наприклад)
#     Continue - прибирає літер зазначений вище (наприклад, у if) і продовжує цикл далі в плоть до else включно.

for j in [0, 1, 2, 3, 4, 5]:
    if j == 2:
        print(j)
        # continue
        j += 1
    else:
     print(j, "- is the least")

# for j in range(2, 6):
#     print(j)

