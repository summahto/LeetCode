class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Sumit', 'Mahto', 50000)
emp_2 = Employee('Amit', 'Mahto', 50000)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)
print(emp_2.__dict__)

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)
print(emp_2.pay)
print(Employee.raise_amount)
print(Employee.num_of_employees)


