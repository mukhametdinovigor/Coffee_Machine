class CoffeeMachine:
    def __init__(self):
        self.supplies = {'ml of water': 400, 'ml of milk': 540, 'grams of coffee beans': 120, 'disposable cups': 9, 'money': 550}
        self.espresso = {'ml of water': 250, 'grams of coffee beans': 16, 'disposable cups': 1, 'money': -4}
        self.latte = {'ml of water': 350, 'ml of milk': 75, 'grams of coffee beans': 20, 'disposable cups': 1, 'money': -7}
        self.cappuccino = {'ml of water': 200, 'ml of milk': 100, 'grams of coffee beans': 12, 'disposable cups': 1, 'money': -6}
        self.user_input = None

    def rule_machine(self):
        while self.user_input != 'exit':
            def buy_drink():
                numb_drink = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n> ')
                flag = 0
                if numb_drink == '1':
                    while True:
                        for item in self.espresso.keys():
                            if self.espresso[item] > self.supplies[item]:
                                print(f'Sorry, not enough {item.split()[-1]}!')
                                flag = 1
                                break
                        if flag == 1:
                            break
                        else:
                            for item in self.espresso.keys():
                                self.supplies[item] -= self.espresso[item]
                            print('I have enough resources, making you a coffee!')
                            break
                elif numb_drink == '2':
                    while True:
                        for item in self.latte.keys():
                            if self.latte[item] > self.supplies[item]:
                                print(f'Sorry, not enough {item.split()[-1]}!')
                                flag = 1
                                break
                        if flag == 1:
                            break
                        else:
                            for item in self.latte.keys():
                                self.supplies[item] -= self.latte[item]
                            print('I have enough resources, making you a coffee!')
                            break
                elif numb_drink == '3':
                    while True:
                        for item in self.cappuccino.keys():
                            if self.cappuccino[item] > self.supplies[item]:
                                print(f'Sorry, not enough {item.split()[-1:]}!')
                                flag = 1
                                break
                        if flag == 1:
                            break
                        else:
                            for item in self.cappuccino.keys():
                                self.supplies[item] -= self.cappuccino[item]
                            print('I have enough resources, making you a coffee!')
                            break

            def fill_machine():
                for item in self.supplies.keys():
                    if item != 'money':
                        self.supplies[item] += int(input(f'Write how many {item} do you want to add:\n> '))

            def remaining():
                print('The coffee machine has:')
                for key, val in self.supplies.items():
                    if key == 'ml of water' or key == 'ml of milk':
                        print(f'{val} of {key.split()[-1]}')
                    elif key == 'grams of coffee beans':
                        i = key.split()
                        print(f'{val} of {i[-2]} {i[-1]}')
                    elif key == 'money':
                        print(f'${val} of {key}')
                    else:
                        print(f'{val} of {key}')

            def take():
                for item in self.supplies:
                    if item == 'money':
                        print(f'I gave you ${self.supplies[item]}')
                        self.supplies[item] = 0

            self.user_input = input('Write action (buy, fill, take, remaining, exit):\n> ')
            if self.user_input == 'buy':
                buy_drink()
            elif self.user_input == 'fill':
                fill_machine()
            elif self.user_input == 'remaining':
                remaining()
            elif self.user_input == 'take':
                take()


a = CoffeeMachine().rule_machine()
