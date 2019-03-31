food = input("Enter your food: ")
"""
if food == "apple":
    time = "21 days."
elif food == "banana.":
    time = "7 days"
elif food == "bread.":
    time = "30 days."
elif food == "peanut butter.":
    time = "80 days."
elif food == "chicken curry.":
    time = "2 days."
elif food == "sushi.":
    time = "3 days."
elif food == "sashimi.":
    time = "3 days."
elif food == "pudding.":
    time = "20 days."
elif food == "pad thai.":
    time = "2 days."
elif food == "burrito":
    time = "3 days."
elif food == "cup noodles.":
    time = "100 days."
elif food == "chocolate.":
    time = "100 days."
elif food == "pizza.":
    time = "7 days."
print(food, "expires in", time)
"""
food_dic={"apple" : 3,
          "burrito" : 5,
          "pudding" : 10,
          "chocolate" : 100,
          "pizza" : 7,
          "cup noodles" : 365,
          "chicken curry" : 2,
          "burrito" : 3,
          "bread" : 30,
          "banana" : 7,
          "pad thai" : 2,
          "sashimi" : 1,
          "peanut butter" : 80,
          "ice-cream" : 7,
          "french fries" : 4,
          "steak" : 4,
          "cripsy fried chicken" : 6,
          "chocolate chip cookies" : 40,
          "cheesecake" : 7,
          "bacon" : 3,
          "cheeseburger" : 8,
          "cheese" : 42,
          "taco" : 3,
          "brownie" : 4,
          "barbecue" : 4,
          "strawberries" : 6,
          "donuts" : 3,
          "pasta" : 2,
          "cake" : 3,
          "waffles" : 90,
          "pancakes" : 180,
          "salmon" : 2,
          "mangoes" : 7,
          "oranges" : 14,
          "raspberries" : 3,          
          }


if food in food_dic:
    print("{} will expire in {} days".format(food, food_dic[food]))
    
