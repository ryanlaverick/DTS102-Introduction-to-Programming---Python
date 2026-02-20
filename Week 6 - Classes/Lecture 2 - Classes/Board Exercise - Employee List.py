class Employee:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def get_employees(self):
        return self.employees

hr_employee = Employee()
hr_employee.add_employee('John')
hr_employee.add_employee('Darcy')
print(hr_employee.get_employees())

tech_employee = Employee()
tech_employee.add_employee('Jack')
tech_employee.add_employee('Sonia')
tech_employee.add_employee('Justin')
print(tech_employee.get_employees())
