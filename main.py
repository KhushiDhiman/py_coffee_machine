MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee":24,
        },
    }
}
profit = 0
resources ={
    "water":300,
    "milk" :200,
    "coffee":100,
}
def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("Insert coins")
    total = int(input("How many quarters ? ")) * 0.25
    total += int(input("How many dimes ? ")) * 0.1
    total += int(input("How many nickels ? ")) * 0.05
    total += int(input("How many pennies ? ")) * 0.01
    return total

def is_transaction_successful(recieved_money, drink_cost):
    if recieved_money > drink_cost:
       change = round(recieved_money - drink_cost,2)
       print(f"Here is a change {change}")
       global profit
       profit += drink_cost
       return True
    else:
        print("Sorry that's not enough money , Money refunded")
        return False

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient [item]
    print(f"Here is your {drink_name}")



is_on = True
while is_on:
    user_ip = input("What would you like ? (espresso/latte/cappuccino) :")
    if user_ip == "off":
        is_on = False
    elif user_ip == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[user_ip]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(user_ip,drink["ingredients"])










