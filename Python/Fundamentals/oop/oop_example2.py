class Employee():
    def __init__(self, f_name, m_name, l_name, starting_salary):
        self.first_name = f_name
        self.middle_name = m_name
        self.last_name = l_name
        self.salary = starting_salary
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_last_name}"


new_employee_1 = Employee('Mark', 'jake' 'Adams', 80000)
new_employee_2 = Employee('Sarah', 'Smith', 73000)
new_employee_3 = Employee('Adam', 'Jones', 57000)

employees = [new_employee_1, new_employee_2, new_employee_3]

for employee in employees:
    print(f"{employee.full_name()}")
