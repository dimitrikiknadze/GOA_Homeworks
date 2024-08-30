# list = [0, 2, 4, 6, 8, 10]
# list_2 = [1, 3, 5, 7, 9]
# def ifelseindex(index):
#     if index == list:
#         print("even")
#     else:
#         print("odd")
# ifelseindex(input("please enter any nember in range 0-11: "))


num_0 = 0
num_1 = 1
num_2 = 2
num_3 = 3
num_4 = 4
num_5 = 5
num_6 = 6
num_01 = -1
num_02 = -2
num_03 = -3
num_04 = -4
num_05 = -5
num_06 = -6

def numbers(num):
    if num == num_0:
        print(0)
    elif num == num_1:
        print(-1)
    elif num == num_2:
        print(-2)
    elif num == num_3:
        print(-3)
    elif num == num_4:
        print(-4)
    elif num == num_5:
        print(-5)
    elif num == num_6:
        print(-6)
    elif num == num_01:
        print(1)
    elif num == num_02:
        print(2)
    elif num == num_03:
        print(3)
    elif num == num_04:
        print(4)

numbers(input("please enter any number in range -6 -2 6: "))