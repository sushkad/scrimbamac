

sales_w1=[7,3,42,19,15,35,9]
sales_w2 =[12,4,26,10,7,28]

sales =[]

new_day = input("Enter # of lemonades for new days : ")
sales_w2.append(int(new_day))


sales = sales_w1 + sales_w2

#sales.sort()

worst_day = min(sales) * 1.5
best_day = max(sales) * 1.5

print(f'worst_day : {worst_day}')
print(f'best_day : {best_day}')
print(f'sales : {sales}')