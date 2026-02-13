class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money_owed = 0
        self.number_of_treatments = 0

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_money_owed(self):
        return self.money_owed

    def get_number_of_treatments(self):
        return self.number_of_treatments

    def pay_bill(self):
        self.money_owed = 0

    def add_treatment(self, treatment, cost):
        self.number_of_treatments += 1
        self.money_owed += cost

class PatientWithInsurance(Patient):
    def __init__(self, name, age, insurance_provider, percentage_of_bill_covered):
        super().__init__(name, age)

        self.insurance_provider = insurance_provider
        self.percentage_of_bill_covered = percentage_of_bill_covered

    def get_insurance_provider(self):
        return self.insurance_provider

    def get_percentage_of_bill_covered(self):
        return self.percentage_of_bill_covered

john = Patient('John Doe', 43)
print('Name', john.get_name())
print('Age', john.get_age())
print('Number of Treatments', john.get_number_of_treatments())
print('Money Owed', john.get_money_owed())
print(' ')

john.add_treatment('Treatment 1', 100)
print('Number of Treatments', john.get_number_of_treatments())
print('Money Owed', john.get_money_owed())
print(' ')

john.pay_bill()
print('Number of Treatments', john.get_number_of_treatments())
print('Money Owed', john.get_money_owed())
print(' ')

bill = PatientWithInsurance('Bill Doe', 75, 'Aviva', 75)
print('Name', bill.get_name())
print('Age', bill.get_age())
print('Number of Treatments', bill.get_number_of_treatments())
print('Money Owed', bill.get_money_owed())
print('Insurance Provider', bill.get_insurance_provider())
print('% Covered', bill.get_percentage_of_bill_covered())
print(' ')

bill.add_treatment('Treatment 1', 100)
print('Number of Treatments', bill.get_number_of_treatments())
print('Money Owed', bill.get_money_owed())
print(' ')

bill.pay_bill()
print('Number of Treatments', bill.get_number_of_treatments())
print('Money Owed', bill.get_money_owed())
print(' ')