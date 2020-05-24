# number = int(input('Write how many cups of coffee you will need:'))
# print('For', number,  'cups of coffee you will need:')
# print(number * 200, 'ml of water')
# print(number * 50, 'ml of milk')
# print(number * 15, 'g of coffee beans')


# amount of water, milk and beans required for one cup
# waterReq = 200
# # # milkReq = 50
# # # coffeeBeansReq = 15
# # #
# # # # print total water, milk and beans
# # # print("Write how many ml of water the coffee machine has:")
# # # totalWater = int(input())
# # # print("Write how many ml of milk the coffee machine has")
# # # totalMilk = int(input())
# # # print("Write how many grams of coffee beans the coffee machine has")
# # # totalCoffeeBeans = int(input())
# # # neededCups = int(input("How many cups of coffee you will need: "))
# # #
# # # # get maximum number of cups of coffee that can be made from available water, milk and beans
# # # maxCupsByWater = totalWater // waterReq
# # # maxCupsByMilk = totalMilk // milkReq
# # # maxCupsByBeans = totalCoffeeBeans // coffeeBeansReq
# # # maxCupsArr = [maxCupsByWater, maxCupsByMilk, maxCupsByBeans]
# # # maxCups = int(min(maxCupsArr))
# # #
# # # if maxCups == neededCups:
# # #     print("Yes, I can make that amount of coffee")
# # #
# # # if maxCups > neededCups:
# # #     moreThanWanted = maxCups - neededCups
# # #     print("Yes, I can make that amount of coffee (and even ", moreThanWanted ," more than that")
# # #
# # # elif maxCups < neededCups:
# # #     print("No, I can make only ", maxCups, "cups of coffee")


# Write your code here
# money = 550
# water = 400
# milk = 540
# coffee_beans = 120
# dis_cups = 9
#
#
# def accounting():
#     print(f"""
# The coffee machine has:
# {water} of water
# {milk} of milk
# {coffee_beans} of coffee beans
# {dis_cups} of disposable cups
# {money} of money
# """)
#
#
# def buy():
#     command_buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
#     global money, water, milk, coffee_beans, dis_cups
#     if command_buy == '1':
#         water -= 250
#         coffee_beans -= 16
#         money += 4
#         dis_cups -= 1
#     elif command_buy == '2':
#         water -= 350
#         milk -= 75
#         coffee_beans -= 20
#         money += 7
#         dis_cups -= 1
#     elif command_buy == '3':
#         water -= 200
#         milk -= 100
#         coffee_beans -= 12
#         money += 6
#         dis_cups -= 1
#
#
# def fill():
#     global water, milk, coffee_beans, dis_cups
#     water += int(input('Write how many ml of water do you want to add:'))
#     milk += int(input('Write how many ml of milk do you want to add:'))
#     coffee_beans += int(input('Write how many grams of coffee beans do you want to add:'))
#     dis_cups += int(input('Write how many disposable cups of coffee do you want to add:'))
#
#
# def take():
#     global money
#     print(f'I gave you ${money}')
#     money -= money
#
#
# accounting()
# command = input('Write action (buy, fill, take):')
# while command != 'exit':
#     if command == 'buy':
#         buy()
#     elif command == 'fill':
#         fill()
#     elif command == 'take':
#         take()
#
#
#
# print('Bye')

