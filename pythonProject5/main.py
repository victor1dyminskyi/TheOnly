# The_age = int(input("Enter the name of your character"))



# while The_age > 10:
#     print("working on....\n", The_age)
#     The_age = The_age - 1


# ab = [1, 2, 3, 4]
#
# part = ab[3:0:-1]
# print(part)

# status = int(input("enter your age "))
status = str(input("enter weather "))

# match status:
#     case child if status in range(0, 18):
#         print("Go sleep")
#     case adult if status in range(18, 25):
#         print("Go study")
#     case experienced if status in range(25, 100):
#         print("Do whatever you want")



match status:
    case bad ['']:
        print("take your umbrella")
    case good:
        print("good luck")
