# task1
# try:
#     num = int(input("Enter the number of the day of the week (1-7), \nwhere 1 is Monday, and 7 is Sunday:   "))
#
#     match num:
#         case 1:
#             print("This number stands for Monday!")
#         case 2:
#             print("This number stands for Tuesday!")
#         case 3:
#             print("This number stands for Wednesday!")
#         case 4:
#             print("This number stands for Thursday!")
#         case 5:
#             print("This number stands for Friday!")
#         case 6:
#             print("This number stands for Saturday!")
#         case 7:
#             print("This number stands for Sunday!")
#         case _:
#             print("Incorrect number")
# except ValueError:
#     print("Please enter only numbers")
# except Exception as e:
#     print(f"Error {e}")
# finally:
#     print("Have a nice day, whatever day of the week it is:)")

# task2 variant1
# while True:
#     try:
#         n1 = int(input("Enter the first number: "))
#         n2 = int(input("Enter the second number: "))
#     except ValueError:
#         print("Enter only numbers, starting from the beginning")
#         continue
#
#     if n1 < n2:
#         print(f"Ascending order: {n1}, {n2}")
#         break
#     elif n1 > n2:
#         print(f"Ascending order: {n2}, {n1}")
#         break
#     elif n1 == n2:
#         print("Numbers equal")
#         break
#     else:
#         print("Incorrect values")
#         break
# print("Calculations finished")

# task2 variant2
# try:
#     n1 = 0
#     n2 = 0
#     while True:
#         try:
#             n1 = int(input("Enter the first number: "))
#         except ValueError:
#             print("Enter only numbers, please")
#             continue
#         break
#     while True:
#         try:
#             n2 = int(input("Enter the second number: "))
#         except ValueError:
#             print("Enter only numbers, please")
#             continue
#         break
#     if n1 < n2:
#         print(f"Ascending order: {n1}, {n2}")
#     elif n1 > n2:
#         print(f"Ascending order: {n2}, {n1}")
#     elif n1 == n2:
#         print("Numbers equal")
#     else:
#         print("Incorrect values")
# finally:
#     print("Calculations finished")


# task3
# try:
#     num1 = 0
#     num2 = 0
#     operation = 0
#     user_select = 0
#     print("You can do an arithmetic operation with 2 numbers")
#     while user_select != 5:
#         while True:
#             try:
#                 num1 = int(input("Enter the first number: "))
#             except ValueError:
#                 print("Enter only numbers, please")
#                 continue
#             break
#         while True:
#             try:
#                 num2 = int(input("Enter the second number: "))
#             except ValueError:
#                 print("Enter only numbers, please")
#                 continue
#             break
#
#         while True:
#             try:
#                 print("Choose the action from menu: \n1. + \n2. - \n3. * \n4. / \n5. Exit")
#                 user_select = int(input("Enter menu number: "))
#                 if user_select == 1:
#                     result = num1 + num2
#                     print(f"{num1} + {num2} = {result}")
#                     print("End of calculations, starting anew!")
#                 elif user_select == 2:
#                     result = num1 - num2
#                     print(f"{num1} - {num2} = {result}")
#                     print("End of calculations, starting anew!")
#                 elif user_select == 3:
#                     result = num1 * num2
#                     print(f"{num1} * {num2} = {result}")
#                     print("End of calculations, starting anew!")
#                 elif user_select == 4:
#                     result = num1 / num2
#                     print(f"{num1} / {num2} = {result}")
#                     print("End of calculations, starting anew!")
#                 elif user_select == 5:
#                     print("Exit...See you next time!")
#             except ValueError:
#                 print("Incorrect value, choose a menu item!")
#                 continue
#             except ZeroDivisionError:
#                 print("Division by zero is impossible. Let's start anew")
#             break
# except Exception as e:
#     print(f"Error: {e}")

# tasks finished
