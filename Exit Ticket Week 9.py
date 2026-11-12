#1
#car = input("What kind of car are you looking for?")
#print("Let me see if i can find you a", car)
#2
#table = input("How many people are in your group?")
    #print("your table is ready")
#elif int(table) > 8:
    #print("you will have to wait for a table")
#3
#number = input("type a number")
#if int(number)%10 == 0:
    #print("your number is a multiple of 10")
#else:
    #print("your number is not a multiple of 10")
#4
#toppings = input("What toppings would you like?")
#while toppings != "quit":
    #print("your toppings are ", toppings)
    #toppings = input("What toppings would you like?")
#5
#active = True
#while active:
    #toppings = input("What toppings would you like?")
    #if toppings == "quit":
        #active = False
        #break
    #else:
        #print("your toppings are ", toppings)
#6
#infinite = input("Enter a number: ")
#while infinite != "":
    #print(infinite)

#7
#sandwich_orders = ["Turkey", "Meatball", "Tuna"]
#finished_sandwiches = []
#while sandwich_orders:
    #orders = sandwich_orders.pop()
    #print("I made your order:", orders)
    #finished_sandwiches.append(orders)
#print(finished_sandwiches)

#8
#places = []
#place = input("Where would you go? ")
#while place != "quit":
    #places.append(place)
    #place = input("Where would you go? (or 'quit')")
#print(places)

#9
#import matplotlib.pyplot as plt
#expenses = {}
#expenses["Food"] = float(input("Food: "))
#expenses["Transportation"] = float(input("Transportation:"))
#expenses["Entertainment"] = float(input("Entertainment:"))
#plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
#plt.show()

#10
#import matplotlib.pyplot as plt
#study_hours = {}
#study_hours["Python"] = int(input("Python hours:"))
#study_hours["Math"] = int(input("Math hours:"))
#study_hours["Science"] = int(input("Science hours:"))
#plt.bar(study_hours.keys(), study_hours.values())
#plt.title("Study Hours")
#plt.xlabel("Subjects")
#plt.ylabel("Hours")
#plt.show()

#11
#temperatures = []
#again = "yes"
#while again != "no":
    #temperatures.append(int(input("Enter temperature:")))
    #again = input("Another? (yes/no)")
#print(temperatures)
#print("Highest:", max(temperatures))
#print("Lowest:", min(temperatures))

#12
#grades = {}
#again = "yes"
#while again != "no":
    #name = input("Name:")
    #grades[name] = int(input("Grade:"))
    ##again = input("Another? (yes/no)")
#print(grades)
#print("Average:", sum(grades.values()) / len(grades))

#13
#foods = []
#again = "yes"
#while again != "no":
    #foods.append(input("Enter food:"))
    #again = input("Another? (yes/no)")
#print(foods)
#search = input("Search food:")
#if search in foods:
    #print("In the list")
#else:
    #print("Not in the list")

#14
#inventory = {}
#again = "yes"
#while again != "no":
    #product = input("Product: ")
    #inventory[product] = int(input("Quantity:"))
    #again = input("Another? (yes/no)")
#print(inventory)
#print("Total:", sum(inventory.values()))

#15
#items = []
#prices = []
#again = "yes"
#while again != "no":
    #items.append(input("Item:"))
    #prices.append(float(input("Price:")))
    #again = input("Another? (yes/no)")
#print(items, prices)
#total = sum(prices)
#print("Total:", total)
#budget = float(input("Budget: "))
#if total <= budget:
    #print("Remaining:", budget - total)
#else:
    #print("Over budget:", total - budget)

#16
movies = []
ratings = []
again = "yes"
while again != "no":
    movies.append(input("Movie:"))
    ratings.append(int(input("Rating (1-5):")))
    again = input("Another? (yes/no)")
print(movies, ratings)
print("Highest:", max(ratings))






