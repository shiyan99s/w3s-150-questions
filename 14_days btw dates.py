from datetime import date

f_date = int(input("Enter first date: "))
f_month = int(input("Enter first month: "))
f_year = int(input("Enter first year: "))

l_date = int(input("Enter last date: "))
l_month = int(input("Enter last month: "))
l_year = int(input("Enter last year: "))

f_final = date(f_year, f_month, f_date)
l_final = date(l_year, l_month, l_date)

delta = l_final - f_final

print(delta.days)