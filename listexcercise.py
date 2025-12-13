

sales_w1=[7,3,42,19,15,35,9]
sales_w2 =[12,4,26,10,7,28]

sales =[]

new_day = input("Enter # of lemonades for new days")
sales_w2.append(int(new_day))


sales = sales_w1 + sales_w2

sales.sort()

worst_day = sales[0] * 1.5
best_day = sales[-1] * 1.5

print(worst_day)
print(best_day)
print(sales)