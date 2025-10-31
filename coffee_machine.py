data = [
   {
      "espresso" : {
         'ingredients': {   
            'water':3,
            'milk': 10,
            'coffee': 50
         },
            'cost': 100      
                     }
   },
   {
      "latte" : {
         'ingredients': {
            'water':5,
            'milk': 14,
            'coffee': 30
         },
            'cost': 150      
                     }
   },
   {
      "cappuccino" : {
         'ingredients': {
            'water':4,
            'milk': 16,
            'coffee': 60
         },
            'cost': 190      
                     }
   }
]

report = {
           'ingredients':{
                'water':30,
                'milk': 60,
                'coffee':200  
         },
         'cost': 0  
}
      

total_cost = []
cost = []
def pay():
    print("Please insert coins.")
    ten = int(input("How many 10s: "))
    twenty = int(input("How many 20s: "))
    fifty = int(input("How many 50s: "))
    hundred = int(input("How many 100s: "))
    total = (ten*10)+(twenty*20)+(fifty*50)+(hundred*100)
    total_cost.append(total)
    print(f"Total cost: {total}")
    # return total_cost

turn_on = True

while turn_on:
    user_input = input("What would you like? (espresso/latte/cappuccino/report/off): ")

    if user_input == 'off':
      turn_on = False
    
    elif user_input == 'report':
        print(f"Water: {water_left}")
        print(f"Milk: {milk_left}")
        print(f"Coffee: {coffee_left}")
        print(f"Cost: {cost}")
    
    elif user_input == 'espresso':
        water_left = report['ingredients']['water'] - data[0]['espresso']['ingredients']['water']
        milk_left = report['ingredients']['milk'] - data[0]['espresso']['ingredients']['milk']
        coffee_left = report['ingredients']['coffee'] - data[0]['espresso']['ingredients']['coffee']

        if water_left < 0 or milk_left < 0 or coffee_left < 0:
            print("Insufficient ingredients")
        else:
            pay()
            cost.append(data[0]['espresso']['cost'])
            print(f"espresso cost: {data[0]['espresso']['cost']}")
            if data[0]['espresso']['cost'] > total_cost[-1]:
                payable = data[0]['espresso']['cost'] - total_cost[-1] 
            else:
                payable =  total_cost[-1] - data[0]['espresso']['cost']

            if total_cost[-1] == data[0]['espresso']['cost'] or total_cost[-1] > data[0]['espresso']['cost']:
                if total_cost[-1] > data[0]['espresso']['cost']:
                    print(f"Change: {payable}")
                print("Here is your espresso, enjoy!")
            else:
                print(f"{payable} is remaining, please make the payment.")

    elif user_input == 'latte':
        water_left = report['ingredients']['water'] - data[1]['latte']['ingredients']['water']
        milk_left = report['ingredients']['milk'] - data[1]['latte']['ingredients']['milk']
        coffee_left = report['ingredients']['coffee'] - data[1]['latte']['ingredients']['coffee']

        if water_left < 0 or milk_left < 0 or coffee_left < 0:
            print("Insufficient ingredients")
        else:
            pay()
            cost.append(data[1]['latte']['cost'])
            print(f"latte cost: {data[1]['latte']['cost']}")
            if data[1]['latte']['cost'] > total_cost[-1]:
                payable = data[1]['latte']['cost'] - total_cost[-1] 
            else:
                payable =  total_cost[-1] - data[1]['latte']['cost']

            if total_cost[-1] == data[1]['latte']['cost'] or total_cost[-1] > data[1]['latte']['cost']:
                if total_cost[-1] > data[1]['latte']['cost']:
                    print(f"Change: {payable}")
                print("Here is your latte, enjoy!")
            else:
                print(f"{payable} is remaining, please make the payment.")

    elif user_input == 'cappuccino':
        water_left = report['ingredients']['water'] - data[2]['cappuccino']['ingredients']['water']
        milk_left = report['ingredients']['milk'] - data[2]['cappuccino']['ingredients']['milk']
        coffee_left = report['ingredients']['coffee'] - data[2]['cappuccino']['ingredients']['coffee']

        if water_left < 0 or milk_left < 0 or coffee_left < 0:
            print("Insufficient ingredients")
        else:
            pay()
            cost.append(data[2]['cappuccino']['cost'])
            print(f"cappuccino cost: {data[2]['cappuccino']['cost']}")
            if data[2]['cappuccino']['cost'] > total_cost[-1]:
                payable = data[2]['cappuccino']['cost'] - total_cost[-1] 
            else:
                payable =  total_cost[-1] - data[2]['cappuccino']['cost']

            if total_cost[-1] == data[2]['cappuccino']['cost'] or total_cost[-1] > data[2]['cappuccino']['cost']:
                if total_cost[-1] > data[2]['cappuccino']['cost']:
                    print(f"Change: {payable}")
                print("Here is your cappuccino, enjoy!")
            else:
                print(f"{payable} is remaining, please make the payment.")

    else:
        print("Enter valid input")
    

    
        