# curr_water = 400
# curr_milk = 540
# curr_coffee = 120
# curr_money = 550
# curr_dis_cups = 9
# status = True
#
# def printResources():
#     print('The coffee machine has:')
#     print(curr_water, 'of water')
#     print(curr_milk, 'of milk')
#     print(curr_coffee, 'of coffee beans')
#     print(curr_dis_cups, 'of disposable cups')
#     print(curr_money, 'of money')
#     print()
#
#
# def makeEspresso():
#     global curr_water, curr_milk, curr_coffee, curr_money, curr_dis_cups
#     curr_water = curr_water - 250
#     curr_coffee = curr_coffee - 16
#     curr_dis_cups = curr_dis_cups - 1
#     curr_money = curr_money + 4
#
# def makeLatte():
#     global curr_water, curr_milk, curr_coffee, curr_money, curr_dis_cups
#     curr_water = curr_water - 350
#     curr_milk = curr_milk - 75
#     curr_coffee = curr_coffee - 20
#     curr_dis_cups = curr_dis_cups - 1
#     curr_money = curr_money + 7
#
# def makeCappuccino():
#     global curr_water, curr_milk, curr_coffee, curr_money, curr_dis_cups
#     curr_water = curr_water - 200
#     curr_milk = curr_milk - 100
#     curr_coffee = curr_coffee - 12
#     curr_dis_cups = curr_dis_cups - 1
#     curr_money = curr_money + 6
#
# def fillMachine():
#     global curr_water, curr_milk, curr_coffee, curr_money, curr_dis_cups
#     fill_water = int(input('Write how many ml of water do you want to add:\n'))
#     curr_water = curr_water + fill_water
#     fill_milk = int(input('Write how many ml of milk do you want to add:\n'))
#     curr_milk = curr_milk + fill_milk
#     fill_coffee = int(input('Write how many grams of coffee beans do you want to add:\n'))
#     curr_coffee = curr_coffee + fill_coffee
#     fill_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
#     curr_dis_cups = curr_dis_cups + fill_cups
#
# def takeMoney():
#     global curr_money
#     print('I gave you $',curr_money)
#     curr_money = 0
#
# while status == True:
#
#     action = input('Write action (buy, fill, take, remaining, exit):\n')
#
#     if action == 'buy':
#         choose_product = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
#         if choose_product == '1':
#             if curr_water >= 250 and curr_coffee >= 16 and curr_dis_cups >= 1:
#                 print('I have enough resources, making you a coffee!')
#                 makeEspresso()
#             elif curr_water < 250:
#                 print('Sorry, not enough water!')
#             elif curr_coffee < 16:
#                 print('Sorry, not enough coffee!')
#             elif curr_dis_cups < 1:
#                 print('Sorry, not enough disposable cups!')
#
#         elif choose_product == '2':
#             if curr_water >= 350 and curr_milk >= 75 and curr_coffee >= 20 and curr_dis_cups >= 1:
#                 print('I have enough resources, making you a coffee!')
#                 makeLatte()
#             elif curr_water < 350:
#                 print('Sorry, not enough water!')
#             elif curr_milk < 75:
#                 print('Sorry, not enough milk!')
#             elif curr_coffee < 20:
#                 print('Sorry, not enough coffee!')
#             elif curr_dis_cups < 1:
#                 print('Sorry, not enough disposable cups!')
#
#         elif choose_product == '3':
#             if curr_water >= 200 and curr_milk >= 100 and curr_coffee >= 12 and curr_dis_cups >= 1:
#                 print('I have enough resources, making you a coffee!')
#                 makeCappuccino()
#             elif curr_water < 200:
#                 print('Sorry, not enough water!')
#             elif curr_milk < 100:
#                 print('Sorry, not enough milk!')
#             elif curr_coffee < 12:
#                 print('Sorry, not enough coffee!')
#             elif curr_dis_cups < 1:
#                 print('Sorry, not enough disposable cups!')
#
#         elif choose_product == 'back':
#                 status = True
#
#
#     elif action == 'fill':
#         fillMachine()
#     elif action == 'take':
#         takeMoney()
#     elif action == 'exit':
#         status = False
#     elif action == 'remaining':
#         printResources()

class Coffee:
    def __init__(self, water, milk, beans, cups, money):
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.water = water
        self.state = ""

    def states(self):
        while self.state != "exit":
            self.state = input("Write action (buy, fill, take, remaining, exit):")
            if self.state == "buy":
                purchase = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to "
                                    "main menu:")
                if purchase == "1":
                    if self.beans >= 16 and self.water >= 250 and self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.money += 4
                        self.beans -= 16
                        self.water -= 250
                        self.cups -= 1
                    elif self.beans < 16:
                        print("Sorry, not enough beans!")
                    elif self.water < 250:
                        print("Sorry, not enough water!")
                    elif self.cups < 1:
                        print("Sorry, not enough cups!")
                elif purchase == "2":
                    if self.beans >= 7 and self.water >= 250 and self.milk >= 75 and self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.money += 7
                        self.water -= 350
                        self.milk -= 75
                        self.beans -= 20
                        self.cups -= 1
                    elif self.beans < 16:
                        print("Sorry, not enough beans!")
                    elif self.water < 250:
                        print("Sorry, not enough water!")
                    elif self.cups < 1:
                        print("Sorry, not enough cups!")
                    elif self.milk < 75:
                        print("Sorry, not enough milk!")
                elif purchase == "3":
                    if self.beans >= 12 and self.water >= 200 and self.milk >= 100 and self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.money += 6
                        self.water -= 200
                        self.milk -= 100
                        self.beans -= 12
                        self.cups -= 1
                    elif self.beans < 12:
                        print("Sorry, not enough beans!")
                    elif self.water < 200:
                        print("Sorry, not enough water!")
                    elif self.cups < 1:
                        print("Sorry, not enough cups!")
                    elif self.milk < 100:
                        print("Sorry, not enough milk!")
                elif purchase == "back":
                    continue
            elif self.state == "fill":
                self.water += int(input("Write how many ml of water do you want to add:"))
                self.milk += int(input("Write how many ml of milk do you want to add:"))
                self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
                self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
            elif self.state == "take":
                print(f"I gave you ${self.money}")
                self.money = 0
            elif self.state == "remaining":
                print(f"""
                    The coffee machine has:
                    {self.water} of water
                    {self.milk} of milk
                    {self.beans} of beans
                    {self.cups} of disposable cups
                    ${self.money} of money """)
hi = Coffee(400,540,120,9,550)
hi.states()