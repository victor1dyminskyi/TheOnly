# li - містить покликання на об'єкт пам'ті

# li = ["hello", 78, 90, 56.8, True, [1,2,3,4]]
# id()

# переприсвоєння значення
# li[0] = "wats's up"
# print(li)
# print(li[-1][1])


# s = li[:]
# - це новий об'єкт, який був створений слайзінгом slice і відповідно має іншу айдішку від того об'єкту li

# f = [1,2,3] +[4,5,6]
# print(f)
# списки можна додввати.

# print(f[2:3])
# print(f[1:5])
#
# f.insert(2,22)
# додавання в конкретне місце елменту в list

# print(f)
#
# f.reverse()
# print(f)
#
# l1 = [1,2,3]
# l2 = l1
# - це ідентичні об'єкти
#
# l3 = l1[:]
# це різні об'єкти. Тепре l3 - це інший об'єкт, з іншим id, а відповідно при зміні значень у l1, l3 залишатиметься не змінним.

# li1 = [22, 1, 7, 3]
# li2 = [89, 6, 4, 99]
#
# print(li1, li2)
#
# w = sorted(li1)
# # - працює з копією. ВІдповідно повретає мені новий елемент. Має слово return
# q = li2.sort()
# # - працює з оригіналом й відповідно міняє його
# print("w: ", w,"q:", q)
# # - змінна q у даному впадку створює новий елмент, у якому є значення none, але паралельно ще й  міняє оригінал. Тобто тут нічого не повретаєтсья
# print("next step")
# print(li1, li2)

# x = ['apple', 'banana', 'mango']
# y = enumerate(x)
# print(y)
# print(list(y))
#
# my_list = []
#
# for item in range(6):
#     my_list.append(item)
#
# print(my_list)
#
# q = [item for item in range(6) if item % 2 == 0]
# print(q)

# for fruit in ['apple','banana','mango']:
#     print("I like",fruit)




# for number in range(int(input("enter the amount of numbers you want to add"))):
#     li = [int(input(f"enter your numbers {number} "))]
#     print(max(li), min(li))


# for i in ['apple', 'banana', 'morc']:
#     print(i)

# def card_hide(card):
#     if len(card) == 16:
#         return "*"*12 + card[12:16]
#     else:
#         return "Invalid card"
#
# print(card_hide("1234567891234567"))

# def X_O(word):
#   a = word.lower()
#   if a.count("x") == a.count("o"):
#       return True
#   elif a.count("x") == 0 and a.count("o") == 0:
#       return True
#   else:
#       return False

# def stutter(word):
#     strug = ""
#     if len(word) >= 2:
#         strug = str(word[0]* 2) + "..." + str(word[1] * 2) +"..." + str(word[2::]) + "?"
#         return strug
#     else:
#         return "OH..."
#
# print(stutter("Hello"))

x = 100
y = 50
print(x and y)