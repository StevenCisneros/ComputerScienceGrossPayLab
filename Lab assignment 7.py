
hString = input("Enter weekly hours worked: ")
hours = float(hString)

hrString = input("Enter hourly rate: ")
hourly_rate = float(hrString)

gross_pay = 0

if hours > 40:
    new_rate = 40*hourly_rate
    overtime = (hours - 40)*1.5*hourly_rate
    gross_pay = new_rate+overtime
else:
    gross_pay = hourly_rate*hours

print ("Weekly gross pay: $",gross_pay)
