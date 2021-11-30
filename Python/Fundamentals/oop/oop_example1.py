first_employee = {'first_name': 'mike', 'last_name': 'Lawson', 'salary': 78000}
second_employee = {'first_name': 'Sarah', 'last_name': 'Micheals', 'salary': 91000}
third_employee = {'first_name': 'Adam', 'last_name': 'Jones', 'salary': 53000}

employees= [first_employee, second_employee, third_employee]

for employee in employees:
    employee['salary'] *= 1.05
    print(employee['salary'])