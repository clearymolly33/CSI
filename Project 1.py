#Shopper 1
name1 = "jami"
grocery_price1 = 1.50
grocery_price2 = 2.00
grocery_price3 = 3.25
grocery_price4 = 1.99
grocery_price5 = 4.50
grocery_count1 = 3
grocery_count2 = 2
grocery_count3 = 1
grocery_count4 = 5
grocery_count5 = 2
total_bill = (grocery_price1 * grocery_count1) + (grocery_price2 * grocery_count2) + (grocery_price3 * grocery_count3) + (grocery_price4 * grocery_count4) + (grocery_price5 * grocery_count5)
total_items = grocery_count1 + grocery_count2 + grocery_count3 + grocery_count4 + grocery_count5
average_price = total_bill / total_items
total_bill = round(total_bill, 2)
average_price = round(average_price, 2)
print(f"{name1.title()}: Total bill ${total_bill}, average price per item ${average_price}")

#Shopper 2
name2 = "david"
grocery_price1 = 2.50
grocery_price2 = 1.15
grocery_price3 = 5.00
grocery_price4 = 0.50
grocery_price5 = 3.75
grocery_count1 = 1
grocery_count2 = 4
grocery_count3 = 2
grocery_count4 = 6
grocery_count5 = 1
total_bill = (grocery_price1 * grocery_count1) + (grocery_price2 * grocery_count2) + (grocery_price3 * grocery_count3) + (grocery_price4 * grocery_count4) + (grocery_price5 * grocery_count5)
total_items = grocery_count1 + grocery_count2 + grocery_count3 + grocery_count4 + grocery_count5
average_price = total_bill / total_items
total_bill = round(total_bill, 2)
average_price = round(average_price, 2)
print(f"{name2.title()}: Total bill ${total_bill}, average price per item ${average_price}")