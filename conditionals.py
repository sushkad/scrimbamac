
# optimize/shorten the code in the function
# try to reduce the number of conditionals
# always use set

def num_days(month):
    days = 31
    if month in {'apr','jun','sep','nov'}:
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)

num_days('jan')
num_days('feb')
num_days('apr')
num_days('may')
num_days('jun')
num_days('jul')


